📘 Black–Scholes & Monte Carlo Option Pricing Engine
<p align="center"> <img src="https://img.shields.io/badge/Finance-Quant%20Modeling-blue" /> <img src="https://img.shields.io/badge/Python-3.10+-yellow" /> <img src="https://img.shields.io/badge/Status-Complete-success" /> <img src="https://img.shields.io/badge/License-MIT-green" /> </p>

A fully-functional Options Pricing Engine implementing:

🧮 Black–Scholes Analytical Model

📈 Greeks (Delta, Gamma, Vega, Theta, Rho)

🔁 Implied Volatility via Newton–Raphson

🎲 Monte Carlo Simulation for Pricing

🧩 Modular Architecture (Production-Ready)

This project follows industry quant standards — perfect for Financial Data Analysts, Quant Roles, and Portfolio Building.

🚀 Features
📘 Black–Scholes Model

European Call & Put Pricing

d1, d2 calculation

Closed-form analytical solution

📊 Greeks Calculation

Delta (Call & Put)

Gamma

Vega

Theta (Call & Put)

Rho (Call & Put)

🧠 Implied Volatility Solver

Newton–Raphson method

Converges efficiently

Computes σ from market price

🎲 Monte Carlo Simulation

Simulates thousands of price paths

GBM stochastic modeling

Validates Black–Scholes outputs

🏗 Modular Project Structure
project/
│
├── main.py
├── black_scholes.py
├── greeks.py
├── implied_vol.py
├── monte_carlo.py
└── README.md

🛠 Installation
git clone https://github.com/yourusername/Black-Scholes-Option-Pricing.git
cd Black-Scholes-Option-Pricing

pip install -r requirements.txt


Libraries used:

numpy  
scipy  
math  

▶️ Usage

Run:

python main.py


You will be prompted to enter:

Stock Price (S)

Strike Price (K)

Time to Expiry (T)

Risk-Free Rate (r)

Volatility (σ)

Market Price (for IV calculation)

The output includes:

Black–Scholes Call/Put Price

Greeks

Implied Volatility

Monte Carlo Call/Put Price

🔍 Example Output
Option Prices:
-----------------------------------------
Call Price : 4.55
Put Price  : 19.68

Greeks:
-----------------------------------------
Delta_call = 0.335
Delta_put  = -0.665
Gamma      = 0.0152
Vega       = 29.133
Theta_call = -5.481
Theta_put  = -0.725

Implied Volatility (call) : 0.300

Monte Carlo Simulation:
-----------------------------------------
MC Call Price : 4.652
MC Put Price  : 19.638

🧩 Mathematical Models Used
🎯 Black–Scholes Formula
𝐶
=
𝑆
⋅
𝑁
(
𝑑
1
)
−
𝐾
𝑒
−
𝑟
𝑇
𝑁
(
𝑑
2
)
C=S⋅N(d
1
	​

)−Ke
−rT
N(d
2
	​

)
𝑑
1
=
ln
⁡
(
𝑆
/
𝐾
)
+
(
𝑟
+
0.5
𝜎
2
)
𝑇
𝜎
𝑇
d
1
	​

=
σ
T
	​

ln(S/K)+(r+0.5σ
2
)T
	​

𝑑
2
=
𝑑
1
−
𝜎
𝑇
d
2
	​

=d
1
	​

−σ
T
	​

🎯 Monte Carlo price simulation
𝑆
𝑇
=
𝑆
0
exp
⁡
(
(
𝑟
−
0.5
𝜎
2
)
𝑇
+
𝜎
𝑇
𝑍
)
S
T
	​

=S
0
	​

exp((r−0.5σ
2
)T+σ
T
	​

Z)

Payoff:

Call: 
max
⁡
(
𝑆
𝑇
−
𝐾
,
0
)
max(S
T
	​

−K,0)

Put: 
max
⁡
(
𝐾
−
𝑆
𝑇
,
0
)
max(K−S
T
	​

,0)

Price:

𝑃
𝑟
𝑖
𝑐
𝑒
=
𝑒
−
𝑟
𝑇
⋅
𝐸
[
𝑃
𝑎
𝑦
𝑜
𝑓
𝑓
]
Price=e
−rT
⋅E[Payoff]
📊 Architecture Overview
 USER INPUTS
      ↓
BLACK–SCHOLES MODEL → Greeks → Implied Volatility
      ↓
Monte Carlo Simulation
      ↓
 FINAL OUTPUT TABLE

🌟 Why This Project Stands Out

✔ Demonstrates real quantitative finance knowledge
✔ Includes both analytical & numerical methods
✔ Production-level modular design
✔ Excellent CV / GitHub portfolio project
✔ Shows strong Python and math skills

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

📜 License

MIT License

💼 Author

Your Name
📧 your.email@example.com

🔗 LinkedIn: https://linkedin.com/in/yourprofile

🐙 GitHub: https://github.com/yourusername