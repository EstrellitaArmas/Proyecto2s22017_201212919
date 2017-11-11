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
@WebServlet(name = "borrarPago", urlPatterns = {"/borrarPago"})
public class borrarPago extends HttpServlet {

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
      String tarjeta = request.getParameter("tarjeta");
      
      HttpSession sesion = request.getSession(true);
      String user = sesion.getAttribute("sesionusuario").toString();
      
      RequestBody formBody = new FormEncodingBuilder()
            .add("nombreCliente",user)
            .add("tarjeta", tarjeta)
            .build();
      String res = Conexion.postString("eliminarPago", formBody);
      System.out.println(res);
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
