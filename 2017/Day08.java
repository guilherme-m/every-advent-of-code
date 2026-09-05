import java.util.*;
import java.util.stream.*;
import java.io.IOException;
import java.nio.file.*;

public class Day08 implements Day {

    public void run() {
        partOne();
        partTwo();
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

        RegisterProgram rp = new RegisterProgram();

        input.forEach(i -> rp.addInstruction(i));

        int max = rp.registers
                .values()
                .stream()
                .mapToInt(Integer::intValue)
                .max()
                .getAsInt();

        System.out.println("Part 1: " + max);
    }

    private void partTwo() {

        var input = readInput();

        RegisterProgram rp = new RegisterProgram();

        input.forEach(i -> rp.addInstruction(i));

        System.out.println("Part 2: " + rp.max);

    }

    static class RegisterProgram {

        public final Map<String, Integer> registers = new HashMap<>();

        public int max;

        public static record Instruction(
                String register1,
                String operation,
                Integer operationNumber,
                String register2,
                String test,
                Integer testNumber) {

        }

        private void process(Instruction i) {

            if (doTest(i)) {

                doOperation(i);

            }

        }


        private boolean doTest(Instruction i) {
            Integer registerValue = registers.getOrDefault(i.register2(), 0);
            return switch (i.test()) {
                case "==" -> registerValue.intValue() == i.testNumber().intValue();
                case ">" -> registerValue.intValue() > i.testNumber().intValue();
                case ">=" -> registerValue.intValue() >= i.testNumber().intValue();
                case "<=" -> registerValue.intValue() <= i.testNumber().intValue();
                case "<" -> registerValue.intValue() < i.testNumber().intValue();
                case "!=" -> registerValue.intValue() != i.testNumber().intValue();
                case null, default -> throw new RuntimeException("Teste invalido");

            };
        }

        private void doOperation(Instruction i) {

            Integer increment = i.operationNumber();

            if (i.operation().equals("dec")) {
                increment = -increment;
            } else if (!i.operation().equals("inc")) {
                throw new RuntimeException("Operacao invalida");
            }

            Integer value = registers.merge(i.register1(), increment, (v1, v2) -> v1 + v2);

            if (value > max) {
                max = value;
            }

        }

       

        public void addInstruction(Instruction i) {
            registers.putIfAbsent(i.register1(), 0);
            registers.putIfAbsent(i.register2(), 0);
            process(i);

        }


    }
}
