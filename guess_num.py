import random

l = random.sample(range(10), 4)
n=int((''.join([str(x) for x in l])))
num=str(n)

chance = 1

while chance <= 5:
    print(f"Chance {chance}")
    guess=str(input("Enter guess:"))

    if guess==num:
        print("you guessed it right!")
        break
        
    else:
        for i in range(len(guess)):
            if guess[i] in num:
                print(f"{guess[i]} is present in pos {num.index(guess[i])}")
            else:
                print(f"{guess[i]} is not present")
        chance = chance + 1

if chance==5:
    print("5 chances are done. GAME OVER!!")


