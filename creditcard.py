# used this for reajx ^(?!.*(\d)\1{3})([456]\d{3}-\d{4}-\d{4}-\d{4}|[456]\d{15})$

#code

import re

def validate_credit_card(cards):
    pattern = re.compile(r"^(?!.*(\d)\1{3})([456]\d{3}-\d{4}-\d{4}-\d{4}|[456]\d{15})$")
    results = []
    for card in cards:
        card = card.replace(" ", "")
        if pattern.match(card):
            results.append("Valid")
        else:
            results.append("Invalid")
    return results

# Sample Input
input_data = [
    "4123456789123456",
    "5123-4567-8912-3456",
    "61234-567-8912-3456",
    "4123356789123456",
    "5133-3367-8912-3456",
    "5123 - 3567 - 8912 - 3456"
]

# Run validation
output = validate_credit_card(input_data)

# Print results
for result in output:
    print(result)
