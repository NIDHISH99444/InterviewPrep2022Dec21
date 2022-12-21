

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

board.reverse()
print(board)
arr = [0]
for i, row in enumerate(board):
    if i % 2 == 0:
        arr += row
    else:
        arr += row[::-1]


print(arr)