import random

l = random.sample(range(10), 4)
n=int((''.join([str(x) for x in l])))
num=str(n)

chance = 0

while chance < 5:
    pos=0
    print(f"Chance {chance+1}")
    guess=str(input("Enter guess:"))

    if guess==num:
        result = 1
        break
        
    else:
        for i in range(len(guess)):

            if guess[i] in num:
                print(f"{guess[i]} is present")
                if num.index(guess[i])==guess.index(guess[i]):
                    pos=pos+1

            else:
                print(f"{guess[i]} is not present")
        print(f"Position of {pos} are correct")

        result = 0
        chance = chance + 1
     
if chance==5 and result==0:
    print(f"5 chances are done. GAME OVER!! \nThe secret number is {num}")
elif result==1:
    print(f"You're correct!! The number is {num}")


