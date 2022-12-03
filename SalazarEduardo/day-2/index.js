import { exampleInput, problemInput } from './inputData.js';


const parseStrategyGuide = rawData => {
  const lines = rawData.trim().split('\n');
  return lines.map(round => round.split(' '));
};

const strategyGuide = parseStrategyGuide(problemInput);


/*
 * Day 2 - Part 1
 */

/*
 * A = X = Rock
 * B = Y = Paper
 * C = Z = Scissors
 */

const counterPerShapeV1 = { A: 'Y', B: 'Z', C: 'X' };
const equivalentPerShapeV1 = { A: 'X', B: 'Y', C: 'Z' };
const scorePerShapeV1 = { X: 1, Y: 2, Z: 3 };

const scorePerRoundV1 = strategyGuide.map(roundStrategy => {
  const opponentPlay = roundStrategy[0];
  const myPlay = roundStrategy[1];
  const shapeScore = scorePerShapeV1[myPlay];
  let roundOutcomeScore;

  if (myPlay === counterPerShapeV1[opponentPlay]) {
    roundOutcomeScore = 6; // win score
  } else if (myPlay === equivalentPerShapeV1[opponentPlay]) {
    roundOutcomeScore = 3; // draw score
  } else {
    roundOutcomeScore = 0; // loss score
  }

  return roundOutcomeScore + shapeScore;
});

const totalScoreV1 = scorePerRoundV1.reduce((acc, curr) => acc + curr);
console.log('Part 1 answer:', totalScoreV1);


/*
 * Day 2 - Part 2
 */

/*
 * A = Rock
 * B = Paper
 * C = Scissors
 * ---------------
 * X = Loss -> 0
 * Y = Draw -> 3
 * Z = Win -> 6
 */

const counterPerShapeV2 = { A: 'B', B: 'C', C: 'A' };
const scorePerRoundOutcomeV2 = { X: 0, Y: 3, Z: 6 };
const scorePerShapeV2 = { A: 1, B: 2, C: 3 };
const weaknessPerShapeV2 = { A: 'C', B: 'A', C: 'B' };

const scorePerRoundV2 = strategyGuide.map(roundStrategy => {
  const opponentPlay = roundStrategy[0];
  const expectedOutcome = roundStrategy[1];
  const roundOutcomeScore = scorePerRoundOutcomeV2[expectedOutcome];
  let myPlay;

  if (scorePerRoundOutcomeV2[expectedOutcome] === 6) {
    myPlay = counterPerShapeV2[opponentPlay];  // win shape
  } else if (scorePerRoundOutcomeV2[expectedOutcome] === 3) {
    myPlay = opponentPlay  // draw shape
  } else {
    myPlay = weaknessPerShapeV2[opponentPlay]; // loss shape
  }

  const shapeScore = scorePerShapeV2[myPlay];

  return roundOutcomeScore + shapeScore;
});

const totalScoreV2 = scorePerRoundV2.reduce((acc, curr) => acc + curr);
console.log('Part 2 answer:', totalScoreV2);
