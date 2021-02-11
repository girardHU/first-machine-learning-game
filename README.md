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
`--nb_players`*: Defines the number of players*  
`--nb_turns`*: Defines the number of turns for each generation*  


### TODOS
Add a CLI argument to fasten the game (lower tick rate and increase Players's movement speed)

### FIXES
Sometimes, best player seems to be broken