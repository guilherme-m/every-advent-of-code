import java.util.*;

import java.nio.file.*;
import java.io.IOException;

public class Day11 implements Day {
    public void run() {

        partOne();
        partTwo();
    }

    public void partOne() {
        List<Direction> directions = readInput();

        Hexagon hex = new Hexagon();

        for (var d : directions) {

            hex = hex.plus(d);
            
        }

        System.out.println("Part 1: " + hex.stepsToOrigin());
    }

    public void partTwo() {
        List<Direction> directions = readInput();

        Hexagon hex = new Hexagon();

        int maxDistance = 0;

        for (var d : directions) {

            hex = hex.plus(d);
            
            maxDistance = Math.max(hex.stepsToOrigin(), maxDistance);
        }

        System.out.println("Part 2: " + maxDistance);

    }

    public List<Direction> readInput() {

        Path p = Path.of("inputs/Day11.txt");

        try {

            String in = Files.readString(p);
            return List
                    .of(in.strip().split(","))
                    .stream()
                    .map(x -> Direction.valueOf(x))
                    .toList();

        } catch (IOException ioe) {
            throw new RuntimeException(ioe);
        }

    }

    enum Direction {
        n(0, 1), ne(0.5, 0.5), nw(-0.5, 0.5),
        s(0, -1), se(0.5, -0.5), sw(-0.5, -0.5);

        Direction(double x, double y) {
            this.x = x;
            this.y = y;
        }

        private double x, y;

        public double x() {
            return x;
        }

        public double y() {
            return y;
        }
    }

    record Hexagon(double x, double y) {

        Hexagon() {
            this(0, 0);
        }

        public Hexagon plus(Direction d) {

            return new Hexagon(x + d.x(), y + d.y());

        }

        public int stepsToOrigin() {

            int xSteps = (int) (Math.abs(x) / 0.5);

            int ySteps = (int) (Math.abs(y) - Math.abs(x));

            return xSteps + ySteps;

        }

    }
}
