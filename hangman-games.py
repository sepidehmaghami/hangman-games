import random
word_bank = ["apple", "banana", "cherry", "date",
             "elderberry", "fig", "grape", "honeydew"]
x = random.randint(0, len(word_bank)-1)
word = word_bank[x]

user_mistakes = 0
good_chars = []
bad_chars = []

while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
        else:
            print("_", end=" ")
    if len(good_chars) == len(set(word)):
        break
    user_char = input("\nplease enter a character: ")
    user_char = user_char.lower()
    if len(user_char) == 1:
        if user_char in word:
            print("✅")
            good_chars.append(user_char)
        else:
            print("❌", end=" ")
            user_mistakes += 1
            bad_chars.append(user_char)
            print("bad chars: ", bad_chars)
    else:
        print("please enter only one character")
        
if user_mistakes == 6:
    print("you lost")
    print("the word was: ", word)
else:
    print("\nyou won")