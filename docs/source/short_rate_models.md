# One-Factor Short Rate Models

## Introduction

We start by establishing a few important definitions.

**(Definition) Stochastic Discount Factor.**
The (stochastic) discount factor $D(t,T)$ between two time instants $t$ and $T$ is the amount at time $t$ that is equivalent to one unit of currency payable at time $T$ and is given by:

$$
D(t,T) = \frac{M(t)}{M(T)} = \exp\left(-\int_t^T r_s ds \right)
$$

The instantaneous rate of interest $r(t)$ is called the *short-rate*.

**(Definition) Zero-Coupon Bonds and Spot Interest rates.** A $T$-maturity zero-coupon bond (pure discount bond) is a contract that guarantees its holder the payment of one unit of currency at time $T$ with no intermediate payments. The contract value at time $t < T$ is denoted by $P(t,T)$. Clearly, $P(T,T) = 1$. By the risk-neutral pricing formula, we have:

$$
\begin{aligned}
P(t,T) &= \mathbb{E}^{Q}\left[\frac{M(t)}{M(T)} V_T\right]\\
&= \mathbb{E}^{Q}\left[D(t,T) \cdot 1\right]\\
&= \mathbb{E}^{Q}[D(t,T)]
\end{aligned}
$$

