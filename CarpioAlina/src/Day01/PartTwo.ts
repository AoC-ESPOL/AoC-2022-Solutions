import { getCaloriesPerElf} from '../common'

let result = getCaloriesPerElf();
export default function solution() {
  result.sort((a,b) => b - a);
  
  return result[0] + result[1] + result[2]
}
