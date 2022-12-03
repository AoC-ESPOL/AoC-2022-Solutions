import { expect, test} from "vitest";
import {getInput} from "../input";
import solution from "./PartOne";

test("Test with example input works", () => {
    const input =`A Y
B X
C Z
    `
    expect(solution(input)).toBe(15)
})

test("Test solution works with real input", () => {
    const input = getInput("02");
    expect(solution(input)).toBe(12855)
})