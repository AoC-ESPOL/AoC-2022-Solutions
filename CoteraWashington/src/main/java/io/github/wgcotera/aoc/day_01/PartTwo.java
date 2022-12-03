package io.github.wgcotera.aoc.day_01;

import io.github.wgcotera.aoc.Aoc;

import java.util.Comparator;

import static io.github.wgcotera.aoc.day_01.Common.createListOfSumCalories;

public class PartTwo implements Aoc<Integer> {

    public static void main(String[] args) {
        System.out.println(new PartTwo().run());
    }

    @Override
    public Integer solution(String input) {

        return createListOfSumCalories(input).stream()
                .sorted(Comparator.reverseOrder())
                .limit(3)
                .reduce(Integer::sum)
                .get();
    }

    @Override
    public String inputFilePath() {
        return "1";
    }
}
