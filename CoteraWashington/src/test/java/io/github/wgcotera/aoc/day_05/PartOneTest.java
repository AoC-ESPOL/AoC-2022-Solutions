package io.github.wgcotera.aoc.day_05;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartOneTest {

    @Test
    void solution() {

//        Using line separator: \r\n for Windows

        var partOne = new PartOne();
        var solution = partOne.solution("""    
                    [D]   \s
                [N] [C]   \s
                [Z] [M] [P]
                 1   2   3\s\r\n\r\nmove 1 from 2 to 1
                move 3 from 1 to 3
                move 2 from 2 to 1
                move 1 from 1 to 2""");

        assertEquals(solution, "CMZ");
    }
}