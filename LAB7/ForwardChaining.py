def forward_chaining(facts, rules, goal):
    facts = set(facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            if set(conditions).issubset(facts):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Inferred:", conclusion)
                    new_fact_added = True

        if goal in facts:
            print("Goal achieved:", goal)
            return True

        if not new_fact_added:
            break

    print("Goal cannot be proved:", goal)
    return False


# Initial facts
facts = ["A", "B"]

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

goal = "E"

print("Initial facts:", facts)
forward_chaining(facts, rules, goal)