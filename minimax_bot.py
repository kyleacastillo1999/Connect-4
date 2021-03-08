import math

"""
@author: Kyle Castillo
Contact: kylea.castillo1999@gmail.com
Date: 03/08/2021

Minimax Alpha-Beta Pruning Search for a Connect-4 Game
"""

"""
eval_echo, echo for the sake of uniqueness, evaluates a connect-4 board
and returns a position that the bot wishes to place a piece. It will 
go down based on a depth set by one of the passed parameters.

Note that only board and player_id should be passed since the rest
are important to the algorithm.
"""

ROWS = 6
COLS = 7


class EchoC4:

    def minimax_echo(self, board, player_id, depth=4, alpha=-math.inf, beta=math.inf, maximizing=True):
        """
        :param board: A 2D array of the board
        :param player_id: The player number that the bot is
        :param depth: Number of plies that the bot will search
        :param alpha: The max value that can be achieved.
        :param beta: The minimum value that can be achieved.
        :param maximizing: Testing for maximizing player_id
        :return: Returns an integer 0-6 to place a piece.
        """
        pos = None

        # First check and see if the bot is going first.
        if player_id == 1 and board[5].count(1) == 0:
            # If it is CLAIM THE MIDDLE
            return 3

        # Maximizing player, we want to check the best position for max.
        if maximizing:
            max_score = -math.inf
            for row in range(ROWS):
                eval = self.minimax_echo(board, player_id, depth - 1, alpha, beta, False)




