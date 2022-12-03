import * as fs from 'fs'

export type Day = '01' | '02';

export function getInput(inputName: Day): string {
  return fs.readFileSync(`puzzle_inputs/${inputName}.txt`, {
    encoding: 'utf-8',
  })
}
