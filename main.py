# from Black_Sholes import black_shcholes
# from monte_carlo import MC


# black_shcholes()
# MC()
import Black_Sholes
from Black_Sholes import black_shcholes
from Black_Sholes import greeks
from monte_carlo import MC
from Black_Sholes import Implied_Volatility

# Step 1 — Inputs
sigma = Black_Sholes.sigma
s = Black_Sholes.s
k = Black_Sholes.k
r = Black_Sholes.r
t = Black_Sholes.t

# Step 2 — Black–Scholes
d1, d2, call_bs, put_bs = black_shcholes(s, k, t, r, sigma)

# Step 3 — Greeks
delta_c, delta_p, gamma, vega, theta_c, theta_p, rho_c, rho_p = greeks(s, k, t, r, sigma, d1, d2)

# Step 4 — Implied Volatility
iv = Implied_Volatility(s, k, t, r, call_bs)

# Step 5 — Monte Carlo
call_price, put_price = MC(s, k, t, r, sigma, simulations=10000)

# Step 6 — Output
print("""------------------------------------------------""")
print("Black–Scholes Call:", call_bs)
print("Black–Scholes Put :", put_bs)
print("Monte Carlo Call  :", call_price)
print("Monte Carlo Put   :", put_price)
print("Implied Volatility:", iv)
