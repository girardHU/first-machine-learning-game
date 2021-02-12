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
`--step-nb-moves`*: The Number by which you want to increase the size of the movepool*  
`--tickrate`*: The speed of the move tickrate (in milliseconds)*  


### TODOS
Add a CLI argument to fasten the game (lower tick rate and increase Players's movement speed)
Fix Bouncing to allow bouncing off walls (and obstacles maybe)
Display only the best player

### FIXES
Sometimes, best player seems to be broken
Allow resizing of the screen (by setting relative sizes)
When the nb of moves is high, it freezes on the first ones and does not play them
Regroup loops on players (in Population) (may fix the problem above)

STARTING_NB_MOVES = 5
STEP_NB_MOVES = 5