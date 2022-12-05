package io.github.wgcotera.aoc.day_05;

import java.util.ArrayList;
import java.util.List;

public class Stack {
    int name;
    List<String> content;

    public Stack(int name, List<String> content) {
        this.name = name;
        this.content = content;
    }

    public Stack(int name) {
        this.name = name;
        this.content = new ArrayList<>();
    }

    public Stack addElementToStack(List<String> elements) {
        content.addAll(elements);
        return this;
    }

    public List<String> removeCratesFromStackOneByOne(int quantity) {

        List<String> removedElements = new ArrayList<>();
        for (int i = 0; i < quantity; i++) {
            removedElements.add(content.remove(content.size() - 1));
        }
        return removedElements;

    }

    public List<String> removeGroupOfCratesFromStack(Stack stack, int quantity) {

        ArrayList<String> removedElements = new ArrayList<>();

        for (int i = 0; i < quantity; i++) {
            removedElements.add(stack.content.remove(stack.content.size() - quantity + i));
        }
        return removedElements;

    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Stack stack = (Stack) o;
        return name == stack.name;
    }

    @Override
    public String toString() {
        return "Stack{" + "name=" + name + ", content=" + content + '}';
    }
}
