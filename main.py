import random
from hangman_art import logo, stages
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_game = False
lives = 6

print(logo + "\n\n")

display = []
for i in chosen_word:
  display.append('_')
print(f"This is a {len(chosen_word)} letter word.\n{display}\n\n")

while not end_game:
  guess = input("Guess a letter: ").lower()

  for i in range(len(chosen_word)):
      if guess == chosen_word[i]:
        display[i] = guess

  if guess not in chosen_word:
    print(f"You guessed {guess} and that is not present in the word.\n") 
    lives -= 1
    if lives == 0:
      end_game = True
      print("You lose")

  if '_' not in display:
    end_game = True
    print("You win!")

  print(display)
  print(stages[lives] + "\n")