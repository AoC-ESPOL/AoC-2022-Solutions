import { getInput } from '../common'
import { getCaloriesPerElf} from '../common'


export default function solution() {
  const result = getCaloriesPerElf();
 
  const max = result.reduce((a, b) => Math.max(a, b), -Infinity)

  return max
}


