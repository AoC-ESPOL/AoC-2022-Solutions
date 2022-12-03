import {calculateScore} from "./common";

const EMPATE = 3
const PIERDE = 0
const GANA = 6

const A = 1
const B = 2
const C = 3


export default function solution(input: string) {
    return calculateScore(input, getState)
}


function getState(oponent: string, objetivo: string): number {
    switch (objetivo) {
        case 'X':
            if (oponent === 'A') return PIERDE + C
            if (oponent === 'B') return PIERDE + A
            if (oponent === 'C') return PIERDE + B
            break
        case 'Y':
            if (oponent === 'A') return EMPATE + A
            if (oponent === 'B') return EMPATE + B
            if (oponent === 'C') return EMPATE + C
            break

        case 'Z':
            if (oponent === 'A') return GANA + B
            if (oponent === 'B') return GANA + C
            if (oponent === 'C') return GANA + A
            break
        default:
            return 0
    }
    return 0
}
