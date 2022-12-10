package io.github.aloussase.aoc;

import static java.util.function.Predicate.*;
import static java.util.stream.IntStream.range;
import static java.util.stream.Stream.iterate;

import java.util.*;
import java.util.regex.*;
import java.util.stream.Collectors;

final public class DayFive extends Aoc<String, String> {
  private List<String> drawing;
  private List<String> moves;
  private long numberOfStacks;
  private List<ArrayDeque<Character>> stacks;

  public DayFive() {
    super();
  }

  public DayFive(String input) {
    super(input);
  }

  @Override
  protected void initialize() {
    var input = getInput();
    var parts = input.split("\n\n");

    this.drawing = parts[0].lines().toList();
    this.moves = parts[1].lines().toList();
    this.numberOfStacks =
        Arrays.asList(drawing.get(drawing.size() - 1).split(" "))
            .stream()
            .filter(not(String::isEmpty))
            .count();
    this.stacks = new ArrayList<>((int)numberOfStacks);

    range(0, (int)numberOfStacks)
        .mapToObj(i -> new ArrayDeque<Character>())
        .forEach(stacks::add);
  }

  private void fillStacks() {
    stacks.forEach(ArrayDeque::clear);
    for (var line : drawing) {
      var crates = parseLine(line);
      range(0, (int)numberOfStacks)
          .filter(i -> crates.get(i) != ' ')
          .forEach(i -> stacks.get(i).addLast(crates.get(i)));
    }
  }

  public List<Character> parseLine(final String line) {
    return iterate(0, pos -> pos < line.length(), pos -> pos + 4)
        .map(pos -> line.charAt(pos) == '[' ? line.charAt(pos + 1) : ' ')
        .collect(Collectors.toList());
  }

  private String getItemsOnTopOfEachStack() {
    return stacks.stream()
        .map(ArrayDeque::removeFirst)
        .map(Object::toString)
        .collect(Collectors.joining());
  }

  private static record Move(int quantity, int src, int dest) {
    public static Move parse(String line) {
      var xs = line.split(" ");
      var n = Integer.parseInt(xs[1]);
      var src = Integer.parseInt(xs[3]) - 1;
      var dest = Integer.parseInt(xs[5]) - 1;
      return new Move(n, src, dest);
    }
  }

  @Override
  public String partOne() {
    fillStacks();

    for (var line : moves) {
      var move = Move.parse(line);
      for (int i = 0; i < move.quantity(); i++) {
        stacks.get(move.dest()).addFirst(stacks.get(move.src()).removeFirst());
      }
    }

    return getItemsOnTopOfEachStack();
  }

  @Override
  public String partTwo() {
    fillStacks();

    for (var line : moves) {
      var move = Move.parse(line);

      ArrayDeque<Character> d = new ArrayDeque<>();

      for (int i = 0; i < move.quantity(); i++) {
        d.addLast(stacks.get(move.src()).removeFirst());
      }

      while (!d.isEmpty()) {
        stacks.get(move.dest()).addFirst(d.removeLast());
      }
    }

    return getItemsOnTopOfEachStack();
  }

  @Override
  public String inputFileName() {
    return "day5.txt";
  }
}
