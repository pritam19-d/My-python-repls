print('''
                                        /\
                                        )(
                                       /{}\
                                      (    )
                         ,----------_____....----.--------,
                _____.....-----~~~~~             |_______/ `
               |                                 |      /  |
               |          H E L L O              |     /
               |                                  |   /   /
                |                                 | _/   /
                |            W O R L D            |,'|~~
               ,|                                ,'  |
             ,'_|_____________________________:,' /) |.
             |  \    \                /    /  |  (/  |_. .
             |   \    \     {}       /    /   |    .' .  .
          . '|    \    \            / _  /    |    ,   .  .
         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
''')
print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
starting_input = input("Here we're staring the game, please choose your path, 'left' or 'right'").lower();
if starting_input == "left":
  swim_wait = input("Do you wanna swim or wait for a boat? please choose one 'swim' or 'wait'").lower();
  if swim_wait == "wait":
    door = input("There are three dores in the cabin, which one you wanna choose? 'Red' or 'Yellow' or 'Blue'").lower();
    if door == "red":
      print("Oh Noooo!! There is fire Go away else you'll burn out...\n**Game Over**");
    elif door == "yellow":
      print("Hurreyyy!! You find the treasure at last...\n**You Win**");
    elif door == "blue":
      print("Oh Noooo!! There was a beast inside and it jumped over you...\n**Game Over**");
    else:
      print("Sorry! there are no such option available.\n**Game Over**");
  else:
    print("You've been attacked by trout. \n**Game over**")
else:
  print("Ah! there was a hole in the dark, and you fall into that. \n **Game Over**")

