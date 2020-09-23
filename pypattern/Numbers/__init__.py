def pattern_0(char='*'):
    for i in range(6):
        for j in range(6):
            if (j == 0 or j == 5) and (i > 0 and i < 5) or (i == 0 or i == 5) and (j > 1 and j < 4):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_1(char='*'):
    for i in range(5):
        for j in range(5):
            if (i == 4) or (j == 2) or ((i + j == 2) and (j < 3)):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_2(char='*'):
    for i in range(10):
        for j in range(7):
            if (i == 9) or (i - j == 2 and (j < 2)) or (i == 1 and (j < 1)) or (
                    i == 0 and (j > 1 and j < 5)) or j == 6 and (i > 0 and i < 3) or i + j == 9 and (i > 2):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_3(char='*'):
    for i in range(8):
        for j in range(7):
            if i == 0 or i + j == 6 and (j > 2) or i == j and (j > 3) or i == 7 and (j > 1) or i - j == 5 and (i > 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_4(char='*'):
    for i in range(8):
        for j in range(9):
            if j == 6 or i + j == 6 and i < 6 or i == 5 and j > 0:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_5(char='*'):
    for i in range(7):
        for j in range(6):
            if i == 6 or i == 0 or j == 0 and (i < 3) or i == 3 or j == 5 and i > 3:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_6(char='*'):
    for i in range(6):
        for j in range(6):
            if j == 0 and i > 1 or i == 1 and j > 0 and j < 2 or i == 0 and j > 2 and j < 5 or i == 5 and j < 5 or i == 2 and j < 5 and j > 1 or j == 5 and (
                    i > 2 and i < 5) or i == 3 and j < 2:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_7(char='*'):
    for i in range(6):
        for j in range(6):
            if i == 0 or i + j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_8(char='*'):
    for i in range(7):
        for j in range(7):
            if i == 0 or j == 0 or j == 6 or i == 3 or i == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_9(char='*'):
    for i in range(6):
        for j in range(6):
            if i == 5 and j > 0 and j < 5 or i == 4 and (j < 1 or j > 4) or j == 5 and (i > 1 and i < 5) or i == 0 and (
                    j > 1 and j < 5) or i == 1 and (j < 1 or j > 4) or i == 2 and (j != 0 and j != 4):
                print(char, end="")
            else:
                print(end=" ")
        print()
