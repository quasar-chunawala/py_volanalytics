# The Heath-Jarrow-Morton(HJM) Framework

## Introduction

A no-arbitrage model is designed to be consistent with today's term structure of interest rates. 

In equilibrium (short-rate models) once we have a specification, for example, a stochastic differential equation governing the short-rate:

$$
dr_t = a(r(t) - b)dt + \eta dW^{Q}(t)
$$

we calibrate all the parameters to the prices of the market instruments, such as zero coupon bonds, and the output of the model is the yield curve. 

On the other hand, we have exogenous models (no-arbitrage models), where the model takes the yield curve, that is, today's term structure of interest rates as an input. This means that whatever parameters we choose, the model always gives us the yield curve back. Essentially, you always get your yield curve back from the model and it is independent of the parameters. So, this is an extremely powerful part of the HJM framework.

The HJM framework describes a clear path from the equilibrium towards term-structure models.

