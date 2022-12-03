package io.github.wgcotera.aoc.day_02;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartTwoTest {

    @Test
    void solution() {

        var partTwo = new PartTwo();
        var solution = partTwo.solution("""
                                                A Y
                                                B X
                                                C Z""");
        assertEquals(solution, 12);

    }
}