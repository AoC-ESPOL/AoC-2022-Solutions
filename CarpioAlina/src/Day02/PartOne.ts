import {getInput} from '../common'

const X = 1 //PIEDRA
const Y = 2 //PAPEL
const Z = 3 //TIJERA

const EMPATE = 3
const PIERDE = 0
const GANA = 6


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
        suma += actual;

        console.log(partida[0], partida[1], suma)
    })

    return suma
}


function getState(oponent: string, reason: string): number {
    switch (oponent) {
        case 'A':
            if (reason === 'X') return EMPATE + X
            if (reason === 'Y') return GANA + Y
            if (reason === 'Z') return PIERDE + Z
            break
        case 'B':
            if (reason === 'X') return PIERDE + X
            if (reason === 'Y') return EMPATE + Y
            if (reason === 'Z') return GANA + Z
            break
        case 'C':
            if (reason === 'X') return GANA + X
            if (reason === 'Y') return PIERDE + Y
            if (reason === 'Z') return EMPATE + Z
            break
        default:
            return 0
    }
    return 0
}
