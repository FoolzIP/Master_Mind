from random import randint
def welcome():
    print("Hello and welcome to MasterMind with Python!!")
    print("In this game, I pick four integers [1..6] in a certain order,")
    print("and ask you to guess what they are -- in that same order!!")
    print("you may guess up to ten (10) times.")
    print("(note: I may also pick the same integer multiple times!!)")
    print("I will score your guess with either a black[b] or white[w] stone")
    print("  - [b] black means you guessed the right number in the right spot!")
    print("  - [w] white means you guessed the right number in the wrong spot.")
    print("If you correctly guess my pattern before the eleventh(11th) guess, you win!")
    print("Else, You lose and are none the wiser.")
    print("\n")
    x = input("Would you like to play??  [y/n] ")
    if x == 'y' or x == "Y":
        return "y"
    else:
        return "n"
    
def getPat():
    Pat = []
    for i in range(4):
        Pat.append(randint(1,6))
    return Pat    
    
def scorePat(guess, myPat, fatPat):
    try:
        guess = [int(i) for i in guess.split()]
    except ValueError:
        bltprf = "Invalid"
        return bltprf
    myPat = []
   # myPat = fatPat
    myPat2 = ""
    for item in fatPat:
        myPat2 += (str(item) + " ")
    for word in myPat2.split():
        myPat.append(int(word))
    b=0
    w=0
    try:
        for i in range(4):
            if guess[i] == myPat[i]:
               # myPat = fatPat
                b +=1
                guess[i] = "h"
                myPat[i] = "k"
        for g in range(4):
            for m in range(4):
                if guess[g] == myPat[m] and g != m:
                   # myPat = fatPat
                    w += 1
                    guess[g] = "h"
                    myPat[m] = "k" 
        score = b * "b" + w * "w"
        if score == "":
            score = "0"
        return score
    except IndexError:
        bltprf = "Invalid"
        return bltprf
def genPat():
    Pat = []
    for i in range(4):
        Pat.append(randint(1,6))
    return Pat  

def main():
    ans = welcome()
    blnWon = False
    if ans == 'y':
        myPat = genPat()
        fatPat = myPat[:]
        fatPat2 = ""
        for item in myPat:
            fatPat2 += (str(item) + " ")
       # for word in fatPat2.split():
        #    fatPat.append(int(word))
        for i in range(1,11):
            guess = input("Enter four(4) numbers[1-6] seperated by spaces and press Enter: ")
            if (guess == fatPat2):
                blnWon = True
                break
            elif len(guess) <= 8:
                print("Your score is " + scorePat(guess, myPat, fatPat) + " Try Again!")
            elif len(guess) > 8:
               print("You just waisted a turn!")
            else:
                break
        if blnWon:
            print("You Won!! The pattern was: ", fatPat)
        else:
            print("After 10 tries...")
            print("You Lost!! Don't beat yourself up too bad.")
    else:
        print("Goodbye")
        

main()            
    
