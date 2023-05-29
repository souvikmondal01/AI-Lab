import random

word_list = ["python", "java", "ruby", "javascript", "Php", "csharp", "html", "css"]
word = random.choice(word_list)
guessed_letters = []
remaining_attempts = max_attempts = 6
print("Welcome to Hangman! Guess the word:")
word_representation = ["_"] * len(word)
print(" ".join(word_representation))
while remaining_attempts > 0 and "_" in word_representation:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1:
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    elif not guess.isalpha():
        print("Please enter a letter.")
    else:
        guessed_letters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_representation[i] = guess

            print(" ".join(word_representation))
            print("Correct!")
        else:
            remaining_attempts -= 1
            print(" ".join(word_representation))
            print("Incorrect. You have", remaining_attempts, "attempts remaining.")

if "_" not in word_representation:
    print("Congratulations! You guessed the word.")
else:
    print("Sorry, you ran out of attempts. The word was", word + ".")
