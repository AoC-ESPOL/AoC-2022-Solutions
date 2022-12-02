import * as fs from 'fs'

export function getInput(inputName: string): string {
  return fs.readFileSync(`puzzle_inputs/${inputName}.txt`, {
    encoding: 'utf-8',
  })
}
