class Solution(object):
    def snakesAndLadders(self, board):

        # flatten board into a 1D array
        board.reverse()
        arr = [0]
        for i, row in enumerate(board):
            if i % 2 == 0:
                arr += row
            else:
                arr += row[::-1]

        NN = len(board) ** 2
        queue = [1]
        visited = set()
        moves = 0
        while queue:

            next_level = []
            while queue:

                square = queue.pop()
                if square == NN:
                    return moves

                    # visit every dice role (1 to 6)
                for i in range(1, 7):

                    # don't visit squares we already saw, don't visit a square past N*N
                    if square + i <= NN and square + i not in visited:
                        visited.add(square + i)

                        # if next square is a snake/ladder, take it
                        if arr[square + i] != -1:
                            next_level.append(arr[square + i])
                        # otherwise go to the square (1 to 6) hops away
                        else:
                            next_level.append(square + i)

            queue = next_level
            moves = moves + 1

        return -1

s=Solution()
board=[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(s.snakesAndLadders(board))