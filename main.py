
def coordinate_to_tuple(inputCoor):
    return (ord(inputCoor[0])-ord("A")+1, int(inputCoor[1]))

def translate_coordinates(inputCoor):
    startInput, endInput = inputCoor.split("-")
    resultStartCoor = coordinate_to_tuple(startInput)
    resultEndCoor = coordinate_to_tuple(endInput)
    return (resultStartCoor,resultEndCoor)

def check_vertical(startCoor, endCoor):
    return startCoor[0]==endCoor[0]

def check_horizontal(startCoor, endCoor):
    return startCoor[1]==endCoor[1]

def check_diagonals(startCoor, endCoor):
    return abs(endCoor[0]-startCoor[0]) == \
            abs(endCoor[1]-startCoor[1])

def check_pawn(startCoor, endCoor):
    return (endCoor[1] - startCoor[1] == 1) and \
            (endCoor[0]==startCoor[0])

def check_rook(startCoor, endCoor):
    return check_horizontal(startCoor, endCoor) or \
            check_vertical(startCoor, endCoor)

def check_knight(startCoor, endCoor):
    return (pow(endCoor[0] - startCoor[0],2) + \
            pow(endCoor[1]-startCoor[1],2)) == 5

def check_bishop(startCoor, endCoor):
    return check_diagonals(startCoor, endCoor)

def check_queen(startCoor, endCoor):
    return check_horizontal(startCoor, endCoor) or \
            check_vertical(startCoor, endCoor) or \
            check_diagonals(startCoor, endCoor)

def check_king(startCoor, endCoor):
    horizontal = abs(endCoor[0] - startCoor[0])
    vertical = abs(endCoor[1] - startCoor[1])
    return (horizontal == 0 or horizontal == 1) and \
            (vertical==0 or vertical==1)

def check_figure(figure, startCoor, endCoor):
    if(figureChecks.get(figure)):
        return figureChecks[figure](startCoor, endCoor)

    return False


figureChecks = {
    "Pawn": check_pawn,
    "Rook": check_rook,
    "Knight": check_knight,
    "Bishop": check_bishop,
    "Queen": check_queen,
    "King": check_king
}


figureInput = input("Input figure:")
coorInput = input("Input coordinates:")
coordinates = translate_coordinates(coorInput)
result = check_figure(figureInput, *coordinates)
print(result)
