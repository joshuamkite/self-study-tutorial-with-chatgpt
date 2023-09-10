import sys

emoji_outcomes = {
    "✂📄": "cuts",
    "💎🦎": "crushes",
    "🖖✂": "smashes",
    "🦎📄": "eats",
    "🖖💎": "vaporizes",
    "✂✂": "tie",
    "💎💎": "tie",
    "📄📄": "tie",
    "🖖🖖": "tie",
    "🦎🦎": "tie",
    "📄💎": "covers",
    "💎✂": "crushes",
    "📄🖖": "disproves",
    "🦎🖖": "poisons",
    "✂🦎":  "decapitates"
}


# Accessing arguments
for arg in sys.argv[1:]:
    outcome = emoji_outcomes.get(arg)
    reverse = False
    if outcome is None:
        outcome = emoji_outcomes.get((arg[1]+arg[0]))
        reverse = True
    if outcome == "tie":
        print("Tie")
    else:
        if reverse == False:
            print(arg[0], outcome, arg[1])
        else:
            print(arg[1], outcome, arg[0])
