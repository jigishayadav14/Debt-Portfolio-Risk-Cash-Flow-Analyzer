from debt_data import debt_portfolio, total_principal
from calculations import weighted_average_rate
from risk_analysis import high_interest_risk, short_term_maturity, floating_rate_exposure


#PORTFOLIO SUMMARY
print("DEBT PORTFOLIO SUMMARY \n---------------------")
print(f"Total Debt Instruments: {len(debt_portfolio)}")
print(f"Total Principal: {total_principal:,}")

#CASH FLOW ANALYSIS
print("CASH FLOW ANALYSIS \n---------------------")
for i, debt in enumerate(debt_portfolio, 1):
    annual_interest = debt["Principal"] * debt["Interest_Rate"]
    total_repayment = debt["Principal"] + (annual_interest * debt["Tenure"])
    print(f"Debt {i}: \nIssuer: {debt['Issuer_Category']}")
    print(f"  Annual Interest: {annual_interest:,}")
    print(f"  Total Repayment: {total_repayment:,}")

#PORTFOLIO METRICS
print("PORTFOLIO METRICS \n ---------------------")
war = weighted_average_rate(debt_portfolio)
print(f"Weighted Average Interest Rate: {war:.1%}")

#MATURITY DISTRIBUTION
print("MATURITY DISTRIBUTION \n---------------------")
bucket_1 = (debt_portfolio[0]["Principal"] / total_principal) * 100
print(f"Short Term: {bucket_1}%")

bucket_2 = (debt_portfolio[1]["Principal"] / total_principal) * 100
print(f"Medium Term: {bucket_2}%")

bucket_3 = (debt_portfolio[2]["Principal"] / total_principal) * 100
print(f"Long Term: {bucket_3}%")

#RISK FLAGS
print("RISK FLAGS \n---------")
risk_flags = []

# High Interest
high_interest = high_interest_risk(war)
if high_interest:
    risk_flags.append(high_interest)

# Short-term maturity
short_term_risk = short_term_maturity(bucket_1)
if short_term_risk:
    risk_flags.append(short_term_risk)

# Floating rate exposure
for debt in debt_portfolio:
    floating_risk = floating_rate_exposure(debt)
    if floating_risk and floating_risk not in risk_flags:
        risk_flags.append(floating_risk)

if risk_flags:
    for r in risk_flags:
        print(r)
else:
    print("No major risks detected")
