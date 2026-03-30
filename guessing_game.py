import random
num=random.randint(1,100)
print(num)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses = [0]
while True:
    guess_number=int(input("Please enter a number between 1 to 100"))
    if (guess_number<1 or guess_number>100):
        print("Input number out of range, Try again!")
        continue #this will break the current iteration and start from start

    if guess_number == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    guesses.append(guess_number)
     
    # when testing the first guess_number, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guesses[-2]: 
        if abs(num-guess_number) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess_number) <= 10:
            print('WARM!')
        else:
            print('COLD!')