package io.github.wgcotera.aoc.day_02;

import io.github.wgcotera.aoc.Aoc;

import java.util.List;

import static io.github.wgcotera.aoc.day_02.Common.createListOfPlay;

public class PartTwo implements Aoc<Integer> {

    //    R 	A 1 X Lose
    //    P     B 2 Y Draw
    //    S	    C 3 Z Win

    public static int myPlayScore(String op, String result) {
        return switch (op) {
            case "A" -> switch (result) {
                case "X" -> 3;
                case "Y" -> 4;
                default -> 8;
            };
            case "B" -> switch (result) {
                case "X" -> 1;
                case "Y" -> 5;
                default -> 9;
            };
            default -> switch (result) {
                case "X" -> 2;
                case "Y" -> 6;
                default -> 7;
            };
        };
    }

    public static void main(String[] args) {
        System.out.println(new PartTwo().run());
    }

    @Override
    public Integer solution(String input) {

        List<List<String>> listOfPlay = createListOfPlay(input);
        List<String> op = listOfPlay.get(0);
        List<String> me = listOfPlay.get(1);

        int score = 0;

        for (int i = 0; i < op.size(); i++) {

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
