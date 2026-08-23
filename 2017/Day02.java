import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

import java.util.stream.*;

import java.util.*;


public class Day02{

    public static void run(){

        partOne();
        partTwo();
    
    }

    private static List<String> readInput(){

        try{

            return Files.readAllLines(Path.of("inputs/Day02.txt"));

        } catch (IOException ioe){

            throw new RuntimeException("Erro na leitura do arquivo", ioe);

        }
    }

    static private void partOne(){

        var lines = readInput();

        var sum = lines.stream()
            .map(l -> {
                return Stream.of(l.split("[^0-9]+")).map(Integer::valueOf).toList();
            })
            .map(l -> {
                l = new ArrayList<>(l);
                l.sort(Integer::compare);
                return l.get(l.size() - 1) - l.get(0);
            })
            .reduce(0, (x1,x2) -> x1 + x2);


        
        System.out.println("Part 1: %s".formatted(sum));
    }

    static private void partTwo(){

        var lines = readInput();

        var divisors = lines.stream()
            .map(l -> {
                return Stream.of(l.split("[^0-9]+")).map(Integer::valueOf).toList();
            })
            .mapToInt(l -> getDivisors(l))
            .sum();

        System.out.println("Part 2: %s".formatted(divisors));
    }    

    private static Integer getDivisors(List<Integer> l){
        int sum = 0;
        
        for(int i = 0; i < l.size(); i++){

            for(int j = 0; j < l.size(); j++){
                int numerator, denominator;

                numerator = l.get(i);
                denominator = l.get(j);

                if(i == j || numerator < denominator || numerator % denominator != 0){
                    continue;
                }

                sum += numerator / denominator;
            }

        }

        return sum;
    }


}