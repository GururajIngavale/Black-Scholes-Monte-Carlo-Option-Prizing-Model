from scipy.stats import norm
from monte_carlo import MC
import math




# Input parameters required to calculate values from black scholes formula 
s = float(input("Current Stock Price : "))

if(s<0):
    while s<=0:
        print("Enter values greater than 0")
        s = float(input("Current Stock Price : "))


k = float(input("Strike Price :"))
if(k<0):
    while k<=0:
        print("Enter values greater than 0")
        k = float(input("Strike Price :"))

t = float(input("Time To Expiration in Years:"))
if(t<0):
    while t<=0:
        print("Enter values greater than 0")
        t = float(input("Time To Expiration :"))

r = float(input("Risk Free Intreast Rate :"))/100
sigma = float(input("Volatility : "))/100


def black_shcholes(s, k, t, r, sigma):



    # -------------------------------------------------
    # Balck Scholes Formula calculation 
    # -------------------------------------------------
    # D1 derived based on input variables.

    d1 = (math.log(s/k) + (r + 0.5 * sigma*sigma)*t) / (sigma * math.sqrt(t))


    # D2 derived based on input variables.

    d2 = d1 - sigma * math.sqrt(t)

    # -------------------------------------------------
    # Calculation to find Call price of trade
    # -------------------------------------------------

    c = (s*norm.cdf(d1)) - (k*math.exp(-r*t)*norm.cdf(d2))

    # -------------------------------------------------
    # Calculation to find Put price of trade
    # -------------------------------------------------

    p = (k*math.exp(-r*t)*norm.cdf(-d2))-(s*norm.cdf(-d1))

    
    return d1, d2, c, p



#---------------------------------------------------------------------------------------------------- 
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#---------------------------------------------------------------------------------------------------- 

# CALCULATING GREEKS BASED ON BLACK SCHOLES MODEL : 


def greeks(s, k, t, r, sigma, d1, d2):

    # Delta Call
    delta_call = norm.cdf(d1)

    # Delta Put
    delta_put = norm.cdf(d1)-1

    # Gamma
    lower = sigma * math.sqrt(t)
    two_pi = (math.pi)*2
    nd1 = (1/math.sqrt(two_pi))*math.exp(-((d1*d1)/2))
    gamma = nd1/(s*sigma * math.sqrt(t))

    # Vega(v)
    vega = s*nd1*(math.sqrt(t))

    # Theta 

    call_theta = ((-s*nd1*sigma)/(2*math.sqrt(t)))-(r*k*math.exp(-r*t)*norm.cdf(d2))
    put_theta = ((-s*nd1*sigma)/(2*math.sqrt(t)))+(r*k*math.exp(-r*t)*norm.cdf(-d2))

    # Rho

    call_rho = k*t*math.exp(-r*t)*norm.cdf(d2)
    put_rho = -k*t*math.exp(-r*t)*norm.cdf(-d2)

    return delta_call, delta_put, gamma, vega, call_theta, put_theta, call_rho, put_rho

# Greeks Function Called)

def Implied_Volatility(s, k, t, r, option_type="call"):
    market_price = float(input("Current Market Price : "))
    sigma = 0.2   # starting point

    for i in range(100):
        # Recompute everything every loop for new sigma

        # D1 derived based on input variables.
        d1 = (math.log(s/k) + (r + 0.5 * sigma*sigma)*t) / (sigma * math.sqrt(t))

        # D2 derived based on input variables.
        d2 = d1 - sigma * math.sqrt(t)


        # BS Price 
        bs_price = (s*norm.cdf(d1)) - (k*math.exp(-r*t)*norm.cdf(d2))

        # Vega Calcukated 
        two_pi = (math.pi)*2
        nd1 = (1/math.sqrt(two_pi))*math.exp(-((d1*d1)/2))
        vega = s*nd1*(math.sqrt(t))

        diff = bs_price - market_price
        sigma = sigma - diff / vega

    return sigma


# ---------- Run calculations ----------
d1, d2, c, p = black_shcholes(s, k, t, r, sigma)


print("""-----------------------------------------
Option Prices:
-----------------------------------------""")
print(f"Call Price : {c:.2f}")
print(f"Put Price  : {p:.2f}")


delta_call, delta_put, gamma, vega, call_theta, put_theta, call_rho, put_rho = \
    greeks(s, k, t, r, sigma, d1, d2)

print("""-----------------------------------------
Greeks:
-----------------------------------------""")
print(f"Delta_call = {delta_call:.3f}")
print(f"Delta put  = {delta_put:.3f}")
print(f"Gamma      = {gamma:.4f}")
print(f"Vega       = {vega:.3f}")
print(f"Call_Theta = {call_theta:.3f}")
print(f"Put_Theta  = {put_theta:.3f}")
print(f"Call_Rho   = {call_rho:.3f}")
print(f"Put_Rho    = {put_rho:.3f}")

iv = Implied_Volatility(s, k, t, r, option_type="call")
print(f"Implied Volatility (call) : {iv:.3f}")
