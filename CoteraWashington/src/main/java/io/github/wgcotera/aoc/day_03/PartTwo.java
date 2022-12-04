package io.github.wgcotera.aoc.day_03;

import io.github.wgcotera.aoc.Aoc;

import java.util.*;

import static io.github.wgcotera.aoc.day_03.Common.mapOfLetterPriority;

public class PartTwo implements Aoc<Integer> {

    public static List<String> listOfitemsRepeatedEachThreeRucksacks(String input) {

        List<String> listRucksacks = input.lines().toList();
        List<String> itemsRepeated = new ArrayList<>();

        for (int i = 0; i < listRucksacks.size(); i += 3) {

            Set<String> r1 = new HashSet<>(Arrays.stream(listRucksacks.get(i).split("")).toList());
            Set<String> r2 = new HashSet<>(Arrays.stream(listRucksacks.get(i + 1).split("")).toList());
            Set<String> r3 = new HashSet<>(Arrays.stream(listRucksacks.get(i + 2).split("")).toList());

            r1.retainAll(r2);
            r1.retainAll(r3);

            itemsRepeated.addAll(r1);
        }

        return itemsRepeated;
    }

    public static void main(String[] args) {
        System.out.println(new PartTwo().run());
    }

    @Override
    public Integer solution(String input) {
        List<String> ListOfItemRepeatedInRucksacks = listOfitemsRepeatedEachThreeRucksacks(input);
        return ListOfItemRepeatedInRucksacks.stream().mapToInt(mapOfLetterPriority::get).sum();
    }

    @Override
    public String inputFilePath() {
        return "3";
    }
}
