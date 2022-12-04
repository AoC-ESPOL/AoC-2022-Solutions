import { exampleInput, problemInput } from './inputData.js';

const parseSectionAssignments = rawData => {
  const lines = rawData.trim().split('\n');
  return lines.map(line =>
    line.split(',').map(range =>
      range.split('-').map(sectionId => parseInt(sectionId))
    )
  );
};

const sectionAssignments = parseSectionAssignments(problemInput);


/*
 * Day 4 - Part 1
 */

const fullyContainedPairs = sectionAssignments.filter(elfPair => {
  const [ rangeElfA, rangeElfB ] = elfPair;
  const [ startA, endA ] = rangeElfA;
  const [ startB, endB ] = rangeElfB;

  return (
    (startA >= startB && endA <= endB) ||
    (startA <= startB && endA >= endB)
  );
});
console.log('Part 1 answer:', fullyContainedPairs.length);


/*
 * Day 4 - Part 2
 */

const overlappedPairs = sectionAssignments.filter(elfPair => {
  const [ rangeElfA, rangeElfB ] = elfPair;
  const [ startA, endA ] = rangeElfA;
  const [ startB, endB ] = rangeElfB;

  return (
    (startA >= startB && startA <= endB) ||
    (endA >= startB && endA <= endB) ||
    (startB >= startA && startB <= endA) ||
    (endB >= startA && endB <= endA)
  );
});
console.log('Part 2 answer:', overlappedPairs.length);
