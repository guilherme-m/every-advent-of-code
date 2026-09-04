import java.util.*;
import java.util.stream.*;
import java.io.IOException;
import java.nio.file.*;

public class Day08 implements Day {

    public void run() {
        partOne();
    }

    private List<RegisterProgram.Instruction> readInput() {

        try (var lines = Files.lines(Path.of("inputs/Day08.txt"))) {

            return lines
                    .map(s -> {

                        String[] args = s.split("\\s+");

                        return new RegisterProgram.Instruction(
                                args[0],
                                args[1],
                                Integer.parseInt(args[2]),
                                args[4],
                                args[5],
                                Integer.parseInt(args[6]));
                    }).collect(Collectors.toList());

        } catch (IOException ioe) {

            throw new RuntimeException(ioe);
        }

    }

    private void partOne() {

        var input = readInput();

        input.forEach(i -> RegisterProgram.addInstruction(i));

        int max = RegisterProgram.registers
                .entrySet()
                .stream()
                .max((e1, e2) -> e1.getValue().compareTo(e2.getValue()))
                .get()
                .getValue();

        System.out.println(max);
    }

}

class RegisterProgram {

    public static Map<String, Integer> registers = new HashMap<>();

    public static record Instruction(
            String register1,
            String operation,
            Integer operationNumber,
            String register2,
            String test,
            Integer testNumber) {

        private void process() {

            if (doTest()) {

                doOperation();

            }

        }

        private boolean doTest() {
            Integer registerValue = registers.getOrDefault(register2, 0);
            return switch (test) {
                case "==" -> registerValue == testNumber;
                case ">" -> registerValue > testNumber;
                case ">=" -> registerValue >= testNumber;
                case "<=" -> registerValue <= testNumber;
                case "<" -> registerValue < testNumber;
                case "!=" -> registerValue != testNumber;
                case null, default -> throw new RuntimeException("Teste invalido");

            };
        }

        private void doOperation() {

            Integer increment = operationNumber;

            if (operation.equals("dec")) {
                increment *= -1;
            } else if (!operation.equals("inc")) {
                throw new RuntimeException("Operacao invalida");
            }

            registers.merge(register1, increment, (v1, v2) -> v1 + v2);

        }

    }

    public static void addInstruction(Instruction i) {

        i.process();

    }

}