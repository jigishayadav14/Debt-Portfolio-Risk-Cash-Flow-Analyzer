from debt_data import debt_portfolio, total_principal


def high_interest_risk(war):
    if war > 0.08:
        return "High interest cost risk"
    return None

def short_term_maturity(bucket_1):
    if bucket_1 > 40:
        return "Refinancing Risk"
    return None

def floating_rate_exposure(debt_portfolio):
    if debt_portfolio["Rate_Type"] == "Floating":
        return "Interest rate volatility risk"
    return None