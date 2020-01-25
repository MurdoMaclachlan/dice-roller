import libdr

def mainMenu():
    options = [libdr.freeRoll, libdr.doAbilityScores]
    x = True
    yArray = ["1", "2"]
    while x == True:
        y = 0
        while y not in yArray:
            y = str(input("Do you want to do free roll, or generate ability scores? [1/2]: "))
            if y not in yArray:
                print("\nPlease enter either 1 or 2.\n")
        x = options[int(y)-1]()

mainMenu()
