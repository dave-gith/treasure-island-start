print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
cross_road = input("You're on a mission to find the treasure and you find yourself at a crossroad, which way will you go? 'left' or 'right':\n").lower()

if cross_road == "left":
  river = input("You end up at a river, type 'wait' to wait for a boat or 'swim' to swim across?:\n").lower()
  if river == "wait":
    abandoned_house = input("You end up at an abandoned house which has three doors leading to rooms, 'Red', 'Blue and 'Yellow' which room will you like to go? Type 'red' 'blue' or 'yellow.':\n").lower()
    if abandoned_house == "blue":
      print("You were eaten by beasts🐲. Game over!")
    elif abandoned_house == "yellow":
      print("You found the treasure💰, you win!!")
    elif abandoned_house == "red":
      print("You got into a room full of fire🔥. Game over!")
    else:
      print("You didnt choose the right room. Game over!")
  else:
    print("You got eaten by crocodiles🐊. Game over!")
else:
  print("You got caught in pirate traps. Game over!")



