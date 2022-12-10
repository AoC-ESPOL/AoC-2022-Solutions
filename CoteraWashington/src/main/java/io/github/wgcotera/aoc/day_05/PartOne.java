package io.github.wgcotera.aoc.day_05;

import io.github.wgcotera.aoc.Aoc;

import java.util.List;

import static io.github.wgcotera.aoc.day_05.Common.*;

public class PartOne implements Aoc<String> {
    public static void main(String[] args) {
        System.out.println(new PartOne().run());
    }

    private static List<Stack> getFinalStacks(String input) {
        List<Stack> stacks = listOfStacks(input);
        List<Move> listOfMoves = listOfMoves(input);

        for (Move move : listOfMoves) {

            Stack from = stacks.get(move.from - 1);
            Stack to = stacks.get(move.to - 1);

            to.addElementToStack(from.removeCratesFromStackOneByOne(move.quantity));

        }
        return stacks;
    }

    @Override
    public String solution(String input) {
        return createStringWithTopCrates(getFinalStacks(input), input);
    }

    @Override
    public String inputFilePath() {
        return "5";
    }
}
