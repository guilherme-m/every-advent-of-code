import java.util.*;
import java.util.stream.*;

import java.nio.file.*;
import java.io.IOException;

import java.util.regex.*;

public class Day07 implements Day {

    public void run() {

        partOne();
    }

    private List<Program> readInput() {

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

        var input = readInput();

        var allPrograms = input.stream()
                .map(p -> p.name())
                .collect(Collectors.toSet());

        var childrenPrograms = input.stream()
                .filter(p -> p.children() != null)
                .collect(Collectors.flatMapping(p -> p.children().stream(), Collectors.toSet()));

        allPrograms.removeAll(childrenPrograms);

        System.out.println("Part 1: " + allPrograms.stream().findFirst().get());

    }
}

record Program(String name, int weight, List<String> children) {

    public Program(String name, int weight) {
        this(name, weight, null);
    }

}