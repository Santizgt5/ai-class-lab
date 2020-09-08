import re
import random
import numpy as np

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None
    self.filaPlayer = ["x","x","x"]
    self.filaMachine = ["o","o","o"]

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    if (self.board.count(None) != 0):
      tableroArray = np.array(self.board)
      tableroMatrix = tableroArray.reshape((3,3))   
      return self.verificarGanadorHorizontal(tableroMatrix) or self.verificarGanadorVertical(tableroMatrix) or self.verificarGanadorDiagonal(tableroMatrix)
    else:
      self.print_result("empate")
      return True

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)


    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    numero = random.randint(0, 8)
    while(self.board[numero]):
      numero = random.randint(0,8)
    self.board[numero] = _MACHINE_SYMBOL

  def format_board(self):
    tablero = ''
    for x in range(0, len(self.board)):
      c = str(self.board[x]) if self.board[x] else ' '
      if (x+1) % 3 == 0:
        tablero = tablero + ' ' + c +'\n'
      else:
        if x == 0:
          tablero = ' '+ c + '   |   '
        else:
          tablero = tablero + ' ' +  c  + '   |   ' 
    return tablero

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self, ganador):
    if (ganador != "empate"):
      print("El ganador fue "+ ganador)
    else:
      print("No hay ganadores, es un empate")
    pass

  def verificarGanadorHorizontal(self, tableroMatrix):
    cadena = str(np.array(self.filaPlayer))
    cadena2 = str(np.array(self.filaMachine))
    fila1 = str(tableroMatrix[0])
    fila2 = str(tableroMatrix[1])
    fila3 = str(tableroMatrix[2])
    if cadena == fila1 or cadena == fila2 or cadena == fila3:
      self.print_result("el jugador")
      return True
    elif cadena2 == fila1 or cadena2 == fila2 or cadena2 == fila3:
      self.print_result("la maquina")
      return True
    else:
      return False

  def verificarGanadorVertical(self, tableroMatrix):
    cols = tableroMatrix.transpose();
    cadena = str(np.array(self.filaPlayer))
    cadena2 = str(np.array(self.filaMachine))
    fila1 = str(cols[0])
    fila2 = str(cols[1])
    fila3 = str(cols[2])
    if cadena == fila1 or cadena == fila2 or cadena == fila3:
      self.print_result("el jugador")
      return True
    elif cadena2 == fila1 or cadena2 == fila2 or cadena2 == fila3:
      self.print_result("la maquina")
      return True
    else:
      return False

  def verificarGanadorDiagonal(self, tableroMatrix):
    diagonal1 = [tableroMatrix[0][0],
                     tableroMatrix[1][1],
                     tableroMatrix[2][2]]

    diagonal2 = [tableroMatrix[0][2],
                     tableroMatrix[1][1],
                     tableroMatrix[2][0]]
    if diagonal1 == self.filaPlayer or diagonal2 == self.filaPlayer:
      self.print_result("el jugador")
      return True
    elif diagonal1 == self.filaMachine or diagonal2 == self.filaMachine:
      self.print_result("la maquina")
      return True
    else:
      return False
        