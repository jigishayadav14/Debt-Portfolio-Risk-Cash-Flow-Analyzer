
debt_portfolio = [
    {"id": 1,
     "Principal": 1000000,
     "Interest_Rate": 0.07,
     "Tenure": 5,
     "Rate_Type": "Fixed",
     "Issuer_Category": "State"
},
    {"id": 2,
     "Principal": 1500000,
     "Interest_Rate": 0.08,
     "Tenure": 3,
     "Rate_Type": "Floating",
     "Issuer_Category": "Corporate"
},
    {"id": 3,
     "Principal": 2500000,
     "Interest_Rate": 0.09,
     "Tenure": 10,
     "Rate_Type": "Fixed",
     "Issuer_Category": "Municipal"
}
]
total_principal = debt_portfolio[0]["Principal"] + debt_portfolio[1]["Principal"] + debt_portfolio[2]["Principal"]
