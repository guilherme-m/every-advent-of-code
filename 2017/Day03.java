import java.io.*;
import java.util.*;

public class Day03 implements Day{
    public void run(){
        partOne();
        partTwo();
    }

    private int readInput(){
        File f = new File("inputs/Day03.txt");
        
        try(var reader = new BufferedReader(new FileReader(f))){

            String s = reader.readLine();
            
            return Integer.parseInt(s);

        } catch(IOException ioe){

            throw new RuntimeException();
        }
        
        
    }

    private void partOne(){
        int input = readInput();

        Board board = new Board();

        board.move(input - 1);

        System.out.println("Part 1: " +
            board.distanceFromOrigin()
        );
    }
    
    public void partTwo(){

        int input = readInput();

        int positionValue;

        Board board = new Board();

        do {
            board.move(1);
        } while((positionValue = board.getPositionValue()) <= input);



        System.out.println("Part 2: " + positionValue);
        

    }
}

class Board{

    private Point edges, position;
    private Direction nextDirection;
    private Map<Point, Integer> positionValue;

    public Board(){
        edges = new Point(1, 1);
        
        position = new Point(0, 0);

        nextDirection = Direction.RIGHT;

        positionValue = new HashMap<>();

        positionValue.put(position, 1);

    }

    public void move(int x){

        for(int i = 0; i < x; i++){

            if(position.add(nextDirection.direction).exceeds(edges)){
                changeDirection();
            }

            position = position.add(nextDirection.direction);

            storePositionValue();

        }


    }

    public Point getPosition(){return this.position;}


    private void storePositionValue(){

        int sum = positionValue.getOrDefault(position.add(new Point(1, 0)), 0) +
            positionValue.getOrDefault(position.add(new Point(0, 1)), 0) +
            positionValue.getOrDefault(position.add(new Point(-1, 0)), 0) +
            positionValue.getOrDefault(position.add(new Point(0, -1)), 0) +
            positionValue.getOrDefault(position.add(new Point(1, 1)), 0) +
            positionValue.getOrDefault(position.add(new Point(1, -1)), 0) +
            positionValue.getOrDefault(position.add(new Point(-1, 1)), 0) +
            positionValue.getOrDefault(position.add(new Point(-1, -1)), 0);
            


        positionValue.put(position, sum);

    }

    public int getPositionValue(){

        return positionValue.get(position);

    }

    private void changeDirection(){

        switch(nextDirection){
            case UP -> nextDirection = Direction.LEFT;
            case LEFT -> {
                edges = edges.add(new Point(1, 0));
                nextDirection = Direction.DOWN;
            }
            case RIGHT -> nextDirection = Direction.UP; 
            case DOWN -> {
                edges = edges.add(new Point(0, 1));
                nextDirection = Direction.RIGHT;
            }
        }

    }

    public int distanceFromOrigin(){

        return Math.abs(position.x()) + Math.abs(position.y());

    }

}

record Point(int x, int y){
    Point add(Point p){
        return new Point(this.x + p.x(), this.y + p.y());
    }

    public boolean exceeds(Point p){
        return Math.abs(this.x) > Math.abs(p.x()) ||
            Math.abs(this.y) > Math.abs(p.y());
    }
}

enum Direction{

    UP(new Point(0, 1)),
    LEFT(new Point(-1, 0)),
    RIGHT(new Point(1, 0)),
    DOWN(new Point(0, -1));
    
    final Point direction;
    
    Direction(Point p){
        this.direction = p;
    }
}
