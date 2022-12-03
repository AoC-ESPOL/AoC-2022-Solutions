package io.github.wgcotera.aoc.day_03;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartOneTest {
    @Test
    void solution() {

        var partOne = new PartOne();
        var solution = partOne.solution("""
                                            vJrwpWtwJgWrhcsFMMfFFhFp
                                            jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
                                            PmmdzqPrVvPwwTWBwg
                                            wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
                                            ttgJtRGJQctTZtZT
                                            CrZsJsPPZsGzwwsLwLmpwMDw""");
        assertEquals(solution, 157);

    }
}