package io.github.aloussase.aoc;

import java.util.*;
import java.util.regex.*;
import java.util.stream.Collectors;
import static java.util.function.Predicate.*;
import static java.util.stream.IntStream.range;
import static java.util.stream.Stream.iterate;

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
    this.numberOfStacks = getNumberOfStacks(drawing);
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

  private Optional<Character> parseCrate(String crate) {
    if (crate.isEmpty()) return Optional.empty();
    return  crate.charAt(0) == '['
        ? Optional.of(crate.charAt(1))
        : Optional.empty();
  }

  private long getNumberOfStacks(List<String> drawing) {
    return Arrays.asList(drawing.get(drawing.size() - 1).split(" "))
      .stream()
      .filter(not(String::isEmpty))
      .count();
  }

  private String getItemsOnTopOfEachStack() {
    return stacks
      .stream()
      .map(ArrayDeque::removeFirst)
      .map(Object::toString)
      .collect(Collectors.joining());
  }


  @Override
  public String partOne() {
    fillStacks();

    for (var line : moves) {
      var xs = line.split(" ");
      var n = Integer.parseInt(xs[1]);
      var src = Integer.parseInt(xs[3]) - 1;
      var dest = Integer.parseInt(xs[5]) - 1;

      for (int i = 0; i < n; i++) {
        stacks.get(dest).addFirst(stacks.get(src).removeFirst());
      }
    }

    return getItemsOnTopOfEachStack();
  }

  @Override
  public String partTwo() {
    fillStacks();

    for (var line : moves) {
      var xs = line.split(" ");
      var n = Integer.parseInt(xs[1]);
      var src = Integer.parseInt(xs[3]) - 1;
      var dest = Integer.parseInt(xs[5]) - 1;

      ArrayDeque<Character> d = new ArrayDeque<>();

      for (int i = 0; i < n; i++) {
        d.addLast(stacks.get(src).removeFirst());
      }

      while (!d.isEmpty()) {
        stacks.get(dest).addFirst(d.removeLast());
      }
    }

    return getItemsOnTopOfEachStack();
  }

  @Override
  public String inputFileName() {
    return "day5.txt";
  }
}
