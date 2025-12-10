class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {other_category.name}")
            other_category.deposit(amount, description=f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}"[:7].rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculate total spent
    spends = []
    total_spent = 0
    for cat in categories:
        spend = 0
        for item in cat.ledger:
            if item["amount"] < 0:   # only withdrawals
                spend += -item["amount"]
        spends.append(spend)
        total_spent += spend

    # Percentages rounded down to nearest 10
    percents = [(spend / total_spent * 100) // 10 * 10 for spend in spends]

    # Build percentage rows
    output = title
    for level in range(100, -1, -10):
            #print level in row
        row = f"{level:>3}|"
                #use ':>3' to create indentation
        for p in percents:
            row += " o " if p >= level else "   "
        output += row + " \n"

    # Bottom line
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category name vertical labels
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     "
        for cat in categories:
            char = cat.name[i] if i < len(cat.name) else " "
            row += char + "  "
        if i < max_len - 1:
            row += "\n"
        output += row

    return output


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
print(food)

auto = Category("Auto")

print(create_spend_chart([food, clothing, auto]))

