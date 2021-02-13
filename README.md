# My First IA using Machine Learning

### If you want to test it
```sh
cd first-machine-learning-game
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 Game.py --level=1
```

### CLI Arguments
`--level`*: From 0 to 3, choose level on which you want to run the simulation*  
`--nb-players`*: Defines the number of players*  
`--player-radius`*: The Radius of the players*  
`--nb-moves`*: Defines the number of turns for each generation*  
`--nb-new-moves`*: The Number by which you want to increase the size of the movepool*  
`--gap-new-moves`*: The Number of generation between two nb moves increases*  
`--tickrate`*: The speed of the move tickrate (in milliseconds)*  


### TODOS
Add a CLI argument to fasten the game (lower tick rate and increase Players's movement speed)  
Fix Bouncing to allow bouncing off walls (and obstacles maybe)  
Display only the best player  
Create a Gamemode where the game pass to the next level by itself (and maybe run each level with optimized ressources)  
Create pre-thought CLI command for each level  
Defin Brain's MAX_STEP and SPEED_VARY dynamically  

### FIXES
Sometimes, best player seems to be broken  
Allow resizing of the screen (by setting relative sizes)  
When the nb of moves is high, it freezes on the first ones and does not play them  
Regroup loops on players (in Population) (may fix the problem above)  
