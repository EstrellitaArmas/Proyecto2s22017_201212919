<%-- 
    Document   : Login
    Created on : Sep 5, 2017, 11:18:49 PM
    Author     : estre
--%>

<%@page import="Helpers.CargaArchivos"%>
<%@page import="Inicio.Registro"%>
<%@page import="Inicio.Login"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
   <!-- Scripts-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="apple-touch-icon" href="apple-touch-icon.png">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <!--        <link rel="stylesheet" href="css/bootstrap-theme.min.css">-->
        <!--For Plugins external css-->
        <link rel="stylesheet" href="css/plugins.css" />
        <!--Theme custom css -->
        <link rel="stylesheet" href="css/style.css">
        <!--Theme Responsive css-->
        <!--<link rel="stylesheet" href="css/responsive.css" />-->
        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
        
        <script src="js/vendor/jquery-1.11.2.min.js"></script>
        <script src="js/vendor/bootstrap.min.js"></script>

        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
    </head>
    <body  data-spy="scroll" data-target="#main-navbar">
       <%
          session.setAttribute("sesionusuario", "");
          session.setAttribute("arbolArchivos", "");
          Registro.setError("");
          Login.setError("");
          CargaArchivos.cargaContenido("C://Users//estre//Desktop//Proyecto2s22017_201212919//habitaciones.xml","habitaciones");
       %>
        <div class='preloader'><div class='loaded'>&nbsp;</div></div>
        <div id="menubar" class="main-menu">	
            <nav class="navbar navbar-default navbar-fixed-top">
                <div class="container">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="navbar-header">
                        <h1><a href=""><B>USAC Driver</B></a></h1>                         
                    </div>                    
                </div><!-- /.container-fluid -->
            </nav>
        </div>
        <header id="home" class="sections">
            <div class="container">
            </div>
        </header>       
        <section id="our-history" class="sections">
           <div class="container">
              <div class="heading">
                 <div class="title text-center arrow-left">
                    <h4 class="">BIENVENIDO</h4>
                 </div>
              </div>
              <div class="row">
                 <div class="main-history">
                    <div class="col-md-6 col-sm-6 col-xs-12">
                       <p align="center">
                           <img src="images/team/3.png" />
                           <img src="images/team/4.png" />
                       </p>                       
                    </div>
                    <div class="col-md-6 col-sm-6 col-xs-12">
                       <div class="history-wrapper">
                          <div class="history-content">
                             <div class="title text-center arrow-right">
                                <h4 class=""><a href="Login.jsp"><b>INICIAR SESION</b></a></h4>                                
                             </div>
                             <div class="title text-center arrow-right">
                                <h4 class=""><a href="Registro.jsp"><b>REGISTRARSE</b></a></h4>                                
                             </div>
                          </div>
                       </div>
                    </div>
                 </div>
              </div>
           </div>
        </section>
    </body>
</html>
