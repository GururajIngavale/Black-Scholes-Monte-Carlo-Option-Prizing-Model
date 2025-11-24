# Black-Scholes & Monte Carlo Option Pricing Model

## 📊 Project Overview

This repository presents a robust quantitative finance model for the **accurate and efficient valuation of financial options**. It features parallel implementations of two industry-standard pricing techniques: the **Black-Scholes (BS) analytical formula** and the **Monte Carlo (MC) simulation method** using Geometric Brownian Motion (GBM).

The primary goal is to provide a clear, functional comparison between these models, highlighting the speed and simplicity of the analytical solution versus the flexibility and power of the numerical simulation approach for derivatives pricing.

---

## ✨ Key Features

* **Dual Pricing Model:** Calculate the fair price of **European Call and Put Options** using both the Black-Scholes formula and the Monte Carlo simulation.
* **Geometric Brownian Motion (GBM):** Simulate thousands of potential asset price paths to derive option payoff distributions. 
* **Comparative Analysis:** Directly compare the results and computational efficiency of the analytical Black-Scholes solution against the Monte Carlo estimate.
* **Volatility Analysis:** Incorporate key option pricing parameters, including underlying stock price ($S_0$), strike price ($K$), risk-free rate ($r$), time to maturity ($T$), and volatility ($\sigma$).
* **Pythonic Implementation:** Utilizes industry-standard quantitative libraries for fast and accurate computation.

---

## ⚙️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core implementation language. |
| **NumPy** | Optimized numerical operations and array handling. |
| **SciPy** | Statistical functions (e.g., Cumulative Distribution Function for Black-Scholes). |
| **Pandas** | Data structuring and input handling (if reading market data). |

---

## 🚀 Installation & Setup

To run this model locally, you will need a Python environment (Python 3.7+ is recommended).

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install numpy scipy pandas
```
