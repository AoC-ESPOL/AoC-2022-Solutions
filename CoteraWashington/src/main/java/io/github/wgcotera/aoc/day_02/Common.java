package io.github.wgcotera.aoc.day_02;

import java.util.ArrayList;
import java.util.List;

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
}
