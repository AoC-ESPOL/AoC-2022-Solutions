import { exampleInput, problemInput } from './inputData.js';

const parseRucksacks = rawData => rawData.trim().split('\n');
const rucksacks = parseRucksacks(problemInput);


/*
 * Day 3 - Part 1
 */

const getRucksackCompartments = rucksacks => {
  return rucksacks.map(items => {
    const rucksackLength = items.length;
    const midIndex = rucksackLength / 2;
    const firstCompartment = items.slice(0, midIndex);
    const secondCompartment = items.slice(midIndex, rucksackLength);

    return [ firstCompartment, secondCompartment ];
  });
};

const isItemRepeatedInCompartments = (item, compartments) => {
  const compartmentsLength = compartments.length;
  if (compartmentsLength === 1) {
    return compartments[0].includes(item);
  } else if (compartmentsLength > 1) {
    const restCompartments = compartments.slice(1, compartmentsLength);
    return compartments[0].includes(item) && isItemRepeatedInCompartments(item, restCompartments);
  }

  return false;  // compartments is empty
};

const getRepeatedItemInCompartments = (myCompartment, otherCompartments) => {
  let repeatedItem = null;

  for (let itemIndex = 0; itemIndex < myCompartment.length; itemIndex+=1) {
    const item = myCompartment[itemIndex];

    if (isItemRepeatedInCompartments(item, otherCompartments)) {
      repeatedItem = item;
      break;
    }
  }

  return repeatedItem;
};

const getItemPriorities = items => items.map(item => {
  return (item === item.toLowerCase())
    ? item.charCodeAt(0) - 96
    : item.charCodeAt(0) - 38;
});

const splittedRucksacks = getRucksackCompartments(rucksacks);

const misplacedItems = splittedRucksacks.map(rucksack => {
  const firstCompartment = rucksack[0];
  const secondCompartment = rucksack[1];

  return getRepeatedItemInCompartments(firstCompartment, [ secondCompartment ]);
});

const misplacedItemPriorities = getItemPriorities(misplacedItems);
const misplacedPrioritiesSum = misplacedItemPriorities.reduce((acc, curr) => acc + curr);
console.log('Part 1 answer:', misplacedPrioritiesSum);


/*
 * Day 3 - Part 2
 */

const getSmallestRucksackIndex = rucksacksArray => {
  let smallestRucksackSize = Number.MAX_SAFE_INTEGER;
  let smallestRucksackIndex = 0;

  rucksacksArray.forEach((rucksack, index) => {
    const currentRucksackSize = rucksack.length;

    if (currentRucksackSize < smallestRucksackSize) {
      smallestRucksackSize = currentRucksackSize;
      smallestRucksackIndex = index;
    }
  });

  return smallestRucksackIndex;
};

const badgeItems = [];

for (let rucksackIndex = 0; rucksackIndex < rucksacks.length; rucksackIndex += 3) {
  const rucksacksGroup = rucksacks.slice(rucksackIndex, rucksackIndex + 3);
  const smallestRucksackIndex = getSmallestRucksackIndex(rucksacksGroup);
  const smallestRucksack = rucksacksGroup[smallestRucksackIndex];
  const biggestRucksacks = rucksacksGroup.filter((_, index) => index !== smallestRucksackIndex);

  const repeatedItem = getRepeatedItemInCompartments(smallestRucksack, biggestRucksacks);
  repeatedItem && badgeItems.push(repeatedItem);
}

const badgePriorities = getItemPriorities(badgeItems);
const badgePrioritiesSum = badgePriorities.reduce((acc, curr) => acc + curr);
console.log('Part 2 answer:', badgePrioritiesSum);
