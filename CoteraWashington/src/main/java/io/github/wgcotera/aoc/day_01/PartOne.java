package io.github.wgcotera.aoc.day_01;

import io.github.wgcotera.aoc.Aoc;

import java.util.Collections;

import static io.github.wgcotera.aoc.day_01.Common.createListOfSumCalories;

public class PartOne implements Aoc<Integer> {

    public static void main(String[] args) {
        System.out.println(new PartOne().run());
    }

    @Override
    public Integer solution(String input) {
        return Collections.max(createListOfSumCalories(input));
    }

    @Override
    public String inputFilePath() {
        return "1";
    }
}
