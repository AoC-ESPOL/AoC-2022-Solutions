package io.github.wgcotera.aoc.day_02;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartOneTest {

    @Test
    void solution() {

        var partOne = new PartOne();
        var solution = partOne.solution("""
                                                A Y
                                                B X
                                                C Z""");
        assertEquals(solution, 15);
    }
}