package io.github.wgcotera.aoc.day_03;

import java.util.HashMap;
import java.util.Map;

public class Common {

    //    Lowercase item types a through z have priorities 1 through 26.
    //    Uppercase item types A through Z have priorities 27 through 52.

    public static Map<String, Integer> mapOfLetterPriority = createMapOfLetterPriority();

    public static Map<String, Integer> createMapOfLetterPriority() {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 1; i <= 26; i++) {
            map.put(String.valueOf((char) (i + 96)), i);
        }
        for (int i = 1; i <= 26; i++) {
            map.put(String.valueOf((char) (i + 64)), i + 26);
        }
        return map;
    }

}
