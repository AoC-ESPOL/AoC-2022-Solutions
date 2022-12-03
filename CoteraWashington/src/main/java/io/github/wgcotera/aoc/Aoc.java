package io.github.wgcotera.aoc;

public interface Aoc<T> {
    T solution(String input);

    String inputFilePath();

    default T run() {
        return solution(Util.readInput(inputFilePath()));
    }
}
