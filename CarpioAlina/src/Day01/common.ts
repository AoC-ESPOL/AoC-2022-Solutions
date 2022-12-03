import {getInput} from "../input";

export function getCaloriesPerElf(){
    const input = getInput('01')
    let caloriesPerElf = input.split('\n\n')
    let caloriesSplit = []
    let result: number[] = []
    let totalCalories;
    for (let c of caloriesPerElf) {
        caloriesSplit.push(c.split('\n').map(Number))
    }
    caloriesSplit.forEach((arr) => {
        totalCalories = arr.reduce((accum, current) => {
            return accum + current
        }, 0)
        result.push(totalCalories)

    })
    return result;
}