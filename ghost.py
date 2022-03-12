#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist
  
def askInput(player):
  while True: 
    letter = input("Player " + str(player) + " how about a letter? ")
    if letter.isalpha() and len(letter) == 1:
      return letter.capitalize()
    else: 
      print("Invalid Input! Please enter a letter.")

def checkState(string, words):
  for word in words:
    if word.startswith(string):
      return True 
  return False

def checkWord(string, words):
  tempStr = string
  while len(tempStr) >= 3:
    for word in words:
      if word == tempStr:
        return False
    tempStr = tempStr[1:]
  return True

def main():
  words = load_wordlist()
  print(f"{len(words)} words loaded.")
  print("Welcome to Ghost!")
  gameState = True
  player = 0
  gameStr = ''
  while gameState: 
    if player == 1:
      player = 2
    else:
      player = 1
    letter = askInput(player)
    gameStr = gameStr + letter
    print(f"Player {player} chose {letter}, giving the fragment {gameStr}.")
    if checkState(letter, words) == True:
      gameState = checkWord(gameStr, words)
  print(str(player) + " just lost!")
main()
