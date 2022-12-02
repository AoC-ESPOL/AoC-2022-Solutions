import { getInput } from '../common'

const totalCalories = 0
const current = 0

export default function solution() {
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
 
  
  const max = result.reduce((a, b) => Math.max(a, b), -Infinity)

  return max
}
