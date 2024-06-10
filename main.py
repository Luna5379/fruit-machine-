import random
import turtle
from turtle import Screen

# globals
bmo = turtle.Turtle(shape='turtle')
bmo.screen.title("Fruit Machine")
symbols = ['cherry', 'bell', 'lemon', 'orange', 'star', 'skull']
symbolPlurals = ['cherries', 'bells', 'lemons', 'oranges', 'stars', 'skulls']
symbolCounts = []
symbolsLength = len(symbols)
thanks = ["That's great to hear!", "Fantastic!", "Glad you're enjoying yourself!", "Someone's getting a bit addicted...", "I'll assume you're having fun!"]
wheelSideWidth = 200
halfWheelSideWidth = wheelSideWidth / 2
symbolPaddingWidth = 30
betweenWheelsWidth = 10
symbolWidth = wheelSideWidth - symbolPaddingWidth * 2
wheelDistance = wheelSideWidth + betweenWheelsWidth
wheelXCoords = [-wheelDistance, 0, wheelDistance]
wheelYCoord = -symbolWidth / 2
wheelsLength = len(wheelXCoords)
credit = 1.00

# functions
def showCredit():
    bmo.up()
    bmo.setheading(270)
    bmo.goto(wheelXCoords[0] - halfWheelSideWidth, -halfWheelSideWidth)

    bmo.fillcolor("black")
    bmo.begin_fill()
    for index in range(2):
        bmo.forward(50)
        bmo.left(90)
        bmo.fd(wheelSideWidth * wheelsLength + betweenWheelsWidth * (wheelsLength - 1))
        bmo.left(90)
    bmo.end_fill()
    bmo.forward(40)
    bmo.left(90)

    bmo.pencolor('#eda800')
    bmo.write("Credit = " + str("£{:,.2f}".format(credit)), False, "Left", ('Algerian', 24, 'bold'))

def updateCredit(creditChange):
    global credit
    credit += creditChange
    showCredit()

def printWheels(wheels, separator):
    for index in range(wheelsLength):
        print(wheels[index], end="\n" if index == wheelsLength - 1 else separator)

def spin():
    wheels = []
    for dummy in wheelXCoords:
        wheels.append(symbols[random.randint(0, 5)])
    return wheels

def printWow(symbolIndex):
    symbolCount = symbolCounts[symbolIndex]
    plural = symbolPlurals[symbolIndex]
    print("Wow! You got " + str(symbolCount) + " " + plural + "!")

def positionTurtle(wheelIndex):
    bmo.pu()
    bmo.setheading(0)

    bmo.goto(wheelXCoords[wheelIndex], wheelYCoord)

def clearBox(wheelIndex):
    positionTurtle(wheelIndex)
    bmo.fd(wheelSideWidth/2)
    bmo.rt(90)
    bmo.fd(symbolPaddingWidth)
    bmo.lt(90)
    bmo.fillcolor("white")
    bmo.pencolor("black")
    bmo.pd()
    bmo.begin_fill()
    for index in range(4):
        bmo.left(90)
        bmo.fd(wheelSideWidth)
    bmo.end_fill()

def clearFruitMachine():
    for wheelIndex in range(wheelsLength):
        clearBox(wheelIndex)

def RandomizeColorComponent(min=0, max=100):
    return (min + random.randint(0, max - min)) / 100

def drawStalk():
    # NOTE: turtle must be heading N

    stalkAngle = 45 + random.randint(0, 30)
    bmo.right(stalkAngle)
    bmo.pencolor((0, RandomizeColorComponent(min=35, max=65), 0))
    bmo.down()
    stalkWidth = symbolWidth / 20
    bmo.circle(stalkWidth, extent=180)

def drawOrange(wheelIndex):
    positionTurtle(wheelIndex)

    bmo.fillcolor((1, RandomizeColorComponent(min=35, max=65), 0))
    bmo.begin_fill()
    bmo.circle(symbolWidth / 2)
    bmo.end_fill()

    bmo.up()
    bmo.left(90)
    bmo.forward(symbolWidth)
    drawStalk()

def drawLemon(wheelIndex):
    positionTurtle(wheelIndex)
    
    smallRadius = symbolWidth / 5
    bigRadius = symbolWidth / 2.5
    bigCircleStart = smallRadius / 2
    topSmallCircleStart = bigRadius * 2 - bigCircleStart * 3
    bmo.fillcolor((RandomizeColorComponent(min=90), 1, 0))
    bmo.begin_fill()
    bmo.circle(smallRadius)
    bmo.lt(90)
    bmo.fd(bigCircleStart)
    bmo.rt(90)
    bmo.circle(bigRadius)
    bmo.lt(90)
    bmo.fd(topSmallCircleStart)
    bmo.rt(90)
    bmo.circle(smallRadius)
    bmo.end_fill()

    bmo.up()
    bmo.left(90)
    bmo.forward(smallRadius * 2)
    drawStalk()

def drawCherry(wheelIndex):
    positionTurtle(wheelIndex)
    
    distanceToCherry = symbolWidth / 3.5
    cherryRadius = symbolWidth / 4.5
    vineLength = cherryRadius * 3
    bmo.fd(distanceToCherry)
    bmo.pencolor((0, RandomizeColorComponent(15, 70), 0))
    bmo.fillcolor((RandomizeColorComponent(50, 100), 0,  RandomizeColorComponent(0, 35)))
    bmo.begin_fill()
    bmo.circle(cherryRadius)
    bmo.backward(distanceToCherry * 2)
    bmo.circle(cherryRadius)
    bmo.end_fill()
    bmo.lt(90)
    bmo.fd(cherryRadius * 2)
    bmo.pd()
    bmo.dot()
    for index in range(2):
        bmo.right(25)
        bmo.fd(vineLength)
        bmo.dot()
        bmo.right(105)

def drawJaw(jawLength):
    # NOTE: heading/colors are taken from outside
    
    origin = bmo.position()

    bmo.begin_fill()
    bmo.down()
    bmo.forward(jawLength / 2)
    bmo.left(75)
    bmo.forward(jawLength / 2)
    bmo.left(105)
    bmo.forward(jawLength * 3 / 5)
    bmo.end_fill()
    bmo.up()
    bmo.goto(origin)
    bmo.begin_fill()
    bmo.down()
    bmo.forward(jawLength / 2)
    bmo.right(75)
    bmo.forward(jawLength / 2)
    bmo.right(105)
    bmo.forward(jawLength * 4 / 5)
    bmo.up()
    bmo.end_fill()

def drawSkull(wheelIndex):
    positionTurtle(wheelIndex)
    
    origin = bmo.position()
    jawLength = symbolWidth * 0.45
    originToEyeDistance = jawLength * 1.3
    centerToEyeDistance = jawLength * 0.4
    eyeRadius = jawLength * 0.35
    bmo.pencolor('#555')
    bmo.fillcolor('#ccc')

    bmo.goto(origin)
    bmo.left(90)
    bmo.forward(jawLength * 0.45)
    bmo.right(90)
    bmo.begin_fill()
    bmo.down()
    bmo.circle(jawLength)
    bmo.up()
    bmo.end_fill()

    bmo.goto(origin)
    drawJaw(jawLength)

    bmo.goto(origin)
    bmo.left(90)
    bmo.forward(jawLength * 1.05)
    bmo.left(90)
    drawJaw(jawLength)

    bmo.fillcolor('black')

    bmo.goto(origin)
    bmo.right(90)
    bmo.forward(originToEyeDistance)
    bmo.right(90)
    bmo.forward(centerToEyeDistance)
    bmo.begin_fill()
    bmo.circle(eyeRadius)
    bmo.end_fill()

    bmo.goto(origin)
    bmo.left(90)
    bmo.forward(originToEyeDistance)
    bmo.right(90)
    bmo.back(centerToEyeDistance)
    bmo.begin_fill()
    bmo.circle(eyeRadius)
    bmo.end_fill()

def drawStar(wheelIndex, drawBorder=False):
    positionTurtle(wheelIndex)
    
    verticesCount = 5
    starWidth = symbolWidth * 1.2
    separatorWidth = symbolWidth * 0.375
    bmo.fillcolor('gold')
    bmo.pencolor('orange')

    if drawBorder == True:
        bmo.back(separatorWidth)
        bmo.left(180 / verticesCount)
        bmo.down()
        for index in range(verticesCount):
            bmo.forward(starWidth)
            bmo.left(720 / verticesCount)
        bmo.up()
        positionTurtle(wheelIndex)

    bmo.back(separatorWidth)
    bmo.left(180 / verticesCount)
    bmo.begin_fill()
    for index in range(verticesCount):
        bmo.forward(starWidth)
        bmo.left(720 / verticesCount)
    bmo.end_fill()

def drawBell(wheelIndex):
    positionTurtle(wheelIndex)

    origin = bmo.position()
    halfBottomWidth = symbolWidth / 2.35
    halfTopWidth = symbolWidth * 2 / 5
    sideLength = symbolWidth * 0.8
    bellRadius = symbolWidth * 0.25
    hookRadius = symbolWidth / 17
    bmo.fillcolor('#eda800')

    bmo.begin_fill()
    bmo.forward(halfBottomWidth)
    bmo.left(105)
    bmo.forward(sideLength)
    bmo.left(75)
    bmo.forward(halfTopWidth)
    bmo.end_fill()

    bmo.goto(origin)
    bmo.begin_fill()
    bmo.forward(halfBottomWidth)
    bmo.right(105)
    bmo.forward(sideLength)
    bmo.right(75)
    bmo.forward(halfTopWidth)
    bmo.end_fill()
    
    bmo.goto(origin)
    bmo.setheading(90)
    bmo.forward(sideLength - bellRadius)
    bmo.setheading(0)
    bmo.begin_fill()
    bmo.circle(bellRadius)
    bmo.end_fill()

    bmo.left(90)
    bmo.fd(bellRadius * 2)
    bmo.rt(90)
    bmo.fd(hookRadius)
    bmo.left(90)
    bmo.pencolor('#d4af37')
    bmo.pd()
    bmo.circle(hookRadius, 180)
    bmo.pu()

    positionTurtle(wheelIndex)
    bmo.forward(halfBottomWidth)
    bmo.left(100)
    bmo.fillcolor('#98720b')
    bmo.begin_fill()
    bmo.circle(halfBottomWidth * 1.015, 160)
    bmo.left(100)
    bmo.fd(halfBottomWidth)
    bmo.end_fill()

# initialize turtle
bmo.speed('fastest')
bmo.pensize(5)
bmo.hideturtle()
bmo.screen.bgcolor("black")

# Intro Screen
bmo.pencolor('#eda800')
bmo.pu()
bmo.left(90)
bmo.forward(wheelSideWidth / 2)
bmo.right(90)
bmo.write("Fruit Machine", False, "Center", ('Algerian', 50, 'bold'))
clearFruitMachine()
showCredit()
print("""Welcome to my fruit machine!
Just some quick rules before we can start!
-You must be 18 or over to engage in gambling.
You will start with £1 in credits, and each turn will cost you 20 pence.
You have the chance to win up to £5 in each go, but there is also the risk of losing all your credit!
In each go, the fruit machine will roll 3 items, and certain combinations can make you rich! (not really)
Just remember, the aim of this game is to have fun! (and also for me to show off my coding skills)""")
play = input("So, what do you say? Would you like to play with the fruit machine? [y/n (Typos aren't accepted, sorry.)] ").lower() # NOTE: from now on the reply is lower-cased
while play not in ('y', 'n'):
    play = input("""That isn't even a valid response. I literally said no typos allowed, what are you trying to do, break my code? Now, answer properly.
Do you want to play? [y/n ONLY. >:(] """).lower()
if play != 'y':
    print("""Oh... So you don't want to play... I'll try not to take this personally then!
You're probably just under 18 or something. Maybe you're a pure soul who doesn't involve themself in polluting games like gambling. Of course!
And if not... Sorry I managed to put you off before you even rolled your first roll. :(""")
else:
    print("Let's get this party started then!")
    play = True
    print("You have " + str("£{:,.2f}".format(credit)))

while play == True and credit >= 0.20:
    bmo.penup()

    print("Rolling...")
    updateCredit(-0.2)
    wheels = spin()
    printWheels(wheels, separator='|')

    # count wheel symbols
    symbolCounts.clear()
    for symbolIndex in range(symbolsLength):
        symbol = symbols[symbolIndex]
        symbolCounts.append(wheels.count(symbol))

    # draw wheel symbols
    drawingFunctions = [drawCherry, drawBell, drawLemon, drawOrange, drawStar, drawSkull]
    for wheelIndex in range(wheelsLength):
        wheelSymbol = wheels[wheelIndex]
        symbolIndex = symbols.index(wheelSymbol)
        drawingFunction = drawingFunctions[symbolIndex]
        drawingFunction(wheelIndex)

    for symbolIndex in range(symbolsLength):
        symbol = symbols[symbolIndex]
        symbolCount = symbolCounts[symbolIndex]
        if symbolCount == 3:
            if symbol == 'skull':
                print("""Oh no! You rolled 3 skulls!
You have lost all of your credits now. D:""")
                updateCredit(-credit)
            elif symbol == 'bell':
                print("""Yahoo! You got 3 bells!
You win an extra £5 in credits! XD""")
                updateCredit(+5)
            else:
                printWow(symbolIndex)
                print("You win an extra pound in credits! :D")
                updateCredit(+1)
        elif symbolCount == 2:
            if symbol == 'skull':
                print("""Oh no! You rolled 2 skulls!
You lose £1 worth of credits. :(""")
                updateCredit(-1)
            else:
                printWow(symbolIndex)
                print("You win an extra 50 pence in credits! :)")
                updateCredit(+0.5)
    print("You have " + str("£{:,.2f}".format(credit)) + " left.")
    if credit >= 0.20:
        play = input("Would you like to play again? (If you don't you can leave with your winnings.) [y/n (Typos aren't accepted, sorry.)] ")
        while play != 'y' and play != 'Y' and play != 'n' and play != 'N':
            play = input("""That isn't even a valid response. I literally said no typos allowed, what are you trying to do, break my code? Now, answer properly.
Do you want to play again? If you choose no, you leave with your winnings. [y/n ONLY. >:(] """)
        if play != 'y' and play != 'Y':
            print("""You have chosen to leave with your winnings! Thank you for indulging in your gambling addiction!
You have left with """ + str("£{:,.2f}".format(credit)) + " in winnings!")
        else:
            thank = thanks[random.randint(0, 4)]
            print(thank)
            clearFruitMachine()
            play = True
    else:
        print("""You have reached less than 20 pence in credits! This means you don't have enough money to play anymore games.
This is what gambling does to people. RIP your bank account. Bye!""")
