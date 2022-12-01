package day_01;

import java.util.stream.Collectors;

import static day_01.common.sumOfCalories;

public class PartTwo {
    public static void main(String[] args) {

        System.out.println(sumOfCalories.stream()
                .sorted((o1, o2) -> o2 - o1)
                .collect(Collectors.toList())
                .subList(0, 3).stream()
                .mapToInt(v -> v)
                .sum());

    }
}
