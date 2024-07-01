inBound = lambda row, col, n: 0 <= row < 2 and 0 <= col < n
directions = [[0, 1], [1, 0], [-1, 0]]

def isthereWay(row, col, string, moved):
    if row == 1 and col >= len(string[0]) - 1:
        return True

    moved.add((row, col))

    if string[row][col] == ">":
        col += 1
    else:
        col -= 1

    if row == 1 and col >= len(string[0]) - 1:
        return True

    for r, c in directions:
        new_row = row + r
        new_col = col + c
        if inBound(new_row, new_col, len(string[0])) and (new_row, new_col) not in moved:
            if isthereWay(new_row, new_col, string, moved):
                return True
    return False

for _ in range(int(input())):
    n = int(input())
    row1 = input()
    row2 = input()
    string = [row1, row2]
    moved = set()
    if isthereWay(0, 1, string, moved) or isthereWay(1, 0, string, moved):
        print("YES")
    else:
        print("NO")
