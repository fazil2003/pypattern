def pattern_A(char='*'):
    for i in range(7):
        for j in range(7):
            if (j == 0 or j == 6) and (i > 0) or (i == 0 or i == 3) and (j > 0 and j < 6):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_B(char='*'):
    for i in range(5):
        for j in range(6):
            if j == 0 or (i == 0 or i == 2 or i == 4) and (j < 5) or j == 5 and (i > 0 and i < 4 and i != 2):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_C(char='*'):
    for i in range(6):
        for j in range(7):
            if (j == 0 and i != 0 and i != 5) or (i == 0 or i == 5) and (j > 1 and j < 5) or (i == 1 or i == 4) and (
                    j > 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_D(char='*'):
    for i in range(6):
        for j in range(6):
            if j == 0 and (i > 0 and i < 5) or (i == 0 or i == 5) and (j < 4) or j == 5 and (i != 0 and i != 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_E(char='*'):
    for i in range(5):
        for j in range(6):
            if j == 0 or i == 0 or i == 2 or i == 4:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_F(char='*'):
    for i in range(6):
        for j in range(6):
            if j == 0 or i == 0 or (i == 2 and j < 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_G(char='*'):
    for i in range(8):
        for j in range(7):
            if j == 0 and (i > 1 and i < 5) or (i == 1 or i == 5) and ((j > 0 and j < 2) or j > 5) or (
                    i == 0 or i == 6) and (j > 2 and j < 6) or (i == 4 and j > 3) or (i == 7 and j > 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_H(char='*'):
    for i in range(7):
        for j in range(7):
            if (j == 0 or j == 6 or i == 3):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_I(char='*'):
    for i in range(7):
        for j in range(7):
            if i == 0 or i == 6 or j == 3:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_J(char='*'):
    for i in range(6):
        for j in range(5):
            if (j == 4 and i != 5) or (i == 5 and (j > 0 and j < 4)) or i == 4 and j < 1:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_K(char='*'):
    for i in range(7):
        for j in range(5):
            if j == 0 or i + j == 4 or i - j == 2:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_L(char='*'):
    for i in range(6):
        for j in range(6):
            if j == 0 or i == 5:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_M(char='*'):
    for i in range(7):
        for j in range(7):
            if j == 0 or ((i - j == 0 or i + j == 6) and (i < 4)) or j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_N(char='*'):
    for i in range(7):
        for j in range(7):
            if j == 0 or i - j == 0 or j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_O(char='*'):
    for i in range(6):
        for j in range(9):
            if ((j == 0 or j == 8) and (i > 1 and i < 4)) or ((i == 0 or i == 5) and (j == 3 or j == 5)) or (
                    (i == 1 or i == 4) and (j == 1 or j == 7)):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_P(char='*'):
    for i in range(7):
        for j in range(6):
            if (j == 0 and i != 0) or ((i == 0 or i == 3) and (j != 0) and (j < 5)) or (
                    (i == 1 or i == 2) and (j == 5 or j == 6)):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_Q(char='*'):
    for i in range(7):
        for j in range(9):
            if ((j == 0 or j == 8) and (i > 1 and i < 4)) or ((i == 0 or i == 5) and (j == 3 or j == 5)) or (
                    (i == 1 or i == 4) and (j == 1 or j == 7)) or ((i - j == 0) and (i > 3 and i < 7)):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_R(char='*'):
    for i in range(7):
        for j in range(7):
            if j == 0 or ((i == 0 or i == 3) and (j < 4)) or (i == 1 or i == 2) and (
                    j > 4 and j != 6) or i - j == 0 and i > 3:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_S(char='*'):
    for i in range(7):
        for j in range(7):
            if ((i == 0 or i == 3 or i == 6) and (j != 0 and j != 6)) or (j == 0) and (i == 1 or i == 2 or i == 5) or (
                    j == 6) and (i == 4 or i == 5 or i == 1):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_T(char='*'):
    for i in range(6):
        for j in range(7):
            if i == 0 or j == 3:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_U(char='*'):
    for i in range(7):
        for j in range(7):
            if ((j == 0 or j == 6) and (i != 6)) or i == 6 and (j > 1 and j < 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_V(char='*'):
    for i in range(7):
        for j in range(13):
            if i - j == 0 or i + j == 12:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_W(char='*'):
    for i in range(7):
        for j in range(26):
            if i - j == 0 or i + j == 12 or i + j == 24 or (i - j == (-12)):
                print(char, end="")
            else:
                print(end=" ")

        print()


def pattern_X(char='*'):
    for i in range(7):
        for j in range(7):
            if i - j == 0 or i + j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_Y(char='*'):
    for i in range(7):
        for j in range(7):
            if ((i - j == 0 or i + j == 6) and i < 4) or j == 3 and (i > 3):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_Z(char='*'):
    for i in range(7):
        for j in range(7):
            if i == 0 or i == 6 or i + j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()
