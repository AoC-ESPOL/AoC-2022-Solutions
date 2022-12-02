const EMPATE = 3
const PIERDE = 0
const GANA = 6

const A = 1
const B = 2
const C = 3

import {getInput} from '../common'

export default function solution() {
    const input = getInput('02')
    const partidas = input.split('\n')
    let result: Array<Array<string>> = []
    let actual = 0
    let suma = 0

    partidas.forEach((partida) => {
        result.push(partida.split(' '))
    })

    result.forEach((partida) => {
        actual = getState(partida[0], partida[1])
        suma += actual

        console.log(partida[0], partida[1], suma)
    })

    return suma
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
