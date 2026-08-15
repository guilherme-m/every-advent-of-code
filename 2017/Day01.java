import java.nio.file.*;
import java.io.IOException;

public class Day01{

    public static void run(){
        partOne();
        partTwo();
    }

    public static void partOne(){

        String lines;

        try{
            lines = Files.readString(Path.of("inputs/Day01.txt"));
        } catch(IOException ioe){
            ioe.printStackTrace();
            return;
        }

        int sum = 0;

        for(int i = 0; i < lines.length(); i++){

            if(lines.charAt(i) == lines.charAt((i + 1) % lines.length())){
                sum += Character.getNumericValue(lines.charAt(i));
            }

        }
        
        System.out.println("Part 1: " + sum);

    }

    public static void partTwo(){

        String lines;

        try{
            lines = Files.readString(Path.of("inputs/Day01.txt"));
        } catch(IOException ioe){
            ioe.printStackTrace();
            return;
        }

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



}
