package main;

import java.util.Scanner;

public class AnalizadorLexico {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        System.out.println(">>> Número de lineas: ");
        String[] input = new String[s.nextInt()];
        s.nextLine();

        String strarr = "";

        System.out.println("Escriba el programa: ");

        for (int i = 0; i < input.length; i++){
            input[i] = s.nextLine();
            strarr += input[i];
        }

        System.out.println("\n Linea de entrada: ");

        String output[] = strarr.split(" ");

        for (String output1 : output) {
            System.out.print(" " + output1);
        }

        System.out.println("");

        int id = 0, tokenNo = 0;

        for (int i = 0; i < output.length; i++) {

            if (null != output[i])
                switch (output[i]) {
                    case "Hilera":
                    case "ent":
                    case "flotante":
                    case "doble":
                    case "booleano":
                        tokenNo++;
                        System.out.println("<palabraClave," + output[i] + ">");
                        break;
                    case "+":
                    case "-":
                    case "*":
                    case "%":
                    case "=":
                    case "<":
                    case ">":
                    case "**":
                    case "<<":
                    case ">>":
                    case "&&":
                    case "||":
                    case "<=":
                    case ">=":
                        tokenNo++;
                        System.out.println("<operador," + output[i] + ">");
                        break;
                    case "20":
                    case "1":
                    case "2":
                    case "3":
                    case "4":
                        tokenNo++;
                        System.out.println("<num," + output[i] + ">");
                        break;
                    case "a":
                    case "b":
                    case "c":
                    case "d":
                    case "e":
                        tokenNo++;
                        id++;
                        System.out.println("<iden " + id + ", " + output[i] + " >");
                        break;
                    case ",":
                        tokenNo++;
                        System.out.println("<separador, " + output[i] + ">");
                        break;
                    case ";":
                        tokenNo++;
                        System.out.println("<finDeEnunciado, " + output[i] + ">");
                        break;
                    default: System.out.println(output[i] + "tipo desconocido");
                    break;
                }
        }
        System.out.println("Numero total de tokens: " + tokenNo);
    }
}
