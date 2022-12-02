package io.github.wgcotera.aoc.day_01;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PartTwoTest {
    @Test
    void solution() {

        var partTwo = new PartTwo();
        var solution = partTwo.solution("""
                                            1000
                                            2000
                                            3000
                                            
                                            4000
                                            
                                            5000
                                            6000
                                            
                                            7000
                                            8000
                                            9000
                                            
                                            10000""");
        assertEquals(solution, 45000);

    }

}