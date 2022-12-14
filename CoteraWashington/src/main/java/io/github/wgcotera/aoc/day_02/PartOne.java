package io.github.wgcotera.aoc.day_02;

import io.github.wgcotera.aoc.Aoc;

import java.util.List;

import static io.github.wgcotera.aoc.day_02.Common.RESULT.*;
import static io.github.wgcotera.aoc.day_02.Common.createListOfPlay;
import static io.github.wgcotera.aoc.day_02.Common.letterValue;

public class PartOne implements Aoc<Integer> {

    //    R 	A 1 X
    //    P     B 2 Y
    //    S	    C 3 Z

    public static int myPlayScore(String op, String me) {
        return letterValue(me) + switch (op) {
            case "A" -> switch (me) {
                case "X" -> DRAW.score;
                case "Y" -> WIN.score;
                default -> LOSE.score;
            };
            case "B" -> switch (me) {
                case "X" -> LOSE.score;
                case "Y" -> DRAW.score;
                default -> WIN.score;
            };
            default -> switch (me) {
                case "X" -> WIN.score;
                case "Y" -> LOSE.score;
                default -> DRAW.score;
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
