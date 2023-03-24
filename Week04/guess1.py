# guess1.py
# Taken from Lab4.2 step 2. Testing how the while loop works. Need to see the terminal running to understand the steps that the while loop goes through. 

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess)