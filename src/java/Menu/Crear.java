/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Menu;

import Helpers.CarpetasDTO;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Helpers.Conexion;
import Helpers.FileJsonDTO;
import Helpers.ParserJson;
import Helpers.Graficador;
import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.List;
import javax.servlet.annotation.MultipartConfig;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
/**
 *
 * @author estre
 */
@WebServlet(name = "Crear", urlPatterns = {"/crear"})
@MultipartConfig
public class Crear extends HttpServlet {

   
   protected void processRequest(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      response.setContentType("text/html;charset=UTF-8");
      try (PrintWriter out = response.getWriter()) {
         /* TODO output your page here. You may use following sample code. */
         out.println("<!DOCTYPE html>");
         out.println("<html>");
         out.println("<head>");
         out.println("<title>Servlet Crear</title>");         
         out.println("</head>");
         out.println("<body>");
         out.println("<h1>Servlet Crear at " + request.getContextPath() + "</h1>");
         out.println("</body>");
         out.println("</html>");
      }
   }

   String r = "";
    
   @Override
   protected void doPost(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      List<FileJsonDTO> itemsTree =  Graficador.getArbolJSP();
      List<CarpetasDTO> itemsCarpetaTree =  Graficador.getArbolCJSP();
      HttpSession sesion = request.getSession(true);
      String user = sesion.getAttribute("sesionusuario").toString();
      String nombreCarpeta = "raiz";
      try{
         FileItemFactory factory = new DiskFileItemFactory();
         ServletFileUpload upload = new ServletFileUpload(factory);
         // Los items obtenidos serán cada uno de los campos del formulario, tanto campos normales como ficheros subidos.
         List items = upload.parseRequest(request);         
         // Se recorren todos los items, que son de tipo FileItem
         for (Object item : items){
            FileItem uploaded = (FileItem) item;
            String nom = uploaded.getFieldName();
            if (nom.equals("nomCarpeta")) {
               nombreCarpeta = uploaded.getString();
               System.out.println("nombrecarpeta------" + uploaded.getString());
            }
            
         }
         for (Object item : items) {
            FileItem uploaded = (FileItem) item;
            FileJsonDTO fileJson = new FileJsonDTO();
            String fileJsonStr = "";
            // Hay que comprobar si es un campo de formulario. Si no lo es, se guarda el fichero subido donde nos interese
            if (!uploaded.isFormField()) {
               try {
                  // Con este código se obtienen los bytes del archivo.
                  BufferedInputStream input = new BufferedInputStream(uploaded.getInputStream());
                  byte[] fileArray = new byte[(int) uploaded.getSize()];
                  input.read(fileArray); // el contenido leido se almacena en el array de bytes
                  input.close();
                  
                  //Se almacena el array de bytes y el nombre en un objeto
                  fileJson.setFileBytes(fileArray);
                  fileJson.setFileName(uploaded.getName());
                  fileJson.setUser(user);
                  fileJson.setNombreCarpeta(nombreCarpeta);
                  fileJson.setIdCarpeta(nombreCarpeta.hashCode());
                  itemsTree.add(fileJson); 
                  
                  //se envia hacia servidor 
                  //Se convierte el objeto en un string tipo Json
                  fileJsonStr = ParserJson.parseObjectToStr(fileJson);
                 // System.out.println("bytes del archivo: " + fileJsonStr);
                  RequestBody formBody = new FormEncodingBuilder()
                          .add("fileJsonStr", fileJsonStr)
                          .build();
                  r = Conexion.postString("insertarArchivo", formBody);
                  System.out.println("fichero guardado con exito");
                  Graficador.dibujar("arbolB" + user + ".dot",  "arbolB" + user + ".png", 1);
                  Graficador.dibujar("arbolAVL" + user + ".dot", "arbolAVL" + user + ".png", 1);
              
               } catch (Exception e) {
                   System.out.println("ERROR EN OBTENER BYTES: "+ e);
               }
               
            } else {
            }            
         }                  
         String lblArchivo = "";
         String lblCarpeta = "";
         for (CarpetasDTO carpeta : itemsCarpetaTree){
            if(carpeta.getUser().equalsIgnoreCase(user)){
               lblCarpeta += "<option class=\"btn btn-link\" value=\""+carpeta.getNombreCarpeta()+"\">"+
                              "<i class=\"fa fa-folder\">&nbsp;"+carpeta.getNombreCarpeta()+"</i>"+
                             "</option>";
            }
         }  
         for (FileJsonDTO file : itemsTree){
            if(file.getUser().equalsIgnoreCase(user)){
               lblArchivo += "<option class=\"btn btn-link\" name=\"" + file.getFileName() + "\" value=\"" + file.getFileName() + "\"><i class=\"fa fa-file\">&nbsp;" + file.getFileName() + "</i></option>";
            }
         }  
         Graficador.setArbolJSP(itemsTree);
         sesion.setAttribute("arbolArchivos", lblArchivo);
         sesion.setAttribute("arbolCarpetas", lblCarpeta);
         response.sendRedirect("Menu.jsp");  
         
      }catch(Exception e){
         System.out.println("ERROR: "+ e);
      }     
   }

   /**
    * Returns a short description of the servlet.
    *
    * @return a String containing servlet description
    */
   @Override
   public String getServletInfo() {
      return "Short description";
   }// </editor-fold>

}
