package io.github.wgcotera.aoc.day_02;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Common {
    public static List<List<String>> createListOfPlay(String input) {

        List<String> listOfPlay = input.lines().toList();

        List<String> op = new ArrayList<>();
        List<String> me = new ArrayList<>();

        for (String s : listOfPlay) {
            String[] play = s.split(" ");
            op.add(play[0]);
            me.add(play[1]);
        }

        return List.of(op, me);
    }

    public static int letterValue(String letter) {
        return Map.of(
                "A", 1,
                "B", 2,
                "C", 3,
                "X", 1,
                "Y", 2,
                "Z", 3
        ).get(letter);
    }

    public enum RESULT {
        WIN(6), DRAW(3), LOSE(0);

        public int score;

        RESULT(int score) {
            this.score = score;
        }
    }
}
