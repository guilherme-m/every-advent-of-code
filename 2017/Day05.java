import java.nio.file.*;
import java.io.IOException;
import java.util.*;

public class Day05 implements Day{
    public void run(){

        partOne();
        partTwo();
    }

    private int[] readInput(){

        try{

            List<String> l = Files.readAllLines(Path.of("inputs/Day05.txt"));

            return l.stream().mapToInt(x -> Integer.parseInt(x)).toArray();

        } catch(IOException ioe){

            throw new RuntimeException(ioe);

        }


    }


    private void partOne(){

        int[] offsets = readInput();

        int nextStep = 0;

        int count = 0;

        while(nextStep >= 0 && nextStep < offsets.length){

            nextStep += offsets[nextStep]++;

            count++;

        }

        System.out.println("Part 1: " + count);
    }

    private void partTwo(){

        int[] offsets = readInput();

        int nextStep = 0;

        int count = 0;

        while(nextStep >= 0 && nextStep < offsets.length){

            
            int oldStep = nextStep;

            nextStep += offsets[nextStep];
            
            if(offsets[oldStep] >= 3){
                offsets[oldStep] -= 1;
            } else {
                offsets[oldStep] += 1;
            }
            
            count++;

        }

        System.out.println("Part 2: " + count);
    }
}
