


def playingField(a):
    for i in a:
        f = '{:3}' * len(i)
        print(f.format(*i))


def borderCheck(k, n):
    k = k - 1
    if k >= n or k < 0:
        k = int(input(f"we've got only {n}*{n} square, pick another number: "))
        return borderCheck(k, n)
    return k + 1


def employment_check(i, j, a, n):
    i = i - 1
    j = j - 1
    if a[i][j] != 0:
        i = int(input(f"cell is occuped, pick another row: "))
        j = int(input(f"pick another column: "))
        borderCheck(i, n)
        borderCheck(j, n)
        return employment_check(i, j, a, n)
    return i + 1, j + 1

def checkWin(playerNumber, i, j, n, a):
    i = i - 1
    j = j - 1
    win_line = 0


    for y in range(max(i - 3, 0), min(i + 4, n)):
        if a[y][j] == playerNumber:
            win_line += 1
        else:
            win_line = 0
        if win_line >= 4:
            return True


    win_line = 0
    for y in range(max(j - 3, 0), min(j + 4, n)):
        if a[i][y] == playerNumber:
            win_line += 1
        else:
            win_line = 0
        if win_line >= 4:
            return True


    win_line = 0
    for y in range(0, 5):
        if not (0 <= i - 3 + y < n and 0 <= j - 3 + y < n):
            continue
        if a[i - 3 + y][j - 3 + y] == playerNumber:
            win_line += 1
        else:
            win_line = 0
        if win_line >= 4:
            return True


    win_line = 0
    for y in range(0, 5):
        if not (0 <= i + 3 - y < n and 0 <= j - 3 + y < n):
            continue
        if a[i + 3 - y][j - 3 + y] == playerNumber:
            win_line += 1
        else:
            win_line = 0
        if win_line >= 4:
            return True

    return False


class Game:
    def __init__(self, n=10, numberOfPlayers = 2):
        self.n = n
        self.numberOfPlayers=numberOfPlayers
        self.a = [[0 for i in range(n)] for j in range(n)]
        self.isWin = False


def players_move(y, game):
    row = int(input(f"Player {y}, row: "))
    row = borderCheck(row, game.n)
    column = int(input(f"Player {y}, column: "))
    column = borderCheck(column, game.n)
    row, column = employment_check(row, column, game.a, game.n)
    game.a[row - 1][column - 1] = y

    playingField(game.a)
    if checkWin(y, row, column, game.n, game.a):
        print(f"FANTASTICA OAOAOA PLAYER {y} WON")
        game.isWin = True

def main():
    game=Game()
    playingField(game.a)
    while not game.isWin:
        for y in range(1, game.numberOfPlayers + 1):
            players_move(y, game)
            if game.isWin:
                return


if __name__ == "__main__":
    print("Let's play a game")
    main()
