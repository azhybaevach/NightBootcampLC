def atm_withdraw(amount):
    denominations = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
    result = {}
    for denom in denominations:
        if amount >= denom:
            count, amount = divmod(amount, denom)
            result[denom] = count
    return result

# Пример использования
withdraw_amount = 12345
result = atm_withdraw(withdraw_amount)
print(result)