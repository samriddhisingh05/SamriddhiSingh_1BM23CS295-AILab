facts = {
    'American(Robert)': True,  # Robert is an American
    'Hostile(A)': True,        # Country A is hostile to America
    'Sells_Weapons(Robert, A)': True  # Robert sold weapons to Country A
}

# Define the law/rule: If American(X) and Hostile(Y) and Sells_Weapons(X, Y), then Crime(X)
def forward_reasoning(facts):
    # Apply the rule: If American(X) and Hostile(Y) and Sells_Weapons(X, Y), then Crime(X)
    if facts.get('American(Robert)', False) and facts.get('Hostile(A)', False) and facts.get('Sells_Weapons(Robert, A)', False):
        facts['Crime(Robert)'] = True  # Robert is a criminal

# Perform forward reasoning to see if we can deduce that Robert is a criminal
forward_reasoning(facts)

# Output the result based on the fact derived
if facts.get('Crime(Robert)', False):
    print("Robert is a criminal.")
    print("Samriddhi Singh 1BM23CS295")
else:
    print("Robert is not a criminal.")
