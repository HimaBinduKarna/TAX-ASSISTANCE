# AI Tax Assistant - Python

# Rupee Symbol
RUPEE_SYMBOL = "₹"

# To display the rupee symbol properly in VS Code, ensure your file encoding is set to UTF-8.
def calculate_tax(income):
    TAX_SLABS = [
        (250000, 0.05),   # 5% for income above 2.5L
        (500000, 0.10),   # 10% for income above 5L
        (1000000, 0.20),  # 20% for income above 10L
        (1500000, 0.30)   # 30% for income above 15L
    ]
    
    tax = 0
    previous_limit = 0

    for limit, rate in TAX_SLABS:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return round(tax, 2)

if __name__ == "__main__":
    income = int(input("Enter your annual income: "))
    tax = calculate_tax(income)
    print(f"Your calculated tax is: {RUPEE_SYMBOL}{tax}")