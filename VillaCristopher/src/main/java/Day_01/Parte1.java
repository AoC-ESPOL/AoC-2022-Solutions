package Day_01;

import java.io.*;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Parte1 {
    public static ArrayList<String> leerArchivo() {
        ArrayList<String> lista = new ArrayList<>();
        File file = new File(
                "src/main/resources/datosDay01.txt");
        BufferedReader br;
        {
            try {
                br = new BufferedReader(new FileReader(file));
                String st;
                while ((st = br.readLine()) != null)
                    lista.add(st);

            } catch (FileNotFoundException e) {
                throw new RuntimeException(e);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return lista;
    }

    public static ArrayList<Integer> obtenerTotales(){
        ArrayList<String> lista = leerArchivo();
        ArrayList<Integer> totales = new ArrayList<>();
        int contador=0;
        for(String s : lista){
            if(!s.equals("")){
                int valor = Integer.parseInt(s);
                contador+=valor;
            }else {
                totales.add(contador);
                contador =0;
            }
        }
        return totales;
    }

    public static void main(String[] args) {
        System.out.println(Collections.max(obtenerTotales()));
    }
}

