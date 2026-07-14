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

### v0.3 — Clustered Input Sensitivity Analysis

- Introduced a clustered sequence generator controlled by clustering probability $p$ to simulate non-random input structures.
- Extended Monte Carlo experiments to compare Local Fix and Suffix Flip under different clustering levels.
- Observed that Suffix Flip gains increasing advantages as input clustering increases.
- Found an approximately linear relationship between performance gap $\Delta$ and clustering probability:

$$
\Delta=48.8958p-24.4336
$$

with a linear regression result of:

$$
R^2=0.9999
$$

- Explored the relationship between $\Delta$ and expected cluster length $1/(1-p)$, finding a nonlinear trend.

## Author Notes
I am delighted to be able to independently raise questions, think about models, design experiments for the first time, and ultimately achieve a fairly beautiful result. It cannot be denied that in this era, development and research are increasingly inseparable from the assistance of AI tools. In this project, my ChatGPT mainly helped me with code debugging, discussion of implementation ideas, and language organization of experimental results. But the direction of the entire experiment is still determined by myself. From initially comparing two simple strategies, to discovering that they perform similarly under random input, to further considering whether input structure affects algorithm performance and designing a clustered sequence generator for validation, each step of exploration is based on one's own observations and judgments. I am currently only a freshman and have not systematically studied higher-level mathematics courses such as stochastic processes. My experience in Python engineering practice is also very limited. But through this project, I experienced for the first time the feeling of starting from a vague problem, gradually forming a complete research process through model construction, experimental verification, and result analysis. This project may not be perfect, as there are many phenomena waiting for deeper theoretical explanations. But it made me realize that even when faced with knowledge that I haven't fully mastered, I can approach the answer by asking questions, designing experiments, and constantly exploring. I am willing to encourage everyone.

很高兴能够第一次独立提出问题、思考模型、设计实验，并最终得到一个还算漂亮的结果。

不可否认，在现在这个时代，开发与研究已经越来越离不开 AI 工具的辅助。在这个项目中，我的 ChatGPT 主要帮助我进行代码调试、实现思路讨论以及实验结果的语言整理。

但整个实验的推进方向，依然由我自己决定。从最初比较两个简单策略，到发现随机输入下两者表现接近，再到进一步思考输入结构是否会影响算法性能，并设计 clustered sequence generator 进行验证，每一步探索都是基于自己的观察与判断。

我目前只是一名大一学生，还没有系统学习随机过程等更高阶数学课程，对于 Python 工程实践的经验也十分有限。但通过这个项目，我第一次体会到了从一个模糊的问题出发，经过模型构建、实验验证和结果分析，逐渐形成一个完整研究过程的感觉。

这个项目或许并不完美，其中还有许多现象等待更深入的理论解释。但它让我认识到，即使面对尚未完全掌握的知识，也可以通过提出问题、设计实验和不断探索去接近答案。

愿与各位共勉。