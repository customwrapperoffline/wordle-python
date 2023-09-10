import random
import nltk
from nltk.corpus import words
from colorama import init, Fore

init(autoreset=True)
nltk.download('words')

def choose_word(min_length, max_length):
    word_list = [word for word in words.words() if min_length <= len(word) <= max_length]
    return random.choice(word_list)

def check_guess(word, guess):
    result = []
    for i in range(len(word)):
        if guess[i] == word[i]:
            result.append(guess[i])
        elif guess[i] in word:
            result.append("*")
        else:
            result.append("-")
    return result

def main():
    print("Welcome to Wordle!")

    min_word_length = 5
    max_word_length = 10

    target_word = choose_word(min_word_length, max_word_length)
    word_length = len(target_word)
    max_attempts = word_length + 2

    print(f"You have {max_attempts} attempts to guess a {word_length}-letter word.")

    attempts = 0

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: ").lower()

        if len(guess) != word_length:
            print(Fore.RED + f"Your guess must be {word_length} letters long.")
            continue

        result = check_guess(target_word, guess)
        colored_result = [Fore.GREEN + char if char == '*' else Fore.YELLOW + char for char in result]
        print(" ".join(colored_result))

        if result == list(target_word):
            print(Fore.GREEN + f"Congratulations! You guessed the word: {target_word}")
            break

        attempts += 1

    if attempts == max_attempts:
        print(Fore.RED + f"Sorry, you're out of attempts. The word was: {target_word}")

if __name__ == "__main__":
    main()
