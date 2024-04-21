import random
import math

class Player:
    def __init__ (self, Letter):
        self.letter = Letter

    def getMove(self, game):
        pass

class randomComputerPLayer(Player):
    def __init__ (self,letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.availableMoves())
        return square

class humanPlayer(Player):
    def __init__ (self,letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-8) ')
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('[- | -]Invalid square! Try again.[- | -]')

        return val
        

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        if len(game.availableMoves()) == 9:
            square = random.choice(game.availableMoves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        maxplayer = self.letter
        otherPlayer = 'O' if player == 'X' else 'X'

        if state.currentWinner == otherPlayer:
            return {
                'position': None,
                'score': 1 * (state.numEmptySquares() + 1) if otherPlayer == maxplayer else -1 * (state.numEmptySquares() + 1)
                }
        elif not state.emptySquares():
            return {
                'position': None,
                'score' : 0
                }

        if player == maxplayer:
            best = {
                'position': None,
                'score': -math.inf
                }
        else:
            best = {
                'position': None,
                'score': math.inf
                }

        for possibleMoves in state.availableMoves():
            state.makeMove(possibleMoves, player)

            simScore = self.minimax(state, otherPlayer)

            state.board[possibleMoves] = ' '
            state.currentWinner = None
            simScore['position'] = possibleMoves

            if player == maxplayer:
                if simScore['score'] > best['score']:
                    best = simScore

            else:
                if simScore['score'] < best['score']:
                    best = simScore
        
        
        return best

    
