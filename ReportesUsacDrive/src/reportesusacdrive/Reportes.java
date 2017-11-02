/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reportesusacdrive;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JTextArea;

/**
 *
 * @author estre
 */
public class Reportes extends javax.swing.JFrame {
    
     String bitacora = Conexion.getString("bitacora");
    
    JLabel grafoPalabrasPNG = new JLabel(" ");
    JTextArea grafoBitacoraPNG = new JTextArea(" ");
    JLabel grafoUsuariosPNG = new JLabel(" ");
    JLabel grafoCarpetasPNG = new JLabel(" ");
    JLabel grafoArchivosPNG = new JLabel(" ");
    public Reportes(){
       initComponents();
    }
    public Reportes(String usuario , String path) { 
    
      initComponents();   
  
      imagenes(usuario, path);
    
    }
    public static void dibujar(String direccionDot, String direccionPng, int opcion) {
      try {
         ProcessBuilder pbuilder;

         if (opcion == 1) {
            pbuilder = new ProcessBuilder("dot", "-Tpng", "-o", direccionPng, direccionDot);

         } else {
            pbuilder = new ProcessBuilder("dot", "-Kfdp", "-n", "-Tpng", "-o", direccionPng, direccionDot);
         }

         pbuilder.redirectErrorStream(true);
         //Ejecuta el proceso
         pbuilder.start();
         System.out.println("Grafica  creada con exito");
         //String[] command = {"cmd","/c","start","Visualizador de fotos de Windows",  archivo.getAbsolutePath() };
         //Process process = Runtime.getRuntime().exec(command);

      } catch (Exception e) {
         e.printStackTrace();
      }
   }
    private void imagenes(String usuario, String path){
        //Imagenes en el tablero
    
      ImageIcon imageCarpetas = new ImageIcon(path + "arbolB"+usuario+".png");
      grafoCarpetasPNG.setIcon(imageCarpetas);
      grafoCarpetasPNG.setSize(450, 600);
      grafoCarpetasPNG.setLocation(0, 0);
      grafoCarpetasPNG.setVisible(true);
      panelCarpetas.setViewportView(grafoCarpetasPNG);
        
      ImageIcon imageArchivos = new ImageIcon(path + "arbolAVL"+usuario+".png");        
      grafoArchivosPNG.setIcon(imageArchivos);
      grafoArchivosPNG.setSize(450,600);               
      grafoArchivosPNG.setLocation(0,0);
      grafoArchivosPNG.setVisible(true); 
      panelArchivos.setViewportView(grafoArchivosPNG); 
      
      //añade imagen de lista de jugadores        
        grafoBitacoraPNG.setText(bitacora);
        grafoBitacoraPNG.setSize(450,600);
        grafoBitacoraPNG.setLocation(0,0);
        grafoBitacoraPNG.setVisible(true); 
        grafoBitacoraPNG.setEditable(false);
        panelBitacora.add(grafoBitacoraPNG); 
        
         //añade imagen de lista de jugadores        
        ImageIcon imageUsuarios = new ImageIcon(path + "listaUsuarios.png");
        grafoUsuariosPNG.setIcon(imageUsuarios);
        grafoUsuariosPNG.setSize(450,600);
        grafoUsuariosPNG.setLocation(0,0);
        grafoUsuariosPNG.setVisible(true); 
        panelUsuarios.add(grafoUsuariosPNG); 
     
        this.hide();
        this.repaint();
        this.show();
    }
   
    @SuppressWarnings("unchecked")
   // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
   private void initComponents() {

      jTabbedPane1 = new javax.swing.JTabbedPane();
      tabPanels = new javax.swing.JTabbedPane();
      panelArchivos = new javax.swing.JScrollPane();
      panelCarpetas = new javax.swing.JScrollPane();
      panelBitacora = new javax.swing.JPanel();
      panelUsuarios = new javax.swing.JPanel();

      setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

      tabPanels.setAutoscrolls(true);
      tabPanels.addTab("Archivos", panelArchivos);
      tabPanels.addTab("Carpetas", panelCarpetas);

      javax.swing.GroupLayout panelBitacoraLayout = new javax.swing.GroupLayout(panelBitacora);
      panelBitacora.setLayout(panelBitacoraLayout);
      panelBitacoraLayout.setHorizontalGroup(
         panelBitacoraLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGap(0, 1292, Short.MAX_VALUE)
      );
      panelBitacoraLayout.setVerticalGroup(
         panelBitacoraLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGap(0, 652, Short.MAX_VALUE)
      );

      tabPanels.addTab("Bitacora", panelBitacora);

      javax.swing.GroupLayout panelUsuariosLayout = new javax.swing.GroupLayout(panelUsuarios);
      panelUsuarios.setLayout(panelUsuariosLayout);
      panelUsuariosLayout.setHorizontalGroup(
         panelUsuariosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGap(0, 1292, Short.MAX_VALUE)
      );
      panelUsuariosLayout.setVerticalGroup(
         panelUsuariosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGap(0, 652, Short.MAX_VALUE)
      );

      tabPanels.addTab("Usuarios", panelUsuarios);

      javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
      getContentPane().setLayout(layout);
      layout.setHorizontalGroup(
         layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGroup(layout.createSequentialGroup()
            .addComponent(tabPanels, javax.swing.GroupLayout.PREFERRED_SIZE, 1297, javax.swing.GroupLayout.PREFERRED_SIZE)
            .addGap(0, 10, Short.MAX_VALUE))
      );
      layout.setVerticalGroup(
         layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGroup(layout.createSequentialGroup()
            .addComponent(tabPanels, javax.swing.GroupLayout.PREFERRED_SIZE, 680, javax.swing.GroupLayout.PREFERRED_SIZE)
            .addGap(0, 3, Short.MAX_VALUE))
      );

      pack();
   }// </editor-fold>//GEN-END:initComponents

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Reportes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Reportes().setVisible(true);
            }
        });
    }

   // Variables declaration - do not modify//GEN-BEGIN:variables
   private javax.swing.JTabbedPane jTabbedPane1;
   private javax.swing.JScrollPane panelArchivos;
   public javax.swing.JPanel panelBitacora;
   private javax.swing.JScrollPane panelCarpetas;
   public javax.swing.JPanel panelUsuarios;
   public javax.swing.JTabbedPane tabPanels;
   // End of variables declaration//GEN-END:variables
}
