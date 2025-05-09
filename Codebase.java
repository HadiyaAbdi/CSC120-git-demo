public class Codebase {

// This is the codebase for all the classes in the game


// Main game class
public class MysteryGame {
    private Player player;
    private List<Room> rooms;
    private boolean basementUnlocked;
    private Scanner s;


    public static void main(String[] args);
    public void start();
}


// Abstract base class for all rooms
public abstract class Room {
    private String name;
    private boolean challengeCompleted;
    public Room(String name);
    public abstract void explore(Player player);
}


// Subclasses for specific rooms
public class FirstFloor extends Room {
    public void explore(Player player);
}


public class SecondFloor extends Room {
    public void explore(Player player);
}


public class Basement extends Room {
    public void explore(Player player);
}


// Represents the player
public class Player {
    private List<Item> inventory;
    private List<Clue> clues;


    public void collectItem(Item item);
    public void collectClue(Clue clue);
    public void loseClue(String floorName);
    public void showClue();
    public boolean hasKeyClues(int required);
    public boolean hasBasementKey();
    public void addItem(String itemName);
    public void removeFloorClues(String string) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'removeFloorClues'");
    }
}


// Clues that help solve the mystery
public class Clue {
    private String text;
    private boolean keyClue;
    private boolean isFound;
    
    public String getText();
    public boolean isKeyClue();
}
    
}
