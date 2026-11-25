import re

def check_production(production):
    production = production.strip()

    # Check whether the production contains ->
    if "->" not in production:
        return False, ["Missing arrow (->)"]

    parts = production.split("->")

    if len(parts) != 2:
        return False, ["Invalid production format"]

    lhs = parts[0].strip()
    rhs = parts[1].strip()

    # Left-hand side must be one uppercase letter
    if not re.fullmatch(r"[A-Z]", lhs):
        return False, ["Invalid non-terminal on left-hand side"]

    if not rhs:
        return False, ["Empty right-hand side"]

    # Separate alternatives using |
    alternatives = rhs.split("|")
    invalid = []

    for alternative in alternatives:
        alternative = alternative.strip()

        # Valid forms: aB or a
        if not re.fullmatch(r"[a-z][A-Z]?", alternative):
            invalid.append(alternative)

    return len(invalid) == 0, invalid


def main():
    print("RIGHT-LINEAR GRAMMAR PRODUCTION CHECKER")
    print("---------------------------------------")
    print("Enter one production per line.")
    print("Example: S -> aA | b")
    print("Press ENTER on an empty line to finish.\n")

    productions = []

    while True:
        line = input("Enter production: ").strip()

        if line == "":
            break

        productions.append(line)

    if not productions:
        print("\nNo productions entered.")
        return

    print("\n----------- RESULT -----------")

    offending = []

    for i, production in enumerate(productions, start=1):
        valid, invalid_parts = check_production(production)

        if valid:
            print(str(i) + ". " + production + " : VALID")
        else:
            print(str(i) + ". " + production + " : INVALID")
            print("   Invalid part(s): " + ", ".join(invalid_parts))
            offending.append(production)

    print("\n----------- OFFENDING PRODUCTIONS -----------")

    if offending:
        for production in offending:
            print("- " + production)

        print("\nConclusion: The grammar is NOT right-linear.")
    else:
        print("No offending productions found.")
        print("\nConclusion: All productions are right-linear.")


if __name__ == "__main__":
    main()