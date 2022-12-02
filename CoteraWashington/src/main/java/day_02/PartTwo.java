package day_02;

import static day_02.Common.me;
import static day_02.Common.op;

public class PartTwo {

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

        int score = 0;

        for (int i = 0; i < op.size(); i++) {

            String m = me.get(i);
            String o = op.get(i);
            score += myPlayScore(o, m);

        }

        System.out.println(score);
    }
}
