from scipy.stats import norm
import numpy as np
import Black_Sholes
import math


def MC(s, k, t, r, sigma,simulations = 10000):
    
    z = np.random.standard_normal(simulations)

    sigma = Black_Sholes.sigma
    s = Black_Sholes.s
    k = Black_Sholes.k
    r = Black_Sholes.r
    t = Black_Sholes.t

    # Calculating future price 

    st = s * np.exp((r - 0.5 * sigma**2) * t + sigma * np.sqrt(t) * z)

    # Calculating Payoff for call option 

    call_payoffs = np.maximum(st-k,0)

    # Calculating Payoff for put option

    put_payoffs = np.maximum(k-st,0)

    # This gives the expected payoff at expiration.

    avg_call = np.mean(call_payoffs)
    avg_put  = np.mean(put_payoffs)

    # Step 6: Discount back to present value
    call_price = math.exp(-r * t) * avg_call
    put_price  = math.exp(-r * t) * avg_put

    print(f"Call Price : {call_price:.3f}")
    print(f"Put Price : {put_price:.3f}")

    return call_price, put_price

