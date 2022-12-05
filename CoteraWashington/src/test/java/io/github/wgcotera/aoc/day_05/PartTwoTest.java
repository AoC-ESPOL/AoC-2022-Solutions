package io.github.wgcotera.aoc.day_05;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PartTwoTest {

    @Test
    void solution() {

//        Using line separator: \r\n for Windows

        var partTwo = new PartTwo();
        var solution = partTwo.solution("""
                    [D]   \s
                [N] [C]   \s
                [Z] [M] [P]
                 1   2   3\s\r\n\r\nmove 1 from 2 to 1
                move 3 from 1 to 3
                move 2 from 2 to 1
                move 1 from 1 to 2""");
        assertEquals(solution, "MCD");
    }
}