# Card State Optimization

> *The idea of this project came from a simple thought experiment rather than a textbook problem.*

> **If every card is randomly oriented, is it always better to fix one card at a time, or can a global operation surprisingly outperform local corrections?**

This project began with that simple question.

Instead of trying to answer it intuitively, I decided to treat it as a computational experiment.

Starting from a minimal binary-state model, different state-transition strategies are implemented and evaluated on randomly generated sequences. Their performances are compared through large-scale simulations to understand how local and global operations behave under identical conditions.

Although inspired by a simple card problem, the framework is intentionally designed to be extensible. Future versions will introduce richer state representations, additional strategies, probabilistic operations, and theoretical analysis.

---

## Current MVP

The first version investigates two deterministic strategies on random binary sequences.

### Strategy A — Local Fix

When a `0` is encountered during a left-to-right scan, only the current element is corrected.

```
0 → 1
```

---

### Strategy B — Suffix Flip

When a `0` is encountered, every element from the current position to the end of the sequence changes its state.

```
0 ↔ 1
```

---

## Experimental Setup

- Binary state model
- Random sequence generation
- Sequence length: 50 / 100
- Left-to-right traversal
- Monte Carlo simulation
- Performance comparison

---

## Evaluation Metrics

The project currently compares strategies using:

- Number of operations
- Average operations
- Execution time

More statistical metrics will be introduced in future versions.

---

## Future Directions

This repository is not intended to remain a simple "card-flipping" simulator.

Future work includes:

- Multi-dimensional card states
- Additional transition strategies
- State-space analysis
- Optimal strategy search
- Monte Carlo optimization
- Dynamic programming
- Reinforcement learning
- Markov Decision Process (MDP)

The long-term goal is to build a general experimental framework for studying optimization strategies in finite-state systems.

---

> *Every project starts with a question.*
>
> *This repository is my attempt to answer one of them.*

## Project Progress

### Version 0.1（2026-07-13）
- Implemented sequence generator.
- Implemented Local Fix strategy.
- Implemented Suffix Flip strategy.
- Verified algorithm correctness using single-case experiments.

### Version 0.2（2026-07-14）
- Built a Monte Carlo simulation framework.
- Compared both strategies over a large number of random sequences.
- Observed that both strategies require approximately n/2 operations on average under uniformly random binary sequences.
- Proposed future investigations into different input distributions and theoretical analysis.
