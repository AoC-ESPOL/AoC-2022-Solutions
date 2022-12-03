package io.github.wgcotera.aoc.day_01;

import java.util.ArrayList;
import java.util.List;

public class Common {

    public static List<Integer> createListOfSumCalories(String input) {

        List<String> listOfCalories = input.lines().toList();
        List<Integer> sumCalories = new ArrayList<>();

        int sumCal = 0;

        for (String c : listOfCalories) {
            if (c.isEmpty()) {
                sumCalories.add(sumCal);
                sumCal = 0;
            } else {
                sumCal += Integer.parseInt(c.trim());
            }
        }
        if(sumCal > 0) {
            sumCalories.add(sumCal);
        }

        return sumCalories;
    }
}
