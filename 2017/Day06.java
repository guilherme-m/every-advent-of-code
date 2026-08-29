
import java.nio.file.*;
import java.io.IOException;
import java.io.FileReader;

import java.util.*;


public class Day06 implements Day {
    public void run(){

        partOne();
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

    public void partOne(){

        var banks = new Banks(readInput());

        int count = banks.redistributionsUntilSameConfiguration();

        System.out.println(count);
    }

}

class Banks{

    private List<Integer> banks;

    private Set<List<Integer>> configurations;

    public Banks(List<Integer> banks){

        this.banks = banks;
        this.configurations = new HashSet<>();

        this.configurations.add(
            this.banks
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
        System.out.println(banks);

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

                configurations.add(banks);
            }
            
        }
        return redistributionsCount;

    }

    public String toString(){return "" + banks;}



}