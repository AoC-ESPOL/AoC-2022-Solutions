package io.github.wgcotera.aoc.day_02;

import io.github.wgcotera.aoc.Aoc;

import java.util.List;

import static io.github.wgcotera.aoc.day_02.Common.createListOfPlay;

public class PartOne implements Aoc<Integer> {

    //    R 	A 1 X
    //    P     B 2 Y
    //    S	    C 3 Z

    public static int myPlayScore(String op, String me) {
        return switch (op) {
            case "A" -> switch (me) {
                case "X" -> 4;
                case "Y" -> 8;
                default -> 3;
            };
            case "B" -> switch (me) {
                case "X" -> 1;
                case "Y" -> 5;
                default -> 9;
            };
            default -> switch (me) {
                case "X" -> 7;
                case "Y" -> 2;
                default -> 6;
            };
        };
    }

    public static void main(String[] args) {
        System.out.println(new PartOne().run());
    }

    @Override
    public Integer solution(String input) {

        List<List<String>> listOfPlay = createListOfPlay(input);
        List<String> op = listOfPlay.get(0);
        List<String> me = listOfPlay.get(1);

        int score = 0;

        for (int i = 0; i < me.size(); i++) {

            String m = me.get(i);
            String o = op.get(i);
            score += myPlayScore(o, m);
        }
        return score;
    }

    @Override
    public String inputFilePath() {
        return "2";
    }
}
