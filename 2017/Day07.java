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

            Map<Program, Integer> totalWeights = new HashMap<>();

            public int totalWeight(Program p) {

                int weight;

                if (totalWeights.containsKey(p)) {
                    return totalWeights.get(p);
                }

                if (p.children() == null) {

                    weight = p.weight();
                } else {

                    weight = p.weight() + p.children().stream()
                            .map(c -> totalWeight(programsMap.get(c)))
                            .reduce(0, (c1, c2) -> c1 + c2);

                }

                totalWeights.put(p, weight);

                return weight;
            }

            public int find() {
                Program parent = start;

                Map<Program, Integer> result = null;
                while (start.children() != null) {

                    var childPrograms = start.children().stream()
                            .map(s -> programsMap.get(s))
                            .toList();

                    if (childPrograms.stream().anyMatch(l -> totalWeight(l) != totalWeight(childPrograms.get(0)))) {

                        parent = start;

                    }

                    var weights = start.children().stream()
                            .map(s -> programsMap.get(s))
                            .collect(Collectors.groupingBy(p -> totalWeight(p)))
                            .values()
                            .stream()
                            .filter(c -> c.size() == 1)
                            .findFirst();

                    if(weights.isPresent()){

                        start = weights.get().get(0);
                    } else {
                        break;
                    }


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

            private int newWeight(Map<Program, Integer> m) {

                var weights = m.entrySet().stream()
                        .collect(Collectors.groupingBy(
                                e -> e.getValue(),
                                Collectors.mapping(e -> e.getKey(), Collectors.toList())));

                var oddProgram = m.keySet().stream().findAny().get();
                int okayProgramWeight = m.values().stream().findAny().get();

                for (var e : weights.entrySet()) {

                    if (e.getValue().size() == 1) {
                        oddProgram = e.getValue().get(0);
                    } else {
                        okayProgramWeight = e.getKey();
                    }

                }

                int diff = okayProgramWeight - m.get(oddProgram);

                return oddProgram.weight() + diff;

            }

        }

        return "" + new UnbalancedProgramFinder().find();
    }

}

record Program(String name, int weight, List<String> children) {

    public Program(String name, int weight) {
        this(name, weight, null);
    }

}
