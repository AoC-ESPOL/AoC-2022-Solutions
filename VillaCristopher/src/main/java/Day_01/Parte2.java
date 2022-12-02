package Day_01;

import java.util.ArrayList;
import java.util.Collections;

public class Parte2 {

    public static int total_3Max(ArrayList<Integer> lista){
        int contador=0;
        lista.sort((i1,i2)->{
            return i2 - i1;
        });
        for(int i = 0 ; i<3;i++){
            contador+= lista.get(i);
        }
        return contador;
    }

    public static void main(String[] args) {
        System.out.println(total_3Max(Parte1.obtenerTotales()));
    }
}
