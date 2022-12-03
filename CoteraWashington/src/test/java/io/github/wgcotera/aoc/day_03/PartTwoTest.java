package io.github.wgcotera.aoc.day_03;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartTwoTest {
    @Test
    void solution() {

        var partTwo = new PartTwo();
        var solution = partTwo.solution("""
                                            vJrwpWtwJgWrhcsFMMfFFhFp
                                            jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
                                            PmmdzqPrVvPwwTWBwg
                                            wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
                                            ttgJtRGJQctTZtZT
                                            CrZsJsPPZsGzwwsLwLmpwMDw""");
        assertEquals(solution, 70);
    }
}