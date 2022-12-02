package day_02;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Common {

    public static List<List<String>> createListOfPlay(String fileName) {

        List<String> op = new ArrayList<>();
        List<String> me = new ArrayList<>();

        try(BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] split = line.split(" ");
                op.add(split[0]);
                me.add(split[1]);
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return List.of(op, me);
    }
    public static List<List<String>> listOfPlay = createListOfPlay("src/main/resources/inputDayTwo.txt");
    public static List<String> op = listOfPlay.get(0);
    public static List<String> me = listOfPlay.get(1);
}
