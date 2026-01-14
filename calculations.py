from debt_data import debt_portfolio, total_principal

def weighted_average_rate(debt_portfolio):
    ttl_principal = 0
    weighted_sum = 0

    for debt in debt_portfolio:
        ttl_principal += debt["Principal"]
        weighted_sum += debt["Principal"] * debt["Interest_Rate"]

    return weighted_sum / ttl_principal

