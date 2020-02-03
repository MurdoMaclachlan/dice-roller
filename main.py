import libdr

def mainMenu():
    options = [libdr.freeRoll, libdr.doAbilityScores]
    x = True
    optNums = ["1", "2"]
    while x == True:
        y = libdr.optValidate("Do you want to do free roll, or generate ability sores? [1, 2]: ",optNums)
        print("")
        x = options[int(y)-1]()

mainMenu()
