from IPython.display import clear_output

#Method to display board
def display_board(board):
    #clear_output()  # Remember, this only works in jupyter!
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Create a list to test display on board
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)