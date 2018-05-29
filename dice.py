import random

min = 1
max = 6
roll_again = "yes"

random.randint(min, max)

while roll_again == 'yes' or roll_again == 'y':
  print("Rolling the dice...")
  print()
  print(random.randint(min, max))
  print(random.randint(min, max))
  print()
  roll_again == input("Want to roll again?")
