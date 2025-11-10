facts = {
    ("Eats", "Anil", "peanuts"),
    ("Alive", "Anil"), 
}

rules = [
    
    {
        "head": ("Food", "?Y"),
        "body": [("Eats", "?X", "?Y"), ("Alive", "?X")]
    },
    
    {
        "head": ("Eats", "Harry", "?Y"),
        "body": [("Eats", "Anil", "?Y")]
    },
   
    {
        "head": ("Likes", "John", "?Y"),
        "body": [("Eats", "Harry", "?Y")]
    },
   
    {
        "head": ("Likes", "?X", "?Y"),
        "body": [("Eats", "?X", "?Y"), ("Food", "?Y")]
    },
]

def unify(goal, fact):
  
    if goal[0] != fact[0] or len(goal) != len(fact):
        return None
    bindings = {}
    for g, f in zip(goal[1:], fact[1:]):
        if g.startswith("?"):
            bindings[g] = f
        elif g != f:
            return None
    return bindings

def substitute(predicate, bindings):
    
    return tuple(bindings.get(arg, arg) for arg in predicate)

def backward_chain(goal, depth=0):
    indent = "  " * depth
    print(f"{indent}Trying to prove {goal}")

  
    if goal in facts:
        print(f"{indent} Found in facts.")
        return True

   
    for rule in rules:
        bindings = unify(rule["head"], goal)
        if bindings is not None:
            print(f"{indent}Using rule: {rule['head']} ← {rule['body']}")
          
            if all(backward_chain(substitute(cond, bindings), depth + 1) for cond in rule["body"]):
                facts.add(goal)  
                print(f"{indent} Proved {goal}")
                return True

    print(f"{indent} Cannot prove {goal}")
    return False


goal = ("Likes", "John", "peanuts")

print("BACKWARD CHAINING TRACE")
result = backward_chain(goal)
print("\nResult:", "Proved" if result else " Could not prove")
