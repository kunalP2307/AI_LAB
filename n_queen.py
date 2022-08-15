result = []


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < n:
        if board[i][j]:
            return False
        i = i + 1
        j = j - 1
    return True


def get_n_q_sol(board, col, n):
    if col == n:
        v = []
        for row in board:
            for j in range(len(row)):
                if row[j] == 1:
                    v.append(j + 1)
        result.append(v)
        return True

    res = False

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = get_n_q_sol(board, col + 1, n) or res
            board[i][col] = 0
    return res


def print_boards(n):
    print("Total Possible Solutions for Board Size ", n, "*", n, " is :", len(result))
    print('Solutions Are as Follow : ')
    for board in range(len(result)):
        for i in range(n):
            for j in range(n):
                if j == result[board][i] - 1:
                    print('1', end=" ")
                else:
                    print('0', end=" ")
            print()
        print()


n = int(input("Enter Board Size : "))
board = [[0 for i in range(n)] for j in range(n)]
get_n_q_sol(board, 0, n)
print_boards(n)
