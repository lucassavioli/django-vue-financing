def sac(loan, installments_number, interest):
    sac_table = []
    amortization = loan / installments_number
    for i in range(installments_number):
        interest_next = loan * interest
        installment = amortization + interest_next
        balance_due = loan - amortization
        sac_table.append(
            {
                "installmentNumber": i + 1,
                "installment": installment,
                "interest": interest_next,
                "amortization": amortization,
                "balanceDue": balance_due,
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
        interest_next = round(loan * interest, decimal_places)
        amortization = round(installment - interest_next, decimal_places)
        balance_due = round(loan - amortization, decimal_places)
        price_table.append(
            {
                "installmentNumber": i + 1,
                "installment": round(installment, decimal_places),
                "interest": interest_next,
                "amortization": amortization,
                "balanceDue": balance_due,
            }
        )
        # update values
        loan = balance_due

    return price_table
