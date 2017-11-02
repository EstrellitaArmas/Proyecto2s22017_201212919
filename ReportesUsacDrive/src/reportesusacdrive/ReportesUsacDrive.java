/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reportesusacdrive;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import static reportesusacdrive.Reportes.dibujar;

/**
 *
 * @author estre
 */
public class ReportesUsacDrive {

   /**
    * @param args the command line arguments
    */
   public static String path = "C:\\Users\\estre\\Desktop\\ProyectoEDD\\";
   public static void main(String[] args) {
      
      // a jframe here isn't strictly necessary, but it makes the example a little more real
      JFrame frame = new JFrame("InputDialog Example #1");
      String usuario = JOptionPane.showInputDialog(frame, "Ingresar nombre de usuario");
      usuario = usuario.toLowerCase();
//      //Caja de texto para ingresa nombre de usuario aqui
      
      Reportes reportes = new Reportes(usuario,path);
      reportes.setVisible(true);
   }
   
}
