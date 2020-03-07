import random

def init_board():
  board = [' ']*10
  board[0] = {'X':{'name':''}, 'O':{'name':''}, 'turn':'', 'winner':False, 'draw':False, 'playing':True}
  return board

def clear_screen():
  print('\n'*100)

def print_board(board):
  clear_screen()
  print('>>>>positions<<<<<'+'\tI\t'+'=====THE GAME=====')
  print('    '+str(1)+' | '+str(2)+' | '+str(3)+'    '+'\tI\t'+'    '+board[1]+' | '+board[2]+' | '+board[3]+'   ')
  print('   ---'+'-'+'---'+'-'+'---   '+'\tI\t'+'   ---'+'-'+'---'+'-'+'---   ')
  print('    '+str(4)+' | '+str(5)+' | '+str(6)+'    '+'\tI\t'+'    '+board[4]+' | '+board[5]+' | '+board[6]+'   ')
  print('   ---'+'-'+'---'+'-'+'---   '+'\tI\t'+'   ---'+'-'+'---'+'-'+'---   ')
  print('    '+str(7)+' | '+str(8)+' | '+str(9)+'    '+'\tI\t'+'    '+board[7]+' | '+board[8]+' | '+board[9]+'   ')
  print('>>>>positions<<<<<'+'\tI\t'+'==================')
  print('')

def read_players(board):
  '''
  Read the players name and marker to position 0 of the board
  '''
  player_name = input("Please type the Player1's name:")
  player_symbol = ''
  while player_symbol != 'X' and player_symbol != 'O' :
    player_symbol = input(player_name+", please select X or O: (X / O)").upper()
  board[0][player_symbol]['name'] = player_name
  
  player_name = input("Please type the Player2's name:")
  if player_symbol == 'X':
    player_symbol = 'O'
  else:
    player_symbol = 'X'
  board[0][player_symbol]['name'] = player_name

def choose_player_turn(board):
  current_turn = board[0]['turn']
  if current_turn == 'X':
    current_turn = 'O'
  elif current_turn == 'O':
    current_turn = 'X'
  elif current_turn == '':
    if random.randint(1,2) == 1:
      current_turn = 'X'
    else:
      current_turn = 'O'
  board[0]['turn'] = current_turn

def read_player_turn(board):
  current_turn = board[0]['turn']
  invalid_input = True
  while invalid_input:
    player_input = input(board[0][current_turn]['name']+", please select an empty position: (1 ~ 9):")
    if player_input in ['1','2','3','4','5','6','7','8','9'] and board[int(player_input)] == ' ':
      invalid_input = False
      board[int(player_input)] = current_turn

def check_result(board):
  print(board)
  if board[1] == board[2] == board[3] == board[0]['turn'] or \
     board[4] == board[5] == board[6] == board[0]['turn'] or \
     board[7] == board[8] == board[9] == board[0]['turn'] or \
     board[1] == board[4] == board[7] == board[0]['turn'] or \
     board[2] == board[5] == board[8] == board[0]['turn'] or \
     board[3] == board[6] == board[9] == board[0]['turn'] or \
     board[1] == board[5] == board[9] == board[0]['turn'] or \
     board[3] == board[5] == board[7] == board[0]['turn']:
    board[0]['winner'] = True
  
  if not board[0]['winner']:
    if ' ' not in board[1:]:
      board[0]['draw'] = True

  if board[0]['winner']:
    print_board(board)
    print("\t\t\t\t"+board[0][board[0]['turn']]['name']+" won!!!")
  if board[0]['draw']:
    print_board(board)
    print("\t\t\t\tGAME OVER")

def play_another(board):
  if board[0]['winner'] or  board[0]['draw']:
    new_game = ''
    while(new_game not in ['y','n']):
      new_game = input("Do you want to play again? (y/n)").lower()
    if new_game == 'y':
      reset_board(board)
    else:
      board[0]['playing'] = False
      print('Bye.')
      print('Thank you for playing!')
      print(':)')

def reset_board(board):
  for i in range(1,10):
    board[i] = ' '

  board[0]['winner'] = False
  board[0]['draw'] = False
  #board[0]['turn'] = ''
  



board = init_board()
read_players(board)

while board[0]['playing']:
  print_board(board)
  choose_player_turn(board)
  read_player_turn(board)
  check_result(board)
  play_another(board)