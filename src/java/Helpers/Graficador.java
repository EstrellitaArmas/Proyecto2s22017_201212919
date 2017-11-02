/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Helpers;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author estre
 */
public class Graficador {
   
   private static List<FileJsonDTO> arbolJSP = new ArrayList<>();
   private static List<CarpetasDTO> arbolCJSP = new ArrayList<>();
   
   public static void setArbolJSP(List<FileJsonDTO> arbolJSP){
      Graficador.arbolJSP = arbolJSP;
   }
   public static List<FileJsonDTO> getArbolJSP(){
      return Graficador.arbolJSP;
   }
   public static void setArbolCJSP(List<CarpetasDTO> arbolCJSP){
      Graficador.arbolCJSP = arbolCJSP;
   }
   public static List<CarpetasDTO> getArbolCJSP(){
      return Graficador.arbolCJSP;
   }
   
   public static String path = "C:\\Users\\estre\\Desktop\\ProyectoEDD\\";
   
   public static void dibujar(String direccionDot, String direccionPng, int opcion) {
      try {
         ProcessBuilder pbuilder;

         if (opcion == 1) {
            pbuilder = new ProcessBuilder("dot", "-Tpng", "-o", path + direccionPng, path + direccionDot);

         } else {
            pbuilder = new ProcessBuilder("dot", "-Kfdp", "-n", "-Tpng", "-o", path + direccionPng, path + direccionDot);
         }

         pbuilder.redirectErrorStream(true);
         //Ejecuta el proceso
         pbuilder.start();
         System.out.println("\nGrafica  creada con exito");
         //String[] command = {"cmd","/c","start","Visualizador de fotos de Windows",  archivo.getAbsolutePath() };
         //Process process = Runtime.getRuntime().exec(command);

      } catch (Exception e) {
         e.printStackTrace();
      }
   }
}
