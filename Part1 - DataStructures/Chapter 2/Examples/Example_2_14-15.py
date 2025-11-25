#Example 2-14. A list with three lists of length 3 can represent a tic-tac-toe board

board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

#Equivalent to:
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)

#Example 2-15. A list with three references to the same list is useless
weird_board = [['_'] * 3] * 3 #The outer list is made of three references to the same inner list.
print(weird_board)
weird_board[1][2] = 'X'
print(weird_board)

#Equivalent to:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)