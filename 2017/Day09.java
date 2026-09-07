
import java.io.*;

public class Day09 implements Day {
    public void run() {
        partOne();
        partTwo();
    }

    private String readInput() {
        File f = new File("inputs/Day09.txt");

        try (var fr = new FileReader(f);
                var bfr = new BufferedReader(fr)) {

            return bfr.readLine();
        } catch(IOException ioe){
            throw new RuntimeException("erro na leitura", ioe);
        }

    }


    public void partOne(){

        BlockStream bs = new BlockStream(readInput());

        bs.processBlockStream();

        System.out.println(bs.getSum());

    }

    public void partTwo(){

        BlockStream bs = new BlockStream(readInput());

        bs.processBlockStream();

        System.out.println(bs.getGarbageCount());

    }

    class BlockStream{

        private String blocks;

        private int level = 0;
        private int sum = 0;
        private int garbageCount = 0;

        private boolean gotCancelSymbol = false;
        private boolean inGarbage = false;

        public BlockStream(String blocks){

            this.blocks = blocks;

        }

        public void processBlockStream(){

            for(char b : blocks.toCharArray()){

                if(gotCancelSymbol){
                    gotCancelSymbol = false;
                } else if(b == '!' && inGarbage){

                    gotCancelSymbol = true;

                } else if(!inGarbage && b == '<'){
                    inGarbage = true;
                } else if(inGarbage){
                    if(b == '>'){
                        inGarbage = false;
                    } else{
                        garbageCount++;
                    }
                } else if(b == '{'){
                    level++;
                } else if(b == '}'){
                    sum += level;
                    level--;
                }

            }

        }

        public int getSum(){return this.sum;}
        public int getGarbageCount(){return this.garbageCount;}


    }
}
