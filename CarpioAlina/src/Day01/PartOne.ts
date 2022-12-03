
import { getCaloriesPerElf} from './common'


export default function solution() {
  const result = getCaloriesPerElf();
  return  result.reduce((a, b) => Math.max(a, b), -Infinity)
}


