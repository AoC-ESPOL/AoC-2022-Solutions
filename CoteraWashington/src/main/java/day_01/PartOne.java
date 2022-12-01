package day_01;

import static day_01.common.sumOfCalories;

public class PartOne {
    public static void main(String[] args) {

        System.out.println(sumOfCalories.stream()
                .mapToInt(v -> v)
                .max()
                .getAsInt());

    }
}
