def pattern_a(char='*'):
    for i in range(9):
        for j in range(10):
            if (j == 8 and i != 0 and i != 8) or ((i == 0 or i == 7) and (j > 2 and j < 7)) or i + j == 5 and i > 3 or (
                    (i == 3 and j > 2 and j < 7)) or i == 6 and j > 0 and j < 2 or i == 8 and j > 8 or (
                    (i == 1 or i == 2) and (j == 0 and j == 1)) or (i == 1 and j == 1):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_b(char='*'):
    for i in range(9):
        for j in range(7):
            if (j == 1 and i < 7 and i != 6) or (((
                                                          i == 3 and j != 2) or i == 6) and j > 1 and j < 5) or j == 6 and i > 3 and i < 6 or j == 0 and i == 7:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_c(char='*'):
    for i in range(6):
        for j in range(7):
            if (j == 0 and i != 0 and i != 5) or (i == 0 or i == 5) and (j > 1 and j < 5) or (i == 1 or i == 4) and (
                    j > 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_d(char='*'):
    for i in range(10):
        for j in range(7):
            if (j == 5 and i < 8) or ((i == 3 or i == 7) and j < 5 and j > 2) or (j == 1) and (i == 4 or i == 6) or (
                    j == 0 and i == 5) or i == 8 and j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_e(char='*'):
    for i in range(7):
        for j in range(7):
            if (i == 2 or (i == 5 and j > 1)) or (i == 0 and j < 5 and j > 1) or (i == 1 and (j == 6 or j == 0)) or (
                    j == 0 and i > 2 and i < 5):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_f(char='*'):
    for i in range(9):
        for j in range(7):
            if ((j == 2) or (i == 3)) and (i != 0 and i < 6) or (i == 0 and j > 2 and j < 6) or (
                    i == 1 and j == 6) or j == 1 and i == 6 or j == 0 and i == 5:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_g(char='*'):
    for i in range(9):
        for j in range(1, 7):
            if ((i == 1 or i == 4 or i == 6) and j > 2 and j < 6) or (i == 2 or i == 3) and (j == 2 or j == 6) or (
                    j == 6 and i > 4 and i < 6):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_h(char='*'):
    for i in range(7):
        for j in range(7):
            if j == 0 or i == 3 and j > 1 and j < 5 or j == 6 and i > 3:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_i(char='*'):
    for i in range(9):
        for j in range(7):
            if (j == 3 and i != 1 and i != 3) or (i == 1 and (j == 1 or j == 5)):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_j(char='*'):
    for i in range(9):
        for j in range(7):
            if (j == 3 and i != 1 and i != 3 and i < 8) or (i == 1 and (j == 1 or j == 5)) or i == 8 and j == 2:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_k(char='*'):
    for i in range(8):
        for j in range(5):
            if j == 0 or i + j == 5 and i > 0 or i - j == 3:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_l(char='*'):
    for i in range(7):
        for j in range(7):
            if j == 3 and i != 6 or i == 6 and (j == 2 or j == 4):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_m(char='*'):
    for i in range(7):
        for j in range(13):
            if (j == 1 and i > 1 or ((j == 6 or j == 11) and i > 1)) or j == 0 and i == 0 or (
                    i == 1 and ((j == 3 or j == 4 or j == 8 or j == 9))):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_n(char='*'):
    for i in range(5):
        for j in range(8):
            if ((j == 1 or j == 7) and i > 0) or ((i == 0) and j != 1 and j != 6 and j != 2 and j != 7):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_o(char='*'):
    for i in range(5):
        for j in range(6):
            if ((j == 0 or j == 5) and i > 1 and i < 4) or ((i == 1 or i == 4) and j > 1 and j < 4):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_p(char='*'):
    for i in range(7):
        for j in range(7):
            if ((j == 1 or (j == 5 and i < 3)) and i != 0) or ((i == 3 or i == 0) and (j > 1 and j < 5)) or (
                    i == 0 and j == 0):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_q(char='*'):
    for i in range(7):
        for j in range(11):
            if j == 6 and i > 0 or ((i == 0 or i == 3) and j > 1 and j < 5) or (
                    j == 0 and i > 0 and i < 3) or i == 0 and j == 7 or i + j == 12:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_r(char='*'):
    for i in range(7):
        for j in range(9):
            if (j == 2 and i != 0) or (i + j == 5 and (i != 0 and i < 3)) or j == 0 and i == 0 or (i == 0 and j == 6):
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_s(char='*'):
    for i in range(7):
        for j in range(7):
            if (((
                         i == 0 or i == 6 or i == 3) and j != 6) and j > 0) or j == 0 and i > 0 and i < 3 or j == 6 and i > 3 and i < 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_t(char='*'):
    for i in range(7):
        for j in range(8):
            if j == 3 and i != 6 or i == 2 or i == 6 and j == 5 or j == 7 and i == 5:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_u(char='*'):
    for i in range(7):
        for j in range(7):
            if ((j == 0 or j == 5) and i < 4) or i == 4 and j > 1 and j < 4 or i == 5 and j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_v(char='*'):
    for i in range(7):
        for j in range(13):
            if i - j == 0 or i + j == 12:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_w(char='*'):
    for i in range(7):
        for j in range(26):
            if i - j == 0 or i + j == 12 or i + j == 24 or (i - j == (-12)):
                print(char, end="")
            else:
                print(end=" ")

        print()


def pattern_x(char='*'):
    for i in range(7):
        for j in range(7):
            if i - j == 0 or i + j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()


def pattern_y(char='*'):
    for i in range(9):
        for j in range(10):
            if i + j == 9 and i < 8 or i == j and i < 5 or i == 7 and j == 0:
                print(char, end="")
            else:
                print(end=" ")

        print()


def pattern_z(char='*'):
    for i in range(7):
        for j in range(7):
            if i == 0 or i == 6 or i + j == 6:
                print(char, end="")
            else:
                print(end=" ")
        print()
