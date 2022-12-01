import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class day_01 {

	public static void main(String[] args) {
		int max = 0;
		
		try (BufferedReader br = new BufferedReader(new FileReader("src/main/resources/input/input1.txt"))){
			int count = 0;
			String linea;
			while((linea = br.readLine()) != null) {
				if (linea.isEmpty()) {
					if(count > max) {
						max = count;
					}
					count = 0;
				} else {
					int cantidad = Integer.parseInt(linea);
					count += cantidad;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println(max);
	}
	
}
