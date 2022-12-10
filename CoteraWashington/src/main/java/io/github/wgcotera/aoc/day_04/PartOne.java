package io.github.wgcotera.aoc.day_04;

import io.github.wgcotera.aoc.Aoc;

import java.util.Arrays;
import java.util.List;
import java.util.Set;

import static io.github.wgcotera.aoc.day_04.Common.createSetOfRangeOfNumbers;

public class PartOne implements Aoc<Integer> {

    public static void main(String[] args) {
        System.out.println(new PartOne().run());
    }

    @Override
    public Integer solution(String input) {

        List<List<String>> listOfPairs = input.lines().map(l -> Arrays.stream(l.split(",")).toList()).toList();

        int result = 0;

        for (List<String> p : listOfPairs) {
            Set<Integer> set1 = createSetOfRangeOfNumbers(p.get(0));
            Set<Integer> set2 = createSetOfRangeOfNumbers(p.get(1));

            if (set1.containsAll(set2) || set2.containsAll(set1)) result++;
        }
        return result;
    }

    @Override
    public String inputFilePath() {
        return "4";
    }
}
