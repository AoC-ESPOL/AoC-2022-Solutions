import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class day_02 {
	public static void main(String[] args) {
		//parte1
		int total = 0;
		
		Map<Character, Integer> valorFigura = new HashMap<>();
		valorFigura.put('A', 1);
		valorFigura.put('B', 2);
		valorFigura.put('C', 3);
		
		Map<Character, Character> cambioDeCaracter = new HashMap<>();
		cambioDeCaracter.put('X', 'A');
		cambioDeCaracter.put('Y', 'B');
		cambioDeCaracter.put('Z', 'C');
		
		try (BufferedReader br = new BufferedReader(new FileReader("input"))){
			String line;
			while((line = br.readLine()) != null) {
				
				char enemigo = line.charAt(0);
				char yo = line.charAt(2);
				
				yo = cambioDeCaracter.get(yo);
				
				total += valorFigura.get(yo);
				
				
				switch (checkResult(enemigo, yo)) {
				case 0:
					total += 3;
					break;
				case 1:
					total += 6;
					break;
				case -1:
					break;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println(total);
		
		//parte2
		total = 0;
		Map<Character, Character> ganadores = new HashMap<>();
		ganadores.put('A', 'B');
		ganadores.put('B', 'C');
		ganadores.put('C', 'A');
		
		try (BufferedReader br = new BufferedReader(new FileReader("input"))){
			String line;
			while((line = br.readLine()) != null) {
				char enemigo = line.charAt(0);
				char resultado = line.charAt(2);
				
				char yo = obtenerMiFigura(enemigo, resultado, ganadores);
				
				total += valorFigura.get(yo);
				
				
				switch (checkResult(enemigo, yo)) {
				case 0:
					total += 3;
					break;
				case 1:
					total += 6;
					break;
				case -1:
					break;
				}
				
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println(total);
		
	}
	
	private static int checkResult(char enemigo, char yo) {
		if (yo == enemigo) {
			return 0;
		}
		int valor;
		switch (yo) {
		case 'A':
			valor = (enemigo == 'C') ? 1 : -1;
			break;
		case 'B':
			valor = (enemigo == 'A') ? 1 : -1;
			break;
		case 'C':
			valor = (enemigo == 'B') ? 1 : -1;
			break;
		default:
			throw new IllegalArgumentException();
		}
		return valor;
	}
	
	private static char obtenerMiFigura(char enemigo, char resultado, Map<Character, Character> ganadores) {
		if (resultado == 'Y') {
			return enemigo;
		} else if (resultado == 'Z') {
			return ganadores.get(enemigo);
		} else {
			Map<Character, Character> perdedores = new HashMap<>();
			ganadores.forEach((Character k, Character v) -> {
				perdedores.put(v, k);
			});
			return perdedores.get(enemigo);
		}
	}
}
