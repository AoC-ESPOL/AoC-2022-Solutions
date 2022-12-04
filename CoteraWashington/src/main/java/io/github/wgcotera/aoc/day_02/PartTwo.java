package io.github.wgcotera.aoc.day_02;

import io.github.wgcotera.aoc.Aoc;

import java.util.List;

import static io.github.wgcotera.aoc.day_02.Common.createListOfPlay;
import static io.github.wgcotera.aoc.day_02.Common.letterValue;

public class PartTwo implements Aoc<Integer> {

    //    R 	A 1 X Lose
    //    P     B 2 Y Draw
    //    S	    C 3 Z Win

    public static int score(String op, String result) {
        return switch (result) {
            case "X" -> letterValue(switch (op) {
                case "A" -> "C";
                case "B" -> "A";
                default -> "B";
            });
            case "Y" -> letterValue(switch (op) {
                case "A" -> "A";
                case "B" -> "B";
                default -> "C";
            }) + 3;
            default -> letterValue(switch (op) {
                case "A" -> "B";
                case "B" -> "C";
                default -> "A";
            }) + 6;
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
            score += score(o, m);

        }
        return score;
    }

    @Override
    public String inputFilePath() {
        return "2";
    }
}
