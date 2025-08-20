
"""
Feature selection with metaheuristics: Simulated Annealing (SA) and Genetic Algorithm (GA)
Author: ChatGPT for Mauricio
Language: English (code), Spanish (report)
"""

from dataclasses import dataclass
from typing import List, Callable, Tuple, Dict
import time, math, random
import numpy as np

from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression

@dataclass
class SearchResult:
    best_mask: np.ndarray
    best_score: float
    history: List[float]
    elapsed: float
    iters: int

def evaluate_mask(X: np.ndarray, y: np.ndarray, mask: np.ndarray, cv_splits: int = 5) -> float:
    """Return mean CV accuracy for selected features; if mask is all False, return 0."""
    if mask.sum() == 0:
        return 0.0
    clf = LogisticRegression(max_iter=2000, n_jobs=None)
    cv = StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=42)
    scores = cross_val_score(clf, X[:, mask], y, cv=cv, scoring="accuracy")
    return float(scores.mean())

def random_neighbor(mask: np.ndarray, p_flip: float = 0.2) -> np.ndarray:
    """Flip each bit with probability p_flip; ensure at least one bit True."""
    m = mask.copy()
    for i in range(len(m)):
        if random.random() < p_flip:
            m[i] = ~m[i]
    if m.sum() == 0:
        idx = random.randrange(len(m))
        m[idx] = True
    return m

def simulated_annealing(X: np.ndarray, y: np.ndarray, iters: int = 150, init_temp: float = 1.0,
                        cooling: float = 0.97, p_flip: float = 0.2, cv_splits: int = 5) -> SearchResult:
    n_features = X.shape[1]
    current = np.random.rand(n_features) < 0.5
    best = current.copy()
    current_score = evaluate_mask(X, y, current, cv_splits=cv_splits)
    best_score = current_score
    history = [best_score]
    T = init_temp
    start = time.perf_counter()
    for it in range(iters):
        neighbor = random_neighbor(current, p_flip=p_flip)
        neighbor_score = evaluate_mask(X, y, neighbor, cv_splits=cv_splits)
        delta = neighbor_score - current_score
        if delta >= 0 or math.exp(delta / max(T, 1e-8)) > random.random():
            current = neighbor
            current_score = neighbor_score
        if current_score > best_score:
            best = current.copy()
            best_score = current_score
        history.append(best_score)
        T *= cooling
    elapsed = time.perf_counter() - start
    return SearchResult(best_mask=best, best_score=best_score, history=history, elapsed=elapsed, iters=iters)

def tournament_selection(pop: np.ndarray, fitness: np.ndarray, k: int = 3) -> np.ndarray:
    idxs = np.random.choice(len(pop), size=k, replace=False)
    best_idx = idxs[np.argmax(fitness[idxs])]
    return pop[best_idx].copy()

def crossover(p1: np.ndarray, p2: np.ndarray, rate: float = 0.9) -> Tuple[np.ndarray, np.ndarray]:
    if random.random() > rate or len(p1) < 2:
        return p1.copy(), p2.copy()
    point = random.randint(1, len(p1) - 1)
    c1 = np.concatenate([p1[:point], p2[point:]])
    c2 = np.concatenate([p2[:point], p1[point:]])
    return c1, c2

def mutate(mask: np.ndarray, p_mut: float = 0.02) -> np.ndarray:
    m = mask.copy()
    for i in range(len(m)):
        if random.random() < p_mut:
            m[i] = ~m[i]
    if m.sum() == 0:
        m[random.randrange(len(m))] = True
    return m

def genetic_algorithm(X: np.ndarray, y: np.ndarray, pop_size: int = 30, generations: int = 50,
                      p_crossover: float = 0.9, p_mut: float = 0.02, cv_splits: int = 5) -> SearchResult:
    n_features = X.shape[1]
    pop = np.random.rand(pop_size, n_features) < 0.5
    start = time.perf_counter()
    fitness = np.array([evaluate_mask(X, y, ind, cv_splits=cv_splits) for ind in pop])
    best_idx = int(np.argmax(fitness))
    best = pop[best_idx].copy()
    best_score = float(fitness[best_idx])
    history = [best_score]
    for g in range(generations):
        new_pop = []
        while len(new_pop) < pop_size:
            p1 = tournament_selection(pop, fitness)
            p2 = tournament_selection(pop, fitness)
            c1, c2 = crossover(p1, p2, rate=p_crossover)
            c1 = mutate(c1, p_mut=p_mut)
            c2 = mutate(c2, p_mut=p_mut)
            new_pop.extend([c1, c2])
        pop = np.array(new_pop[:pop_size])
        fitness = np.array([evaluate_mask(X, y, ind, cv_splits=cv_splits) for ind in pop])
        gen_best_idx = int(np.argmax(fitness))
        gen_best_score = float(fitness[gen_best_idx])
        if gen_best_score > best_score:
            best_score = gen_best_score
            best = pop[gen_best_idx].copy()
        history.append(best_score)
    elapsed = time.perf_counter() - start
    return SearchResult(best_mask=best, best_score=best_score, history=history, elapsed=elapsed, iters=generations)
