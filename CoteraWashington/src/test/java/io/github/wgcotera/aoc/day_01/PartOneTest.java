package io.github.wgcotera.aoc.day_01;


import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PartOneTest {
    @Test
    void solution() {

        var partOne = new PartOne();
        var solution = partOne.solution("""
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
        assertEquals(solution, 24000);

    }
}