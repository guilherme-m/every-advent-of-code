
import java.nio.file.*;
import java.io.IOException;
import java.io.FileReader;

import java.util.*;


public class Day06 implements Day {
    public void run(){

        partOne();
        partTwo();
    }

    private List<Integer> readInput(){

        Path p = Path.of("inputs/Day06.txt");
        try{
            String s = Files.lines(p).limit(1).findFirst().get();
            
            String[] sArr =  s.split("[^0-9]+");
            
            List<Integer> nums = new ArrayList<>();

            for(int i = 0; i < sArr.length; i++){

                nums.add(Integer.parseInt(sArr[i]));

            }
            
            return nums;

        } catch(IOException ioe){
            throw new RuntimeException(ioe);
        }

    }

    private void partOne(){

        var banks = new Banks(readInput());

        int count = banks.redistributionsUntilSameConfiguration();

        System.out.println("Part 1: " + count);
    }

    private void partTwo(){

        var banks = new Banks(readInput());

        var count = banks.redistributionsCountFromSameConfiguration();

        System.out.println("Part 2: " + count);

    }

}

class Banks{

    private List<Integer> banks;

    private Set<List<Integer>> configurations;

    public Banks(List<Integer> banks){

        this.banks = banks;
        this.configurations = new HashSet<>();

        this.configurations.add(
            List.copyOf(this.banks)
        );
    }

    private void redistribute(){

        int max = banks.stream().mapToInt(x -> x).max().getAsInt();

        int indexOfMax = banks.indexOf(max);

        banks.set(indexOfMax, 0);

        while(max-- > 0){

            indexOfMax = (indexOfMax + 1) % banks.size();

            banks.set(indexOfMax, 
                banks.get(indexOfMax) + 1
            );

        }
        

    }

    public int redistributionsUntilSameConfiguration(){

        boolean alreadyHasConfig = false;

        int redistributionsCount = 0;

        while(!alreadyHasConfig){

            redistribute();
            redistributionsCount++;
            if(configurations.contains(banks)){
                alreadyHasConfig = true;
            } else{

                configurations.add(List.copyOf(banks));
            }
            
        }
        return redistributionsCount;

    }

    public int redistributionsCountFromSameConfiguration(){

        boolean alreadyHasConfig = false;

        int redistributionsCount = 0;

        Map<List<Integer>, Integer> map = new HashMap<>();

        map.put(
            List.copyOf(banks), 
            redistributionsCount
        );


        while(!alreadyHasConfig){

            redistribute();
            redistributionsCount++;
            if(map.containsKey(banks)){
                alreadyHasConfig = true;
            } 

            map.putIfAbsent(
                List.copyOf(banks),
                redistributionsCount
            );
            
        }
        return redistributionsCount - map.get(banks);

    }

    public String toString(){return "" + banks;}



}