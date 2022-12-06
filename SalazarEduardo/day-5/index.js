import { exampleInput, problemInput } from './inputData.js';

const parsePuzzleInput = rawData => {
  const [ cratesStacksNotes, rearrangementStepsNotes ] = rawData.split('\n\n');
  const cratesStacks = parseCratesStacksNotes(cratesStacksNotes);
  const rearrangementSteps = parseRearrangementStepsNotes(rearrangementStepsNotes);

  return [ cratesStacks, rearrangementSteps ];
};

const parseCratesStacksNotes = cratesStacksNotes => {
  const cratesStacksLines = cratesStacksNotes.split('\n');
  const cratesStackIds = cratesStacksLines.pop().trim().split('   ');
  const cratesStacks = {};

  cratesStackIds.forEach(stackId => cratesStacks[stackId] = []);

  cratesStacksLines.forEach(line => {
    if (line.length === 0) {
      return;
    }
    
    cratesStackIds.forEach((stackId, index) => {
      const charIndex = index * 4;
      const stackCrate = line.slice(charIndex, charIndex + 3).replace(/\[|\]| /g, '');
      stackCrate && cratesStacks[stackId].unshift(stackCrate);
    });
  });

  return cratesStacks;
};

const parseRearrangementStepsNotes = rearrangementProcedureNotes => {
  const rearrangementStepsLines = rearrangementProcedureNotes.trim().split('\n');

  const rearrangementSteps = rearrangementStepsLines.map(line => {
    const step = {};
    const [ moveValue, fromValue, toValue ] = line.replace(
      /move |from |to /gi, ''
    ).split(' ');

    step['move'] = parseInt(moveValue);
    step['from'] = fromValue;
    step['to'] = toValue;

    return step;
  });

  return rearrangementSteps;
};

const [ cratesStacks, rearrangementSteps ] = parsePuzzleInput(problemInput);

/*
 * Day 5 - Part 1
 */

const cratesStacksV1 = JSON.parse(JSON.stringify(cratesStacks));  // Deep copy of cratesStacks

rearrangementSteps.forEach(step => {
  const { move, from, to } = step;

  for (let movementIndex = 0; movementIndex < move; movementIndex += 1) {
    const crateToMove = cratesStacksV1[from].pop();
    cratesStacksV1[to].push(crateToMove);
  }
});

const topCratesV1 = Object.keys(cratesStacksV1).map(key => {
  const cratesStack = cratesStacksV1[key];
  return cratesStack[cratesStack.length - 1];
});

console.log('Part 1 answer:', topCratesV1.join(''));

/*
 * Day 5 - Part 2
 */

const cratesStacksV2 = JSON.parse(JSON.stringify(cratesStacks));  // Deep copy of cratesStacks

rearrangementSteps.forEach(step => {
  const { move, from, to } = step;

  const crateStack = cratesStacksV2[from];
  const crateToMove = crateStack.splice(crateStack.length - move, move);
  cratesStacksV2[to].push(...crateToMove);
});

const topCratesV2 = Object.keys(cratesStacksV2).map(key => {
  const cratesStack = cratesStacksV2[key];
  return cratesStack[cratesStack.length - 1];
});

console.log('Part 2 answer:', topCratesV2.join(''));
