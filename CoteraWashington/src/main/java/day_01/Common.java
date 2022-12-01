package day_01;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.List;

public class Common {
    public static List<String> createListOfCalories(String fileName) {
        List<String> list = new ArrayList<>();
        try(BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                list.add(line);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return list;
    }

    public static List<Integer> createListOfSumCalories(List<String> listOfCalories) {
        List<Integer> sumCalories = new ArrayList<>();
        int sumCal = 0;
        for (String c : listOfCalories) {
            if (c.equals("")) {
                sumCalories.add(sumCal);
                sumCal = 0;
            } else {
                sumCal += Integer.parseInt(c);
            }
        }
        return sumCalories;
    }

    public static List<String> listOfCalories = createListOfCalories("src/main/resources/inputDayOne.txt");
    public static List<Integer> sumOfCalories = createListOfSumCalories(listOfCalories);
}
