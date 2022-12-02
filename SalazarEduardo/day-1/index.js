import { exampleInput, problemInput } from './inputData.js';


/*
 * Day 1 - Part 1
 */;

const parseCaloriesPerElf = rawData => {
  const elfsNotes = rawData.trim().split('\n\n');
  const elfsCalories = elfsNotes.map(note => {
    const lines = note.split('\n');
    const calories = lines.map(line => parseInt(line));
    return calories;
  });
  return elfsCalories;
};

const caloriesPerElf = parseCaloriesPerElf(problemInput);

const totalCaloriesPerElf = caloriesPerElf.map(singleElfCalories => {
  return singleElfCalories.reduce((acc, curr) => acc + curr);
});
const maxElfCalories = Math.max(...totalCaloriesPerElf);
console.log('Part 1 answer:', maxElfCalories);


/*
 * Day 1 - Part 2
 */;

const totalCaloriesPerElfSorted = totalCaloriesPerElf.sort((a, b) => a - b);
const top3TotalCaloriesPerElf = totalCaloriesPerElfSorted.slice(-3);
const top3SumOfCalories = top3TotalCaloriesPerElf.reduce((acc, curr) => acc + curr);
console.log('Part 2 answer:', top3SumOfCalories);


/*
 * Day 1 - Heuristic Method
*/;

const getTopTotalCalories = (caloriesPerElf, topSize) => {
  let topTotalCalories = new Array(topSize).fill(0);

  caloriesPerElf.forEach(singleElfCalories => {
    const elfTotalCalories = singleElfCalories.reduce((acc, curr) => acc + curr);
    const currentArray = [ elfTotalCalories, ...topTotalCalories ].sort((a, b) => a - b);

    topTotalCalories = [
      ...currentArray.slice(-1 * (topSize))
    ];
  });
  return topTotalCalories;
};

const answer1 = getTopTotalCalories(caloriesPerElf, 1)[0];
const answer2 = getTopTotalCalories(caloriesPerElf, 3).reduce((acc, curr) => acc + curr);

console.log('--- Heuristic Method ---');
console.log('Part 1 answer:', answer1);
console.log('Part 2 answer:', answer2);
