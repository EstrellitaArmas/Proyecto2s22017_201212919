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
import static java.lang.System.out;
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
@WebServlet(urlPatterns = {"/reservar"})
public class Reservar extends HttpServlet {

  

  
   @Override
   protected void doPost(HttpServletRequest request, HttpServletResponse response)
           throws ServletException, IOException {
      PrintWriter out = response.getWriter();
      String tarjeta = request.getParameter("tarjeta");
      String habitacion = request.getParameter("habitacion");
      String fechaIngreso = request.getParameter("fechaIngreso");
      String fechaSalida = request.getParameter("fechaSalida");
      String extras = request.getParameter("extras");
      
      HttpSession sesion = request.getSession(true);
      String user = sesion.getAttribute("sesionusuario").toString();
      
      RequestBody formBody = new FormEncodingBuilder()
            .add("nombreCliente",user)
            .add("tarjeta", tarjeta)
            .add("habitacion", habitacion)
            .add("fechaIngreso", fechaIngreso)
            .add("fechaSalida", fechaSalida)
            .add("extras", extras)
            .build();
      String res = Conexion.postString("insertarReserva", formBody);
      System.out.println(res);
      out.println(res);
      
   }

}
