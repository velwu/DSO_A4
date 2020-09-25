# DSO_A4
This is a group assignment repo for IS 597 DSO FA20 A4 - Virtual Matchbox Engine

GitHub link: https://github.com/velwu/DSO_A4/tree/A4_final

### Team members: (Name / GitHub ID / NetID)
Samantha Walkow / samwalkow / swalkow2

Rajath John / jrajath94 / rajathj2

Vel (Tien-Yun) Wu / velwu / tienyun2

## Files decripstion:
### Primary files:
**- 1. TTT_vel_rajath_samantha.py**
  - This is our main program. All finalized codes and primary functions are found here. Run the 2nd file (TTT_run_the_program) to see the effects

**- 2. TTT_run_the_program.py**
  - This executes the main program (TTT_vel_rajath_samantha).
    
**- 3. Game_Memory.pickle**
  - A file created by the main program. It is essentially a storage for learning outcomes.

**- 4. records.txt**
  - Also created by the main program. This is a track record of every 10,000 games played. It can be seen that the disadvanted player ("O", as it plays second) improves overtime and turns the win-loss around by the end of the 30-minute training through 1,000,000 games.
    
### Supplementary files:
**- 1. FirstDesign.py**
  - This is where an alternate approach of storing learning outcomes as node classes and trees was experimented with. We ultimately left this approach behind and chose to go with the hashmap/dictionary approach.
    
**- 2. TicTacToe.py**
  - This was largely a clone of the main program to try out different weight adjustments between win-loss rewards/punishments and became a proper place for the file-dumping functions to develop.


![Snapshot Image 1](https://github.com/velwu/DSO_A4/blob/master/TTT_image_for_fun.jpg)
