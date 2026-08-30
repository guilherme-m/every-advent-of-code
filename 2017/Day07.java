import java.util.*;
import java.util.stream.*;

import java.nio.file.*;
import java.io.IOException;

import java.util.regex.*;

public class Day07 implements Day {

    public void run() {

        partOne();
        partTwo();
    }

    protected List<Program> readInput() {

        Pattern p = Pattern.compile(
                "([a-z]+) \\(([0-9]+)\\)(?: -> (.+))?");

        List<Program> programs = new ArrayList<>();

        try (var lines = Files.lines(Path.of("inputs/Day07.txt"))) {

            lines.forEach(s -> {
                Matcher m = p.matcher(s.strip());

                if (m.matches()) {

                    if (m.group(3) == null) {

                        programs.add(
                                new Program(m.group(1), Integer.parseInt(m.group(2))));

                    } else {

                        String[] childPrograms = m.group(3).split(", ");

                        programs.add(
                                new Program(
                                        m.group(1),
                                        Integer.parseInt(m.group(2)),
                                        Arrays.asList(childPrograms)));

                    }

                }

            });

        } catch (IOException ioe) {

            throw new RuntimeException(ioe);
        }

        return programs;

    }

    private void partOne() {

        System.out.println("Part 1: " + getRoot());

    }

    private String getRoot() {
        var input = readInput();

        var allPrograms = input.stream()
                .map(p -> p.name())
                .collect(Collectors.toSet());

        var childrenPrograms = input.stream()
                .filter(p -> p.children() != null)
                .collect(Collectors.flatMapping(p -> p.children().stream(), Collectors.toSet()));

        allPrograms.removeAll(childrenPrograms);

        return allPrograms.stream().findFirst().get();
    }

    private void partTwo() {

        String unbalancedProgram = findUnbalancedProgram();

        System.out.println("Part 2: " + unbalancedProgram);

    }

    private String findUnbalancedProgram() {

        class UnbalancedProgramFinder {

            List<Program> programs = readInput();

            Map<String, Program> programsMap = programs.stream()
                    .collect(Collectors.toMap(p -> p.name(), p -> p));

            Program start = programsMap.get(getRoot());

            public int totalWeight(Program p) {
                if (p.children() == null) {

                    return p.weight();
                } else {

                    return p.weight() + p.children().stream()
                            .map(c -> totalWeight(programsMap.get(c)))
                            .reduce(0, (c1, c2) -> c1 + c2);

                }
            }

            public int find() {
                Program parent = start;

                Map<Program, Integer> result = null;
                while (start.children() != null) {
                    
                    var childPrograms = start.children().stream()
                            .map(s -> programsMap.get(s))
                            .toList();

                    if (childPrograms.stream().anyMatch(l -> totalWeight(l) != totalWeight(childPrograms.get(0)))){

                        parent = start;
                        
                    
                    }


                    start = start.children().stream()
                            .map(s -> programsMap.get(s))
                            .sorted((p1, p2) -> totalWeight(p2) - totalWeight(p1))
                            .findFirst()
                            .get();

                }
                result = parent
                        .children()
                        .stream()
                        .map(s -> programsMap.get(s))
                        .toList()
                        .stream()
                        .collect(Collectors.toMap(p -> p, p -> totalWeight(p)));

                return newWeight(result);

            }

            private int newWeight(Map<Program, Integer> m){
                var heavyProgram = m.entrySet().stream().max(Map.Entry.comparingByValue()).get();

                int min = m.entrySet().stream().min(Map.Entry.comparingByValue()).get().getValue();

                int diff = heavyProgram.getValue() - min;

                return heavyProgram.getKey().weight() - diff;

            }

        }

        return ""  + new UnbalancedProgramFinder().find();
    }

}

record Program(String name, int weight, List<String> children) {

    public Program(String name, int weight) {
        this(name, weight, null);
    }

}
