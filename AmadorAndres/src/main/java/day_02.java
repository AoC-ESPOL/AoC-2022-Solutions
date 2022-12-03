import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class day_02 {
	public static void main(String[] args) {
		//parte1
		int total = 0;
		
		HashMap<Character, Integer> valorFigura = new HashMap<>();
		valorFigura.put('X', 1);
		valorFigura.put('Y', 2);
		valorFigura.put('Z', 3);
		
		HashMap<Character, Character> cambioDeCaracter = new HashMap<>();
		cambioDeCaracter.put('A', 'X');
		cambioDeCaracter.put('B', 'Y');
		cambioDeCaracter.put('C', 'Z');
		
		try (BufferedReader br = new BufferedReader(new FileReader("src/main/resources/input/input2.txt"))){
			String line;
			while((line = br.readLine()) != null) {
				
				char enemigo = line.charAt(0);
				char yo = line.charAt(2);
				
				total += valorFigura.get(yo);
				
				enemigo = cambioDeCaracter.get(enemigo);
				
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
		case 'X':
			valor = (enemigo == 'Z') ? 1 : -1;
			break;
		case 'Y':
			valor = (enemigo == 'X') ? 1 : -1;
			break;
		case 'Z':
			valor = (enemigo == 'Y') ? 1 : -1;
			break;
		default:
			throw new IllegalArgumentException();
		}
		return valor;
	}
}
