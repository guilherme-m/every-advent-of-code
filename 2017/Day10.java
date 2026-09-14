import java.util.stream.*;
import java.util.*;
import java.io.*;

public class Day10 implements Day {
    public void run() {
        partOne();
        partTwo();
    }

    public int[] readInput() {

        File f = new File("inputs/Day10.txt");

        try (
                var fr = new FileReader(f);
                var br = new BufferedReader(fr)) {

            String[] input = br.readLine().split(",");

            return Arrays.stream(input)
                    .mapToInt(x -> Integer.parseInt(x))
                    .toArray();

        } catch (IOException ioe) {

            throw new RuntimeException(ioe);
        }

    }

    public int[] readInputAsChars() {

        File f = new File("inputs/Day10.txt");

        try (
                var fr = new FileReader(f);
                var br = new BufferedReader(fr)) {

            String input = br.readLine();

            return input
                    .chars()
                    .toArray();

        } catch (IOException ioe) {

            throw new RuntimeException(ioe);
        }

    }

    public void partOne() {
        int[] input = readInput();

        var knotHash = new KnotHash(input);

        knotHash.calculateHash();

        System.out.println("Part 1: " + (knotHash.knots[0] * knotHash.knots[1]));
    }

    public void partTwo() {

        int[] input = readInputAsChars();

        input = IntStream.concat(
                Arrays.stream(input),
                Arrays.stream(new int[] { 17, 31, 73, 47, 23 })).toArray();

        var knotHash = new KnotHash(input);

        for (int i = 0; i < 64; i++) {
            knotHash.calculateHash();
        }

        System.out.println(knotHash.getDenseHash());

    }

    private static class KnotHash {

        private final int KNOTS_SIZE;

        int[] knots;

        int[] steps;

        int skipSize = 0;

        int currentPosition = 0;

        public KnotHash(int[] steps) {

            this.KNOTS_SIZE = 256;

            this.knots = IntStream.range(0, KNOTS_SIZE).toArray();

            this.steps = steps;
        }

        public KnotHash(int[] steps, int size) {

            this.KNOTS_SIZE = size;

            this.knots = IntStream.range(0, KNOTS_SIZE).toArray();

            this.steps = steps;
        }

        public void calculateHash() {

            for (int step : steps) {

                proccessStep(step);

                skipSize++;

            }

        }

        private void proccessStep(int step) {

            int start = currentPosition;
            int end = (currentPosition + step - 1) % KNOTS_SIZE;

            for (int i = 0; i < step / 2; i++) {

                swap(start, end);

                start = (start + 1) % KNOTS_SIZE;
                end = end == 0 ? KNOTS_SIZE - 1 : end - 1;

            }

            currentPosition = (currentPosition + step + skipSize) % KNOTS_SIZE;

        }

        private void swap(int i, int j) {

            int tmp = knots[i];

            knots[i] = knots[j];
            knots[j] = tmp;

        }

        public String getDenseHash() {

            List<Integer> list = new ArrayList<>();

            for (var i = 0; i <= KNOTS_SIZE - 16; i += 16) {

                int xorInt = knots[i];

                for (var j = 1; j < 16; j++) {

                    xorInt = xorInt ^ knots[i + j];

                }

                list.add(xorInt);

            }

            return list
                    .stream()
                    .map(x -> String.format("%02x", x))
                    .collect(Collectors.joining());

        }

    }
}
