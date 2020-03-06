def init_game():
  game = {}
  game['game_over'] = False
  game['no_space'] = False
  game['board'] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  game['current_player'] = ''
  game['players'] = {'player1': {'symbol':'', 'name':'', 'played': {'onboard':(), 'num':''}}, 'player2': {'symbol':'', 'name':'', 'played':{'onboard':(), 'num':''}}}
  return game

def print_board(board):
  clear_screen()
  print('>>>>positions<<<<<'+'\tI\t'+'=====THE GAME=====')
  print('    '+str(1)+' | '+str(2)+' | '+str(3)+'    '+'\tI\t'+'    '+board[0][0]+' | '+board[0][1]+' | '+board[0][2]+'   ')
  print('   ---'+'-'+'---'+'-'+'---   '+'\tI\t'+'   ---'+'-'+'---'+'-'+'---   ')
  print('    '+str(4)+' | '+str(5)+' | '+str(6)+'    '+'\tI\t'+'    '+board[1][0]+' | '+board[1][1]+' | '+board[1][2]+'   ')
  print('   ---'+'-'+'---'+'-'+'---   '+'\tI\t'+'   ---'+'-'+'---'+'-'+'---   ')
  print('    '+str(7)+' | '+str(8)+' | '+str(9)+'    '+'\tI\t'+'    '+board[2][0]+' | '+board[2][1]+' | '+board[2][2]+'   ')
  print('>>>>positions<<<<<'+'\tI\t'+'==================')
  
  print('')


def clear_screen():
  pass #print('\n'*100)

def read_players(players):
  symbols = ['x','o']
  player_name = input("Please type the Player1's name:")
  players['player1']['name'] = player_name
  player_symbol = input(player_name+" do you want to be X or O?")
  while(player_symbol.lower() not in symbols):
    player_symbol = input("Invalid input, please select 'X' or 'O'")
  players['player1']['name'] = player_name
  players['player1']['symbol'] = player_symbol.lower()
  
  player_name = input("Please type the Player2's name:")
  players['player2']['name'] = player_name
  if player_symbol == 'x':
    player_symbol = 'o'
  else:
    player_symbol = 'x'
  print(player_name+' will be '+player_symbol.upper())
  players['player2']['symbol'] = player_symbol.lower()

def read_turn(game):
  current_player = game['players'][game['current_player']]
  valid_input = False
  while(not valid_input):
    player_input = input(current_player['name']+", please select a valid position 1 and 9 which is empty:")
    if player_input  in ['1','2','3','4','5','6','7','8','9']:
      board_position = map_input_to_board(player_input)
      if game['board'][board_position[0]][board_position[1]] == ' ':
        game['board'][board_position[0]][board_position[1]] = current_player['symbol']
        current_player['played']['onboard'] = board_position
        current_player['played']['num'] = player_input
        valid_input = True
  print(game)


def map_input_to_board(player_input):
  n = 0
  for i in range(0,3):
    for j in range(0,3):
      n+=1
      if str(n) == player_input:
        return (i,j)

def select_current_player(game):
  if game['current_player'] == 'player1':
    game['current_player'] = 'player2'
  elif game['current_player'] == 'player2':
    game['current_player'] = 'player1'
  elif game['current_player'] == '':
    game['current_player'] = 'player1'

def check_game_over(game):
  current_player = game['players'][game['current_player']]
  symbol = current_player['symbol']
  position = current_player['played']['onboard']
  l = position[0]
  c = position[1]
  board = game['board']
  line = 0
  col = 0
  diag = 0
  has_space = False
  for i in range(0,3):
    if(board[l][i] == symbol):
      line+=1
    if(board[i][c] == symbol):
      col+=1
    if((l == c and board[i][i] == symbol) or ((position == (2,0) or position == (2,0)) and board[i][2-i] == symbol )):
      diag+=1
    if(' ' in board[i]):
      has_space = True
  print(line)
  print(col)
  print(diag)
  if line == 3 or col == 3 or diag == 3:
    game['game_over'] = True
  if not has_space:
    game['no_space'] = True


def check_new_game(game):
  if game['game_over']:
    print_board(game['board'])
    print(game['players'][game['current_player']]['name']+" won!!!")
    read_play_again()
  if game['no_space']:
    print_board(game['board'])
    print(" GAME OVER ")
    read_play_again()

def read_play_again():
  new_game = ''
  while(new_game.lower() not in ['y','n']):
    new_game = input("Play another round? (y/n)")
  if new_game.lower() == 'y':
    reset_game(game)
  else:
    print("Thanks for playing! :)")
    game['game_over'] = True

def reset_game(game):
  game['game_over'] = False
  game['no_space'] = False
  game['board'] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

game = init_game()
read_players(game['players'])
playing = True
while(playing):
  print_board(game['board'])
  select_current_player(game)
  read_turn(game)
  map_input_to_board(game)
  check_game_over(game)
  check_new_game(game)
  playing = not game['game_over']
