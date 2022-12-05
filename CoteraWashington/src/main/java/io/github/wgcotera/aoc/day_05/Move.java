package io.github.wgcotera.aoc.day_05;

public class Move {
    int from;
    int to;
    int quantity;

    public Move(int quantity, int from, int to) {
        this.quantity = quantity;
        this.from = from;
        this.to = to;
    }

    @Override
    public String toString() {
        return "Move{" + "quantity=" + quantity + ", from=" + from + ", to=" + to + "}";
    }
}
