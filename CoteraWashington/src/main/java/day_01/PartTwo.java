package day_01;

import static day_01.Common.sumOfCalories;

public class PartTwo {
    public static void main(String[] args) {

        System.out.println(sumOfCalories.stream()
                .sorted((o1, o2) -> o2 - o1).toList()
                .subList(0, 3).stream()
                .mapToInt(v -> v)
                .sum());

    }
}
