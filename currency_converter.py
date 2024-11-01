conversion_rate = {
'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
}

def currency_converter(amount, from_converter, away_converter):
    if amount>0:
        if from_converter in conversion_rate and away_converter in conversion_rate[from_converter]:
            conversion_rate_value = conversion_rate[from_converter][away_converter]
            converted_amount = amount * conversion_rate_value
            return converted_amount
        else:
            return "Conversion rate not available for this currency pair."
    else:
        return "Amount should be greater than 0."
         



banksum= int(input("How much would you like to convert?: "))
home= int(input("Are you converting from:\n 1. GBP\n 2. CNY\n 3.PHP\n 4. INR\n"))
away= int(input("Are you converting to:\n 1. GBP\n 2. CNY\n 3.PHP\n 4. INR\n"))

match home:
    case 1:
        home= "GBP"
    case 2:
        home= "CNY"
    case 3:
        home = "PHP"
    case 4:
        home = "INR"

match away:
    case 1:
        away= "GBP"
    case 2:
        away= "CNY"
    case 3:
        away = "PHP"
    case 4:
        away = "INR"

print(currency_converter(banksum, home, away))



