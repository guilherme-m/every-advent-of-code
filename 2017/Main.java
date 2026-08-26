public class Main{

    public static void main(String[] args){

        if(args.length == 0){
            throw new RuntimeException("Informar dia desejado");
            
        }

        Integer day;

        try{

            day = Integer.parseInt(args[0]);

        } catch(NumberFormatException nfe){

            throw new RuntimeException("Formato de dia errado");
            
        }

        switch(day){
            case 1 -> Day01.run();
            case 2 -> Day02.run();
            case 3 -> new Day03().run();
            case 4 -> new Day04().run();
            case 5 -> new Day05().run();
            default -> System.out.println("Dia nao implementado");
        }
    }


}