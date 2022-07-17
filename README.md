# the-Ball-game
Its my first completed game, with fully object oriented code.

The purpose of developing this project was to test and train my skills in object oriented programming
and expand my knowledge of pygame module.

### ABOUT THE GAME ### 
The game was heavily inspired by popular type of 'Brick Breaker' games. Winning condition
is easy you have to break all bricks which display on screen. You can move the platform using 'A' and 'D' keys to
bounce flying ball, if the last ball falls down from the screen - you lost.
Also I added ability to shoot laser from the middle of the platform (if you have enough ammo to do that), 
which can be done by pressing 'SPACE' (This feature was inspired by 'Space Invaders' game). 

Color of the brick is NOT a random thing. Every color is assigned to a number of hit points which are required to 
finally break the brick:

GREEN -- 1 hit point

BLUE -- 2 hit points

ORANGE -- 3 hit points

PURPLE -- +4 hit points

When brick breaks there is a chance for it to drop power-up / power-down. Effect of the drop is applied to game if 
you 'catch' it by platform. 

So far I implemented 3 power-ups ('3x number of balls', 'length (platform) up', 'add 1 ammon') and 
1 power-down ('length (platform) down').
Effects of these drops are pretty well described by their names, but if you want to experience it on your own 
just download this repository and to run it type 'python main.py' in terminal (also make sure you have installed pygame module).

Feel free to report directly to me any bugs you encounter (email in Bio). :3  
