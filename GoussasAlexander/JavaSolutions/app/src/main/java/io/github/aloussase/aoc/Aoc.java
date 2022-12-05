package io.github.aloussase.aoc;

import java.nio.file.Files;
import java.nio.file.Paths;

public abstract class Aoc<P1, P2> {
  private String input;

  public Aoc() {
    try {
      var path = getClass().getResource("/" + inputFileName()).toURI();
      this.input = Files.readString(Paths.get(path));
    } catch (Exception ex) {
      throw new RuntimeException(ex);
    }
    initialize();
  }

  public Aoc(String input) {
    this.input = input;
    initialize();
  }

  public String getInput() {
    return input;
  }

  public void run() {
    System.out.println("Solution for " + this.getClass().getSimpleName());
    System.out.println("Part I: " + partOne());
    System.out.println("Part II: " + partTwo());
  }

  protected abstract void initialize();

  abstract P1 partOne();

  abstract P2 partTwo();

  abstract String inputFileName();
}
