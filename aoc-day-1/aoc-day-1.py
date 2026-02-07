rotations = []

def setRotations():
    with open("rotation-inputs.txt", "r") as file:
        for i in file:
            formattedInput = i.rstrip()
            rotations.append(formattedInput)


def checkRotation():
   position = 50
   combinationCount = 0
   for i in rotations:
        direction = i[0]
        value = int(i[1:])
        if direction == "L":
            value = -value
        
        position = position + value
        while position > 99:
            position = position - 100
        while position < 0:
            position = position + 100
        if position == 0:
            combinationCount = combinationCount + 1
   combinationCount = str(combinationCount)    
   return combinationCount

setRotations()
print("The dial was zero " + checkRotation() + " times.")
