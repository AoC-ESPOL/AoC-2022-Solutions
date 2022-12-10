package io.github.wgcotera.aoc;

import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Objects;

public class Util {
    public static String readInput(String day) {
        try {
            final URI path = Objects.requireNonNull(Util.class.getResource("/inputDay" + day + ".txt")).toURI();
            return Files.readString(Paths.get(path));
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
