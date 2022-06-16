"""
Name(s): Jesse Uppal and Emma Baltrusaitis
Name of Project: Choose your adventure: Peppa Pig
"""

def start():
  print("\nWelcome to Peppa Pig World!!! \U0001F973\U0001F43D \nGet ready to live a day full of fun and surprises! To start, pick a name!")
  choice = input("\nEnter A for Allie Alligator \U0001F40A or B for Bob Baboon \U0001F412: ")
  if choice == "A":
    doorA()
  elif choice == "B":
    doorB()

def doorA():
  print("\nHi Allie Alligator! Do you want to befriend Peppa Pig \U0001F437 or Danny Dog \U0001F436?")
  choice = input("Enter P for Peppa Pig, D for Danny Dog, or X to go back to the start: ")
  if choice == "P":
    pancakes()
  elif choice == "D":
    sailing()
  elif choice == "X":
    start()

def doorB():
  print("\nHi Bob Baboon! Do you want to befriend George Pig \U0001F416 or Suzie Sheep \U0001F411 ?")
  choice = input("Enter G for George Pig, S for Suzie Sheep, or X to go back to the start: ")
  if choice == "G":
    playdate()
  elif choice == "S":
    party()
  elif choice == "X":
    start()               

def pancakes():
  print("\nAllie, you chose to make pancakes \U0001F95E with Peppa and Daddy Pig! Do you eat them with spinach or ice cream?")
  choice = input("Enter N for spinach \U0001F96C, I for ice cream \U0001F366, or X to go back to start: ")
  if choice == "N": 
    print("\nOopsie daisy, wrong choice. No one eats spinach with pancakes! \U0001F92E Make a yummier decision...") 
    pancakes()
  elif choice == "I":
    night()
  elif choice == "X":
    start()

def sailing():
  print("\nTime to go sailing with Danny Dog and Granddad Dog! The lake is full of endless possibilities. Do you want to explore sharks \U0001F988 or frogs \U0001F438?")
  choice = input("Enter K for sharks, F for frogs, or X to go back to the start: ")
  if choice == "K":
    print("\nUh oh spagetti-o! Sharks are way too dangerous for two silly children. \U0001F6AB Choose again Allie!")
    sailing()
  elif choice == "F":
    night()
  elif choice == "X":
    start()

def playdate():
  print("\nYayyy! You get to have a playdate with the one and only George Pig! Do you want to play with dinosaurs \U0001F996, play outside in the mud \U0001FAB1 \U0001F7E4, or bother George's sister Peppa \U0001F437?")
  choice = input("Enter O for dinos, M for mud, Y for bothering Peppa, or X to go back to the start: ")
  if choice == "O":
    night()
  elif choice == "M":
    night()
  elif choice == "Y":
    print("\nBob Baboon! That is absolutely not okay. \U0001F446 You need to be respectful to your friends. Choose again...")
    playdate()
  elif choice == "X":
    start()

def party():
  print("\nWoohoo! Suzie taught you how to whistle! Now, you're both dancing the Head Shoulders Knees and Toes dance! What music do you want to listen to? Blues music \U0001F399, rap music \U0001F4B8, or pop music \U0001F3B8?")
  choice = input("Enter L for blues, R for rap, E for pop, or X to go back to the start: ")
  if choice == "L": 
    night()
  elif choice == "R":
    print("\nSilly you! You can't dance to rap music! Rap is too grown up for you children anyways. Tsk tsk tsk. Choose again, more wisely perhaps \U0001F914.")
    party()
  elif choice == "E":
    night()
  elif choice == "X":
    start()

def night():
  print("\nGreat choices! \U0001F44F You've had a fun day in Peppa Pig's adventure world. Sleep well \U0001F634 so you'll do swell in school with Miss Gazelle!")

start()   