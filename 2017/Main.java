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

        Day d = switch(day){
            case 1 -> new Day01();
            case 2 -> new Day02();
            case 3 -> new Day03();
            case 4 -> new Day04();
            case 5 -> new Day05();
            case 6 -> new Day06();
            case 7 -> new Day07();
            case null, default -> throw new RuntimeException("Dia nao implementado");
        };

        d.run();
    }


}