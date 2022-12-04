package io.github.wgcotera.aoc.day_04;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartOneTest {

    @Test
    void solution() {

        var partOne = new PartOne();
        var solution = partOne.solution("""
                                        2-4,6-8
                                        2-3,4-5
                                        5-7,7-9
                                        2-8,3-7
                                        6-6,4-6
                                        2-6,4-8""");
        assertEquals(solution, 2);
    }
}