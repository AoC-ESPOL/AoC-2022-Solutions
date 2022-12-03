import {expect, test} from "vitest";
import solution from "./PartTwo";

test("Test with examples", () => {
    const input = `A Y
B X
C Z`
    expect(solution(input)).toBe(12)
})