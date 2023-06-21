from game_data import data
import random
from art import logo, vs





def random_data():
    """gives random data from game dictionary"""
    return random.choice(data)



def compare(dataA,dataB):
    """gives true or false for our guess value"""
    if dataA["follower_count"] > dataB['follower_count'] and user_choice=="A":
      return True
    elif dataA["follower_count"] < dataB['follower_count'] and user_choice=="B":
      return True
    else:
      return False
  
def score():
    global total_score
    if compare(dataA, dataB)== True:
      total_score = total_score +1
      return True
    else:
      print(f"Wrong guess.Your total_score is {total_score}")
      return False

dataA = random_data()
total_score = 0
dataB = random_data()
game_run =True

while game_run:
  print(logo)
  print(f"Compare A:{dataA['name']}, {dataA['description']}, {dataA['country']}")
  print(vs)
  print(f"Compare B:{dataB['name']}, {dataB['description']}, {dataB['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B' ")
  # clear()
  game_run=score()
  dataA = dataB
  dataB = random_data()