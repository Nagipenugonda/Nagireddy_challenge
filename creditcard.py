# used this for reajx ^(?!.*(\d)\1{3})([456]\d{3}-\d{4}-\d{4}-\d{4}|[456]\d{15})$

#code

import re

def is_valid_credit_card(card):
    # Regex pattern to match the valid credit card rules
    pattern = r'^[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})$'
    # Check if the card matches the pattern
    if not re.match(pattern, card):
        return "Invalid"
    
    # Remove all hyphens for further checking
    card = card.replace('-', '')
    
    # Check for four or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card):
        return "Invalid"
    
    return "Valid"

# Read input
n = int(input())
credit_cards = [input().strip() for _ in range(n)]

# Validate each credit card
results = [is_valid_credit_card(card) for card in credit_cards]

# Print the results
for result in results:
    print(result)
