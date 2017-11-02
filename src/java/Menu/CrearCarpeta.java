package Menu;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Helpers.Conexion;
import Helpers.ParserJson;
import Helpers.CarpetasDTO;
import Helpers.Graficador;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.util.List;
import javax.servlet.http.HttpSession;

@WebServlet(urlPatterns = {"/crearCarpeta"})
public class CrearCarpeta extends HttpServlet {
	
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType( "text/html; charset=iso-8859-1" );
		PrintWriter out = response.getWriter();
		List<CarpetasDTO> itemsTree =  Graficador.getArbolCJSP();
		// Obtengo los datos de la peticion
		String nombreCarpeta = request.getParameter("nombreCarpeta");
		HttpSession sesion = request.getSession(true);
                String user = sesion.getAttribute("sesionusuario").toString();
		
		CarpetasDTO carpetaDTO = new CarpetasDTO();
                carpetaDTO.setIdCarpeta(nombreCarpeta.hashCode());
                carpetaDTO.setNombreCarpeta(nombreCarpeta);
                carpetaDTO.setUser(user); 
                itemsTree.add(carpetaDTO);
                Graficador.setArbolCJSP(itemsTree);
                
                String carpetaJson = ParserJson.parseObjectToStr(carpetaDTO);
                
		if (!nombreCarpeta.equals("")) {
                   RequestBody formBody = new FormEncodingBuilder()
                           .add("carpetaJson", carpetaJson)
                           .build();
                   String res = Conexion.postString("insertarCarpeta", formBody);
                   System.out.print(res);
                   Graficador.dibujar("arbolB" + user + ".dot",  "arbolB" + user + ".png", 1);
                  Graficador.dibujar("arbolAVL" + user + ".dot", "arbolAVL" + user + ".png", 1);

		}
                
                out.println("<option class=\"btn btn-link\" value=\""+nombreCarpeta+"\"><i class=\"fa fa-folder\">&nbsp;"+nombreCarpeta+"</i></option>");
		
	}

}
