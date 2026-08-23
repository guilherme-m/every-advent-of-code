import java.nio.file.*;
import java.io.IOException;
import java.util.stream.*;

public class Day01{

    public static void run(){
        partOne();
        partOneWithIntStream();
        partTwo();
    }

    public static void partOne(){

        String lines = readInput();

        int sum = 0;

        for(int i = 0; i < lines.length(); i++){

            if(lines.charAt(i) == lines.charAt((i + 1) % lines.length())){
                sum += Character.getNumericValue(lines.charAt(i));
            }

        }
        
        System.out.println("Part 1: " + sum);

    }

    public static void partOneWithIntStream(){

        String lines = readInput();

        int sum = IntStream
            .range(0, lines.length())
            .filter(i -> lines.charAt(i) == lines.charAt((i + 1) % lines.length()))
            .map(i -> Character.digit(lines.charAt(i), 10))
            .sum();

        
       System.out.println("Part 1 (with IntStream):" + sum);

    }

    public static void partTwo(){

        String lines = readInput();

        char[] chars = lines.toCharArray();

        int length = chars.length;

        int sum = 0;

        for(int i = 0; i < length; i++){

            if(chars[i] == chars[(i + length/2) % length]){
                sum += Character.getNumericValue(chars[i]);
            }

        }
        
        System.out.println("Part 2: " + sum);

    }

    public static String readInput(){
         try{
            String lines = Files.readString(Path.of("inputs/Day01.txt"));

            return lines;
        } catch(IOException ioe){
            ioe.printStackTrace();
            return "";
        }


    }

}
