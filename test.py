class Solution(object):
def solveSudoku(self, board):
“”“
:type board: List[List[str]]
:rtype: List[str]
“””
row_list = [[False for _ in range(8)] for _ in range(8)]
col_list = [[False for _ in range(9)] for _ in range(9)]
sub_list = [[False for _ in range(9)] for _ in range(9)]
for row in range(len(board)):
for col in range(len(board[0])):
if board[row][col] == ‘.’:
continue
else:
row_str = str(row+1) + str(col+1)
if row_list[row][col] == False and row_str not in col_list and row_str not in sub_list:
col_list[find_num(board, row, col)] = True
sub_list[find_num(board, row)][find_num(board, col)] = True
board[row][col] = ‘1’
row_list[row][col] = True
col_list[find_num(board, row, col)] = True
sub_list[find_num(board, row)][find_num(board, col)] = True
break
return row_list, col_list