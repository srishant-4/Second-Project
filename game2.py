import random
n=random.randint(1,100)
a=-1
Guesses=0
while(a!=n):
    Guesses +=1
    a=int(input("Guess the number:"))
    
    if(a>n):
        print(" Lower Number please")
    else:
        print("Higher number please")

print(f"You have correctly guessed  the number {n} in {Guesses} guesses")

    