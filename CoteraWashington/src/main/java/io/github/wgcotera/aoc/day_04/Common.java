package io.github.wgcotera.aoc.day_04;

import java.util.HashSet;
import java.util.Set;

public class Common {

    public static Set<Integer> createSetOfNumbers(String range) {

        String[] rangeOfNumbers = range.split("-");
        int start = Integer.parseInt(rangeOfNumbers[0]);
        int end = Integer.parseInt(rangeOfNumbers[1]);
        Set<Integer> setOfNumbers = new HashSet<>();

        for (int i = start; i <= end; i++) {
            setOfNumbers.add(i);
        }
        return setOfNumbers;

    }

    public static void main(String[] args) {
        System.out.println(createSetOfNumbers("2-4"));
    }

}
