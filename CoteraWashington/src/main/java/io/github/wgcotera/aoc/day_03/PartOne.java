package io.github.wgcotera.aoc.day_03;

import io.github.wgcotera.aoc.Aoc;

import java.util.*;

import static io.github.wgcotera.aoc.day_03.Common.mapOfLetterPriority;

public class PartOne implements Aoc<Integer> {

    public static List<String> listOfItemRepeatedInRucksacks(String input) {

        List<String> listOfRucksacks = input.lines().toList();
        List<String> itemRepeated = new ArrayList<>();

        for (String s : listOfRucksacks) {
            List<String> rucksack = Arrays.stream(s.split("")).toList();
            Set<String> r1 = new HashSet<>(rucksack.subList(0, rucksack.size() / 2));
            Set<String> r2 = new HashSet<>(rucksack.subList(rucksack.size() / 2, rucksack.size()));
            r1.retainAll(r2);
            itemRepeated.addAll(r1);
        }

        return itemRepeated;
    }

    public static void main(String[] args) {
        System.out.println(new PartOne().run());
    }

    @Override
    public Integer solution(String input) {
        List<String> itemRepeated = listOfItemRepeatedInRucksacks(input);
        return itemRepeated.stream().mapToInt(mapOfLetterPriority::get).sum();
    }

    @Override
    public String inputFilePath() {
        return "3";
    }
}
