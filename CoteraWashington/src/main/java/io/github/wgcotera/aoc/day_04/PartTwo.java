package io.github.wgcotera.aoc.day_04;

import io.github.wgcotera.aoc.Aoc;

import java.util.Arrays;
import java.util.List;
import java.util.Set;

import static io.github.wgcotera.aoc.day_04.Common.createSetOfNumbers;

public class PartTwo implements Aoc<Integer> {

    public static void main(String[] args) {
        System.out.println(new PartTwo().run());
    }

    @Override
    public Integer solution(String input) {

        List<List<String>> listOfPairs = input.lines().map(l -> Arrays.stream(l.split(",")).toList()).toList();

        int result = 0;
        for (List<String> p : listOfPairs) {
            Set<Integer> set1 = createSetOfNumbers(p.get(0));
            Set<Integer> set2 = createSetOfNumbers(p.get(1));

            set1.retainAll(set2);
            if (set1.size() > 0) result++;
        }
        return result;
    }

    @Override
    public String inputFilePath() {
        return "4";
    }
}
