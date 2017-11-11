/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Menu;

import Helpers.Conexion;
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

/**
 *
 * @author estre
 */
@WebServlet( urlPatterns = {"/modificarInformacion"})
public class modificarInformacion extends HttpServlet {

   
   /**
    * Handles the HTTP <code>POST</code> method.
    *
    * @param request servlet request
    * @param response servlet response
    * @throws ServletException if a servlet-specific error occurs
    * @throws IOException if an I/O error occurs
    */
   @Override
   protected void doPost(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      
      PrintWriter out = response.getWriter();
      String habitacion = request.getParameter("habitacion");
      String idFechaIngreso = request.getParameter("idFechaIngreso");
      String fechaSalida = request.getParameter("fechaSalida");
      String total = request.getParameter("total");
      String nuevoNombre = request.getParameter("nuevoNombre");
      
      RequestBody formBody = new FormEncodingBuilder()
            .add("nuevoNombre",nuevoNombre)
            .add("habitacion", habitacion)
            .add("idFechaIngreso", idFechaIngreso)
            .add("fechaSalida", fechaSalida)
            .add("total", total)
            .build();
      String res = Conexion.postString("modificarHistoria", formBody);
      System.out.println("RESPUESTA DE SERVIDOR" +res);
      out.println(res);
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
