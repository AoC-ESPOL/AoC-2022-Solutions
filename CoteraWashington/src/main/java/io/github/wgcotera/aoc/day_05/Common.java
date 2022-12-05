package io.github.wgcotera.aoc.day_05;

import java.util.*;

public class Common {


    public static List<String> getDataSeparated(String input) {
        return Arrays.asList(input.split(System.lineSeparator() + System.lineSeparator()));
    }

    public static List<List<String>> getStacksInfo(List<String> dataSeparated) {

        List<String> dataStacks = dataSeparated.get(0).lines().toList();
        List<List<String>> stacksInfo = new ArrayList<>();

        for (String line : dataStacks) {

            List<String> stack = new ArrayList<>();

            for (int i = 1; i < line.length(); i += 4) {
                stack.add(line.substring(i, i + 1));
            }

            stacksInfo.add(stack);
        }

        return stacksInfo;
    }

    public static Map<Integer, List<String>> createStacksMap(List<List<String>> stacksInfo) {

        List<Integer> stacksNumbers = stacksInfo.get(stacksInfo.size() - 1).stream().map(Integer::parseInt).toList();
        List<List<String>> stacksContent = stacksInfo.subList(0, stacksInfo.size() - 1);

        Map<Integer, List<String>> stacksMap = new HashMap<>();
        for (int i : stacksNumbers) {
            stacksMap.put(i, new ArrayList<>());
        }

        for (List<String> stack : stacksContent) {

            for (int i = 0; i < stack.size(); i++) {
                String s = stack.get(i);
                if (!s.equals(" ")) {
                    stacksMap.get(i + 1).add(0, s);
                }
            }
        }
        return stacksMap;
    }

    public static List<Stack> getStacks(Map<Integer, List<String>> stacksMap) {

        List<Stack> stacksList = new ArrayList<>();

        for (Map.Entry<Integer, List<String>> entry : stacksMap.entrySet()) {
            stacksList.add(new Stack(entry.getKey(), entry.getValue()));
        }

        return stacksList;
    }

    public static List<Move> getMoves(List<String> dataSeparated) {

        List<String> dataMoves = dataSeparated.get(1).lines().toList();
        List<Move> moves = new ArrayList<>();

        for (String line : dataMoves) {
            String[] move = line.trim().split(" ");
            moves.add(new Move(Integer.parseInt(move[1]), Integer.parseInt(move[3]), Integer.parseInt(move[5])));
        }

        return moves;
    }

    public static List<Stack> listOfStacks(String input) {
        return getStacks(createStacksMap(getStacksInfo(getDataSeparated(input))));
    }

    public static List<Move> listOfMoves(String input) {
        return getMoves(getDataSeparated(input));
    }

    public static String createStringWithTopCrates(List<Stack> finalStacks, String input) {
        StringBuilder result = new StringBuilder();
        for (Stack stack : finalStacks) {
            if (stack.content.size() > 0) {
                result.append(stack.content.get(stack.content.size() - 1));
            }
        }

        return result.toString();
    }
}
