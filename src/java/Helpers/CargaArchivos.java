/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Helpers;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 *
 * @author estre
 */
public class CargaArchivos {
    public static void cargaContenido(String path, String nombreServicio) throws FileNotFoundException, IOException {
      
      File archivo = new File(path);
      String contenido = "";
      try {
         FileInputStream txteditor = new FileInputStream(archivo);
         int ascci;
         while ((ascci = txteditor.read()) != -1) {
            char carcater = (char) ascci;
            contenido += carcater;
         }
         System.out.println("ESTE ES EL CONTENIDO" + contenido);
         RequestBody formBody = new FormEncodingBuilder()
                 .add("xmlTexto", contenido)
                 .build();
         String r = Conexion.postString(nombreServicio, formBody);
         System.out.println(r);
         
      } catch (Exception e) {
         
      }
    } 
     
}
