import math
from sys import exit

def main():
    circleCount = getNumberOfCircles()
    areas = circleCountLoop(int(circleCount))
    displayAreas(areas)

def getNumberOfCircles():
    try:
        return float(input("How many circles are you working with? "))
    except:
        print("Error!")
        sys.exit()

def computeCircleArea(radius):
    return math.pi * radius**2

def getRadius():
    return float(input("Please enter a radius: "))

def circleCountLoop(circleCount):
    areas = []
    for _ in range(circleCount):
        r = getRadius()
        areas.append(computeCircleArea(r))
    return areas
        
def displayAreas(areas):
    zeroes = '.2f'
    # roundedAreaList = [round(a, 4) for a in areas]
    roundedAreaList = [f"{a:,{zeroes}}" for a in areas]
    # for a in areas:
    #     roundedAreaList.append(f"{a:,{zeroes}}")

    print(roundedAreaList)

# def errorHandling(givenInput):
#     try:
#         givenInput
#     except:
#         print("Error!")

main()

#lambda param1, param2, … paramN: expression