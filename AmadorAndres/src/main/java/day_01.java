import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class day_01 {

	public static void main(String[] args) {
		//parte1
		int max = 0;
		
		try (BufferedReader br = new BufferedReader(new FileReader("input"))){
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
		
		//parte2
		List<Integer> totales = new LinkedList<>();
		try (BufferedReader br = new BufferedReader(new FileReader("input"))){
			int count = 0;
			String linea;
			while((linea = br.readLine()) != null) {
				if (linea.isEmpty()) {
					totales.add(count);
					count = 0;
				} else {
					int cantidad = Integer.parseInt(linea);
					count += cantidad;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		Collections.sort(totales);
		Collections.reverse(totales);
		Iterator<Integer> totalesIt = totales.iterator();
		System.out.println(totalesIt.next() + totalesIt.next() + totalesIt.next());
	}
	
}
