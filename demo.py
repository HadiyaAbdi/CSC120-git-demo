Hadiya Cabdi  
Updated Architecture (with Progress Annotations)  
                          |  MysteryGame  |  <- Welcome prompt and game flow start


                          +--------------------------+
                          | - player                 |
                          | - rooms                  |  <-- List<Room>, each has challenge
                          | - s (Scanner)            |
                          | - basementUnlocked       |  <-- ** Set to true when player meets clue requirement (Progress Gate)
                          +--------------------------+
                          | + start()                |  <-- () Controls game flow: room exploring, gate checks
                          +--------------------------+
                                   |
                            has-a  |
                                   v
                          +--------------------------+
                          |         Player           |  <-- Aggregates both items and clues
                          +--------------------------+
                          | - inventory              |
                          | - clues                  |  <-- + Clues are required to unlock basement (Progress Resource)
                          +--------------------------+
                          | + collectItem()          |
                          | + collectClue()          |
                          | + hasKeyClues()          |  <-- () Returns true if enough key clues (Progress Gate)
                          | + hasBasementKey()       |
                          | + showClue()             |
                          | + loseClue()             |
                          +--------------------------+
                                   |
         +-------------------------+--------------------------+
         |                                                    |
     +-------------+                                    +-------------+
     |   Item      |                                    |   Clue      |
     +-------------+                                    +-------------+
     | - name      |                                    | - text      |
     | - desc      |                                    | - isKey     |  <-- () Determines if clue counts for progress
     +-------------+                                    +-------------+


                                ^  
                                | (abstract)
                          +--------------------------+
                          |          Room            |  
                          +--------------------------+
                          | - name                   |
                          | - challengeCompleted     |  <-- ** Becomes true after solving challenge (Progress Flag)
                          +--------------------------+
                          | + explore(Player)        |  <-- () Abstract method - subclasses define room interaction
                          +--------------------------+
                                ^
         +----------------------+----------------------+----------------------+
         |                      |                      |
 +------------------+  +------------------+     +------------------+
 |   FirstFloor     |  |  SecondFloor     |     |     Basement     |
 +------------------+  +------------------+     +------------------+
 | + explore()      |  | + explore()      |     | + explore()      |
 | - riddle logic   |  | - riddle logic   |     | - final action   |
 | - clues given **  |  | - clues given **  |     | - end message () |
 +------------------+  +------------------+     +------------------+

Legend:
** = Progress Gate / Condition  
() = Progress Trigger / Event  
+ = Resource used for progress  




