import math
import pandas as pd

def main(cupOneSize, cupTwoSize):
    if cupOneSize == cupTwoSize:
        raise Exception('Cups need to be different sizes.')
    
    largerCup = cupOneSize
    smallerCup = cupTwoSize
    if largerCup < smallerCup:
        largerCup = cupTwoSize
        smallerCup = cupOneSize
    
    if largerCup % smallerCup == 0:
        raise Exception('Cups need to be relatively primes.')
    
    
    validStates = []
    
    for x in range(smallerCup + 1):
        for y in range(largerCup + 1):
            validStates.append((x, y))
    
    df = pd.DataFrame(columns=validStates, index=validStates)
    
    for dest in validStates:
        for source in validStates:
            if (source == dest):
                df.at[source, dest] = 0

        
    possibleMoves = {}
    
    for move in validStates:
        emptySmall = (0, move[1])
        emptyLarger = (move[0], 0)
        fillSmall = (smallerCup, move[1])
        fillLarge = (move[0], largerCup)
        
        sumOfCups = move[0] + move[1]
        transferSmall = (max(sumOfCups - largerCup, 0), min(sumOfCups, largerCup))
        transferLarge = (min(sumOfCups, smallerCup), max(sumOfCups - smallerCup, 0))
        
        addToDict(possibleMoves, emptySmall, move) 
        addToDict(possibleMoves, emptyLarger, move) 
        addToDict(possibleMoves, fillSmall, move) 
        addToDict(possibleMoves, fillLarge, move) 
        addToDict(possibleMoves, transferSmall, move) 
        addToDict(possibleMoves, transferLarge, move) 
    
    for dest in possibleMoves.keys():
        for source in possibleMoves[dest]:
            if math.isnan(df.at[source, dest]):
                df.at[source, dest] = 1


    for i in range(2, 10):
        oldPossibleMoves = possibleMoves
        possibleMoves = {}
        validStates = oldPossibleMoves.keys()
        
        for move in validStates:
            emptySmall = (0, move[1])
            emptyLarger = (move[0], 0)
            fillSmall = (smallerCup, move[1])
            fillLarge = (move[0], largerCup)
            
            sumOfCups = move[0] + move[1]
            transferSmall = (max(sumOfCups - largerCup, 0), min(sumOfCups, largerCup))
            transferLarge = (min(sumOfCups, smallerCup), max(sumOfCups - smallerCup, 0))
            
            addToDict(possibleMoves, emptySmall, oldPossibleMoves[move]) 
            addToDict(possibleMoves, emptyLarger, oldPossibleMoves[move]) 
            addToDict(possibleMoves, fillSmall, oldPossibleMoves[move]) 
            addToDict(possibleMoves, fillLarge, oldPossibleMoves[move]) 
            addToDict(possibleMoves, transferSmall, oldPossibleMoves[move]) 
            addToDict(possibleMoves, transferLarge, oldPossibleMoves[move]) 

        for dest in possibleMoves.keys():
            for source in possibleMoves[dest]:
                if math.isnan(df.at[source, dest]):
                    df.at[source, dest] = i

    
    print (df)    
    
    return

def addToDict(dict, key, value):
    if key not in dict and type(value) is not list:
        dict[key] = [value]
    elif key not in dict:
        dict[key] = value
    elif value not in dict[key] and type(value) is not list:
        dict[key].append(value)        
    elif value not in dict[key]:
        dict[key] = list(set(dict[key] + value))

if __name__ == "__main__":
    main(3, 2)