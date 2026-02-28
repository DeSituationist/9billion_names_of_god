def get_tic_tac_toe_winner(input_board: list[list[str]]) -> str | None:
    '''Function that defines tic_tac_toe winner'''
    for row in input_board:
        if len(set(row)) == 1: return row[0]
    all_columns = [[input_board[j][i] for j in range(3)] for i in range(3)]
    for column in all_columns:
        if len(set(column)) == 1: return column[0]
    diagnals = [[input_board[0][0], input_board[1][1], input_board[2][2]], [input_board[0][2], input_board[1][1], input_board[2][0]]]
    for diag in diagnals:
        if len(set(diag)) == 1: return diag[0]
print(get_tic_tac_toe_winner([["X", "X", "X"], ["O", "X", "O"], ["X", "O", "O"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "O", ""], ["X", "O", "O"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "X", ""], ["X", "O", "O"]]))