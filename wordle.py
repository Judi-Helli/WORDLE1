import sys

#Util Functions:

#This function converts the tries counter to the formal ordering form, i.e. 1st, 2nd, 3rd, 4th,..
#Depending on the counter tries we read the suitable index from the ranks list.

def whichTry(counter):
    ranksList = ["1st", "2nd", "3rd"]
    if counter > 2:
        return str(counter + 1) + "th"
    return ranksList[counter]

#This function compares the inputWord and wod letter by letter, using a loop and the index of each word.
def compareLetters(inputWord, wod):
    for i in range(len(inputWord)):
        if inputWord[i] == wod[i]:
            print(str(i + 1) + ". letter exists and located in right position")
        elif inputWord[i] in wod:
            print(str(i + 1) + ". letter exists but located in wrong position")
        else:
            print(str(i + 1) + ". letter does not exist.")


#Main Function:
def main():
    wod = sys.argv[1].upper()

    #If the length of wod is not satisfied,the program will terminate directly.
    if len(wod) != 5:
        print("The length of WoD must be five!")
        return

    #The game is here.
    counter = 0
    maxTries = 6
    is_won = False
    while counter < maxTries:
        thisTry = whichTry(counter)
        inputWord = input("Enter your " + thisTry + " try:").upper()

        if len(inputWord) != 5:
            print("Try" + str(counter + 1) + " (" + inputWord + "): The length of word must be five!")

        elif inputWord == wod:
            is_won = True
            print("Try" + str(counter + 1) + " (" + inputWord + "): Congratulations! You guess right in " + thisTry +
                  " shot!")
            break

        else:
            print("Try" + str(counter + 1) + " (" + inputWord + "):")
            compareLetters(inputWord, wod)

        counter += 1

    if not is_won:
        print("You are failed!")

main()
