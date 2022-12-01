package day_01;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PartOne {
    public static void main(String[] args) throws IOException {
        List<String> listOfCalories = createListOfCalories("src/main/resources/inputOne.txt");
        List<Integer> sumOfCalories = createListOfSumCalories(listOfCalories);
        System.out.println(sumOfCalories.stream().mapToInt(v -> v).max().getAsInt());
    }

    public static List<String> createListOfCalories(String fileName) throws IOException {
        List<String> list = new ArrayList<>();
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        String line;
        while ((line = br.readLine()) != null) {
            list.add(line);
        }
        br.close();
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
}
