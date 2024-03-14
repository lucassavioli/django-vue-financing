import decimal


def sac(loan, installments_number, interest):
    sac_table = []
    amortization = loan / installments_number
    for i in range(installments_number):
        interest_next = loan * interest
        installment = amortization + interest_next
        balance_due = loan - amortization
        sac_table.append(
            {
                "installments_number": i + 1,
                "installment": installment,
                "interest": interest_next,
                "amortization": amortization,
                "balance_due": balance_due,
            }
        )
        loan = balance_due

    return sac_table


def price(loan, installments_number, interest):
    price_table = []
    decimal_places = 2
    installment = loan * (
        interest
        * pow(1 + interest, installments_number)
        / (pow(1 + interest, installments_number) - 1)
    )
    for i in range(installments_number):
        interest_next = loan * interest
        amortization = installment - interest_next
        balance_due = loan - amortization
        price_table.append(
            {
                "installments_number": i + 1,
                "installment": round(installment, decimal_places),
                "interest": round(interest_next, decimal_places),
                "amortization": round(amortization, decimal_places),
                "balance_due": round(balance_due, decimal_places),
            }
        )

        loan = balance_due

    return price_table
