package io.github.wgcotera.aoc.day_03;

import io.github.wgcotera.aoc.Aoc;

import java.util.List;

import static io.github.wgcotera.aoc.day_02.Common.createListOfPlay;

public class PartTwo implements Aoc<Integer> {
    public static void main(String[] args) {
        System.out.println(new PartTwo().run());
    }

    @Override
    public Integer solution(String input) {
        List<List<String>> listOfPlay = createListOfPlay(input);
        return null;
    }

    @Override
    public String inputFilePath() {
        return "3";
    }
}
