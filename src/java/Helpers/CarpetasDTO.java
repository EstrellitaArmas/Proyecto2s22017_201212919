/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Helpers;

import java.util.List;

/**
 *
 * @author estre
 */
public class CarpetasDTO extends BaseDTO {
   private int idCarpeta;

   private String nombreCarpeta;

   private List<FileJsonDTO> archivos;
   
   public String getNombreCarpeta() {
      return nombreCarpeta;
   }

   public void setNombreCarpeta(String nombreCarpeta) {
      this.nombreCarpeta = nombreCarpeta;
   }

   public int getIdCarpeta() {
      return idCarpeta;
   }

   public void setIdCarpeta(int idCarpeta) {
      this.idCarpeta = idCarpeta;
   }
   
   public void setArchivos(List<FileJsonDTO> archivos){
      this.archivos = archivos;
   }
   
   public List<FileJsonDTO> getArchivos(){
      return archivos;
   }
//{
   //"idNombre": 30,
   //"arbolAVL": {
   //    "raiz": null,
   //    "byteFile": null
   //},
   //"nombreCarpeta": "Videos",
   //"raizB": null
//}   
}
