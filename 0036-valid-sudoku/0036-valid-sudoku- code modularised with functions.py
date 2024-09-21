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

        def are_rows_valid(board):
            for row in board:
                if not is_unit_valid(row):
                    return False
            return True
            
        def are_columns_valid(board):
            for c in range(0,9):
                column = [board[i][c] for i in range(0,9)]
                if not is_unit_valid(column):
                    return False
            return True

        def are_squares_valid(board):
            for i in [0,3,6]:
                for j in [0,3,6]:
                    square = [board[r][c] for r in range(i,i+3) for c in range(j,j+3)]
                    if not is_unit_valid(square):
                        return False
            return True
        
        def is_unit_valid(unit):
            elements = [i for i in unit if i!="." ]
            return len(set(elements)) == len(elements)

        return are_rows_valid(board) and are_columns_valid(board) and are_squares_valid(board)