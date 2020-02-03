from random import randint
from .validate import optValidate
from .validate import numTypeValidate

def doAbilityScores():
    allResults = []
    for i in range(6):
        results = []
        total = 0
        for i in range(4):
            results.append(randint(1,6))
        lowest = 6
        lowestPos = 0
        for i in range(4):
            if results[i] < lowest:
                lowest = results[i]
                lowestPos = i
        results.remove(results[lowestPos])
        for i in range(len(results)):
            total += results[i]
        allResults.append(total)
    total = 0
    for i in range(len(allResults)):
        total += allResults[i]
    print("\nArray:", allResults)
    print("Total:", total)
    print("\nBased on the results of 10000 arrays, the average total is about 73.")
    if total >= 73:
        print("Since your total equals or exceeds this, you're fine. Have fun playing D&D.\n")
    elif total < 73 and total > 65:
        print("Since your total is only slightly less than this, it's probably still fine to keep the array.\nAbility Scores don't define everything, but if you really want to have good ones, ask your DM is you are allowed to reroll.\n")
    else:
        print("Since your total is quite a lot less than this, you may want to ask your DM if you can reroll.\n")
    return True

def freeRoll():
    results = []
    total = 0
    options = [4, 6, 8, 10, 12, 20, 100]
    diceType = int(optValidate("\nWhat type of dice should I roll? [4, 6, 8, 10, 12, 20, 100]: "),options)
    noRoll = numTypeValidate(input("How many should I roll?: "),"a number: ",True)
    for i in range(int(noRoll)):
        results.append(randint(1,diceType))
        total += results[i]
    print("\nIndividual Results:", results)
    print("Total:", total, "\n")
    return True
