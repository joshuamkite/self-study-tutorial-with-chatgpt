from english_words import get_english_words_set

# Replace the arguments inside the function call with the appropriate word list identifier and flags
english_words_set = get_english_words_set(['web2'], lower=True)


# Define the minion_game function


def minion_game(word):
    vowels = "aeiou"
    stuart_score = 0
    kevin_score = 0

    n = len(word)
    for i in range(n):
        if word[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)

    if stuart_score > kevin_score:
        return "Stuart"
    elif kevin_score > stuart_score:
        return "Kevin"
    else:
        return "Draw"


# Initialize counters for the results
stuart_wins = 0
kevin_wins = 0
draws = 0

# Iterate through the list of words and simulate the game
for word in english_words_set:
    winner = minion_game(word)
    if winner == "Stuart":
        stuart_wins += 1
    elif winner == "Kevin":
        kevin_wins += 1
    else:
        draws += 1

# Calculate and print the statistical results
total_games = len(english_words_set)
print(f"Total Games: {total_games}")
print(f"Stuart Wins: {stuart_wins} ({(stuart_wins / total_games) * 100:.2f}%)")
print(f"Kevin Wins: {kevin_wins} ({(kevin_wins / total_games) * 100:.2f}%)")
print(f"Draws: {draws} ({(draws / total_games) * 100:.2f}%)")
