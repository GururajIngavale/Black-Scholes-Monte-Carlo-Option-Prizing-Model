# Black-Scholes & Monte Carlo Option Pricing Model

### 📊 Project Overview

This repository presents a robust quantitative finance model for the **accurate and efficient valuation of financial options**. It features parallel implementations of two industry-standard pricing techniques: the **Black-Scholes (BS) analytical formula** and the **Monte Carlo (MC) simulation method** using Geometric Brownian Motion (GBM).

The primary goal is to provide a clear, functional comparison between these models, highlighting the speed and simplicity of the analytical solution versus the flexibility and power of the numerical simulation approach for derivatives pricing.

---

### ✨ Key Features

* **Dual Pricing Model:** Calculate the fair price of **European Call and Put Options** using both the Black-Scholes formula and the Monte Carlo simulation.
* **Geometric Brownian Motion (GBM):** Simulate thousands of potential asset price paths to derive option payoff distributions. 
* **Comparative Analysis:** Directly compare the results and computational efficiency of the analytical Black-Scholes solution against the Monte Carlo estimate.
* **Volatility Analysis:** Incorporate key option pricing parameters, including underlying stock price ($S_0$), strike price ($K$), risk-free rate ($r$), time to maturity ($T$), and volatility ($\sigma$).
* **Pythonic Implementation:** Utilizes industry-standard quantitative libraries for fast and accurate computation.

---

### 🏗️ Architecture Diagram

```bash
INPUTS (S, K, T, r, σ)
          ↓
black_scholes.py       → Price Call/Put analytically
          ↓
greeks.py              → Compute Greeks
          ↓
implied_vol.py         → Newton–Raphson IV solver
          ↓
monte_carlo.py         → Stochastic simulation pricing
          ↓
main.py                → Final combined output

```

### ⚙️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core implementation language. |
| **NumPy** | Optimized numerical operations and array handling. |
| **SciPy** | Statistical functions (e.g., Cumulative Distribution Function for Black-Scholes). |
| **Pandas** | Data structuring and input handling (if reading market data). |

---


### ⚙️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GururajIngavale/Black-Scholes-Monte-Carlo-Option-Prizing-Model/tree/main
cd Black-Scholes-Monte-Carlo-Option-Prizing-Model
```

### 2️⃣ Install Dependencies
#### Required packages:
```bash
numpy  
scipy  
math
```

### ▶️ Run the Full Engine
```bash
python main.py
```


### You will enter:

```bash

Stock Price (S)

Strike Price (K)

Time to Expiry (T)

Risk-Free Rate (r)

Volatility (σ)

Current Market Price (for IV)
```

### 📊 Sample Input & Output

```bash
Current Stock Price : 80
Strike Price :100
Time To Expiration in Years:1
Risk Free Intreast Rate in % :5
Volatility in % : 30
-----------------------------------------
Option Prices:
-----------------------------------------
Call Price : 4.55
Put Price  : 19.68
-----------------------------------------
Greeks:
-----------------------------------------
Delta_call = 0.335
Delta put  = -0.665
Gamma      = 0.0152
Vega       = 29.133
Call_Theta = -5.481
Put_Theta  = -0.725
Call_Rho   = 22.218
Put_Rho    = -72.905
Current Market Price : 4.55
Implied Volatility (call) : 0.300
Current Market Price : 4.55
Call Price : 4.417
Put Price : 19.745
------------------------------------------------
Black–Scholes Call: 4.553219350065298
Black–Scholes Put : 19.676161800136697
Monte Carlo Call  : 4.417258237839932
Monte Carlo Put   : 19.74498997331014
Implied Volatility: 0.2998894873048196

```

### ⭐ Support

If you like this project, please star ⭐ the repository — it means a lot!
```

