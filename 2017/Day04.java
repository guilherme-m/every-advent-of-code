import java.util.*;
import java.nio.file.*;
import java.io.IOException;

public class Day04 implements Day{
    
    public void run(){
        partOne();
        partTwo();
    }

    private List<String> readInput(){

        Path p = Path.of("inputs/Day04.txt");

        try{
            List<String> lines = Files.readAllLines(p);
            return lines;
        } catch(IOException ioe){

            throw new RuntimeException(ioe);
        }        

    }

    private void partOne(){

        var lines = readInput();

        int validPassphrases = (int) lines
            .stream()
            .map(s -> List.of(s.split("\\s+")))
            .filter(l -> isValidPassphrase(l))
            .count();

        System.out.println("Part 1: " + validPassphrases);


    }


    private void partTwo(){

        var lines = readInput();

        int validPassphrases = (int) lines
            .stream()
            .map(s -> List.of(s.split("\\s+")))
            .filter(l -> !containsAnagram(l))
            .count();

        System.out.println("Part 2: " + validPassphrases);


    }

    private boolean isValidPassphrase(List<String> l){

        return l.size() == l.stream().distinct().count();

    }

    private boolean containsAnagram(List<String> l){

        for(int i = 0; i < l.size() - 1; i++){

            for(int j = i + 1; j < l.size(); j++){


                boolean isAnagram = Arrays.mismatch(
                    l.get(i).chars().sorted().toArray(),
                    l.get(j).chars().sorted().toArray()
                ) == -1;


                if(isAnagram) return true;
            }

        }

        return false;

    }

}
