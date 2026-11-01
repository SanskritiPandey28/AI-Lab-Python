def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    # If the goal is already a known fact
    if goal in facts:
        print("Fact found:", goal)
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that conclude the goal
    for conditions, conclusion in rules:
        if conclusion == goal:
            print("Trying to prove:", goal)

            # Every condition must be proved
            if all(
                backward_chaining(condition, facts, rules, visited.copy())
                for condition in conditions
            ):
                print("Proved:", goal)
                return True

    print("Cannot prove:", goal)
    return False


# Known facts
facts = {"A", "B"}

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

goal = "E"

print("Goal:", goal)

if backward_chaining(goal, facts, rules):
    print("Goal successfully proved.")
else:
    print("Goal could not be proved.")