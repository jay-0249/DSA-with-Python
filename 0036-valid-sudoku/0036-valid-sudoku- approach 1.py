class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        '''
        Iterate over the rows, store the unique numbers in a set, at each iteration if you find a a number duplicate then return as invalid Sudoko
        Similarly iterate over the columns, and check the validity in the same way
        Similarly iterate over each of the 9 squares and check for the validity in the same way

        Time Complexity - O(N^2) here N is either the number of rows or columns
        Space Complexity - O(N) to store the set of elements in a row or column or square 
        '''
        #check rows
        for i in range(0,9):
            unique_numbers = set()
            for j in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] in unique_numbers:
                        return False
                    else:
                        unique_numbers.add(board[i][j])

        #check columns
        for i in range(0,9):
            unique_numbers = set()
            for j in range(0,9):
                if board[j][i] != ".":
                    if board[j][i] in unique_numbers:
                        return False
                    else:
                        unique_numbers.add(board[j][i])

        #check squares
        for box_row in range(0,3):
            for box_column in range(0,3):
                #check one square
                unique_numbers = set()
                for i in range(box_row*3,(box_row+1)*3):
                    for j in range(box_column*3,(box_column+1)*3):
                        if board[i][j] != ".":
                            if board[i][j] in unique_numbers:
                                return False
                            else:
                                unique_numbers.add(board[i][j])

        return True