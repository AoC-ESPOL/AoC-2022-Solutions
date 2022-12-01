package day_01;

import java.io.IOException;
import java.util.List;

import static day_01.PartOne.createListOfCalories;
import static day_01.PartOne.createListOfSumCalories;

public class PartTwo {
    public static void main(String[] args) throws IOException {
        List<String> listOfCalories = createListOfCalories("src/main/resources/inputOne.txt");
        List<Integer> sumOfCalories = createListOfSumCalories(listOfCalories);
        sumOfCalories.sort((o1, o2) -> o2 - o1);
        int sum = sumOfCalories.get(0) + sumOfCalories.get(1) + sumOfCalories.get(2);
        System.out.println(sum);

    }
}
