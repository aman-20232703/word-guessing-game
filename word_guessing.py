import random

print("-----------------------------------")
print("🤔WELCOME THE GUSSING WORD GAME🤔")
print("-----------------------------------")

# Word lists for different difficulty levels
easy=["lion","man","copy","boy","dog","cat","pen","name","game"]
medium=["bottle","body","code","living","money","baby","body","secret","eraser"]
hard=["picnic","mobile","pencil","holiday","college","network","healthy","freely","always","strong"]

print("choose a dificulty level🤨:  easy , medium, hard: ")

# Get user input for difficulty level
level = input("enter difficulty👉: ".lower())

# Select a secret word based on difficulty
if level == 'easy':
    mywords=easy# Secret word
elif level== 'medium':
    mywords=medium# Secret word
elif level=='hard':
    mywords=hard# Secret word
else:
    print("invalid choice❗, default to easy")
    code=random.choice(easy)# Secret word
    
code=random.choice(mywords)
attempts=0
max_attempts=4
code_len=len(code)
print("guess the secret code⚡ ")

# Allow the user to guess up to 4 times
while attempts<max_attempts:
    guess=input("enter your guess🔒: ").lower()
    attempts+=1

    if len(guess)!=len(code):
        print(f"⚠️ Your guess must be {len(code)} letters long.")
        continue

    if guess==code:
        print(f"🥇congratulations! you are guessing in {attempts} attempts")
        break
    
# Generate a hint based on matching letters
    hint=" "
    for i in range (len(code)):
        if guess[i]==code[i]:
            hint+=guess[i]
        else:
            hint += "_"
            
    print("hint🙋‍♂️: ",hint)
else:
    
# If all attempts used up
    print("😞you are using your all attempts 😞")
    print("try to choose from the given options👁️:-\n")
    
# Create list of same-length words (excluding correct one)
    len_words=[ ]
    for word in mywords:
        if len(word)==code_len and word!=code:
            len_words.append(word)
            
# Prepare options list (3 random + 1 correct)
    options = random.sample(len_words, min(3, len(len_words))) + [code]
    random.shuffle(options)
    
# Show options
    for idx,word in enumerate(options, start=1):
        print(f"{idx}.{word}")
        
    try:
        choice=int(input("enter your option👉: "))
    except ValueError:
        print("invalid choice❗! plz select in numeric digits(1,2,3,4)")
    
# Check selected choice
    if 1<=choice <=len(options):
        if options[choice-1]==code:
            print("✅correct options")
        else:
            print(f"❌wrong option.🔰correct word is {word}")
    else:
        print(f"❗invalid input. the correct word {word}")
        
print("⚜️ game over ⚜️")
    
