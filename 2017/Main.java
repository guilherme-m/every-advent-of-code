import java.io.IOException;

public class Main{

    public static void main(String[] args){

        if(args.length == 0){
            System.out.println("Informar dia desejado");
            return;
        }

        Integer day;

        try{

            day = Integer.parseInt(args[0]);

        } catch(NumberFormatException nfe){

            System.out.println("Formato de dia errado");
            return;

        }

        switch(day){
            case 1 -> Day01.run();
            default -> System.out.println("Dia nao implementado");
        }
    }


}