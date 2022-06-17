from random import Random

min = 1
max = 100
input = int(input())

n = 0
guessedTime = 0
isRunning = True
badCase = []
goodCase = []

for i in range(input):
    print(i)
    _min = min
    _max = max
    number = Random().randint(min, max)
    while(isRunning):
        n = int((_max+_min)//2)
        guessedTime += 1
        if guessedTime >= max:
            print(f"Min: {_min}, Max: {_max}, N: {n, (_max+_min)//2, int((_max+_min)/2)}, Number: {number}")
            n = number
            badCase.append(guessedTime)
            isRunning = False
            break
        if n > number:
            _max = int(n)
        elif n < number:
            _min = int(n)
        elif n == number:
            isRunning = False
            goodCase.append(guessedTime)
    isRunning = True
    guessedTime = 0

isRunning = False
goodCase.sort
indexGoodCase = set(goodCase)

print(f"Bad Case: {(len(badCase)/input)*100}% / {len(badCase)}")
print(f"Good Case: {(len(goodCase)/input)*100}% / {len(goodCase)}")

print("----- Good Case Detail -----")
for i in indexGoodCase:
    case = goodCase.count(i)
    percent = (case/len(goodCase))*100
    print(f"Case: {i} - {percent}%")

#* Pseudocode Binary Search
# Step 1: Min = 0, Max = 100
# Step 2: If guessed = (0+100)//2 integer
# Step 3: If n < guessed -> Max = guessed -> go back step 2
# Step 3a: If n > guessed -> Min = guessed -> go back step 2
# Step 3b: If n == guessed -> n have found -> Finish