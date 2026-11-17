class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()  # Track cells used in the current path.

        def backtrack(row, column, index):

            # 1. Successful base case: All characters matched.
            if index == len(word):
                return True

            # 2. Check whether coordinates are outside the board.
            if (
                row < 0
                or row >= len(board)
                or column < 0
                or column >= len(board[0])
            ):
                return False

            # 3. Prevent revisiting the same cell.
            if (row, column) in visited:
                return False

            # 4. Check whether the current character matches.
            if board[row][column] != word[index]:
                return False

            # 5. Mark the current cell as visited.
            visited.add((row, column))

            # 6. Recursively explore all four directions.
            found = (
                backtrack(row + 1, column, index + 1) or  # Down
                backtrack(row - 1, column, index + 1) or  # Up
                backtrack(row, column + 1, index + 1) or  # Right
                backtrack(row, column - 1, index + 1)     # Left
            )

            # 7. Backtrack: Remove the current cell.
            visited.remove((row, column))

            # 8. Return whether any direction found the word.
            return found

        # 9. Try every cell as a starting position.
        for row in range(len(board)):
            for column in range(len(board[0])):

                if backtrack(row, column, 0):
                    return True

        # 10. No valid path found.
        return False
