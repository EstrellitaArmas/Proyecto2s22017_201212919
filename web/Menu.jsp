<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import = "Menu.Reservar"%>
<%@page import = "Menu.BorrarReserva"%>
<%@page import = "Menu.modificarPago"%>
<%@page import = "Menu.borrarPago"%>
<%@page import = "Menu.modificarInformacion"%>
<%@page import = "Menu.borrarInformacion"%>
<%@page import = "Menu.EliminarHabitacion"%>
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
        
        <!--For Plugins external css-->
        <link rel="stylesheet" href="css/plugins.css" />
        
        <!--Theme custom css -->
        <link rel="stylesheet" href="css/style.css"> <!-- Estilo de barra superior -->
        <!--Theme Responsive css-->
        <link rel="stylesheet" href="css/responsive.css" />
        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
        
        <script src="js/vendor/jquery-1.11.2.min.js"></script>
        <script src="js/vendor/bootstrap.min.js"></script>

        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
        
        <!-- text fonts -->
        <link rel="stylesheet" href="assets/css/ace-fonts.css" />
        <!-- ace styles -->
        <link rel="stylesheet" href="assets/css/ace.css" class="ace-main-stylesheet" id="main-ace-style" />
        <!-- ace settings handler -->
        <script src="assets/js/ace-extra.js"></script>

    </head>
   <body  data-spy="scroll" data-target="#main-navbar">
        <div id="menubar" class="main-menu">
             <nav class="navbar navbar-default navbar-fixed-top">
                <div class="container">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="navbar-header">
                        <h1><a href=""><B>HOTEL</B></a></h1>                         
                    </div>
                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                       <ul class="nav navbar-nav navbar-right">
                          <li class="active"><a href="#crear">INICIO<span class="sr-only">(current)</span></a></li>
                          <li>
                             <a data-toggle="dropdown" href="#" class="dropdown-toggle">
                                <span class="user-info">
                                   <%= session.getAttribute("sesionusuario") %>
                                </span>
                                <i class="ace-icon fa fa-caret-down"></i>
                             </a>
                             <ul class="user-menu dropdown-menu-right dropdown-menu dropdown-yellow dropdown-caret dropdown-close">                               
                                <li><a href="Inicio.jsp">Salir &nbsp; <i class="fa fa-arrow-right fa-1x"></i></a></li>
                             </ul>
                          </li>                           
                       </ul>                         
                    </div><!-- /.navbar-collapse -->                    
                </div><!-- /.container-fluid -->
             </nav>        
        </div>     
        <header id="home" class="sections">
           <div class="row">
              <div class="homepage-style">
                 <div class="container">
                    <div class="col-md-12 col-sm-12 col-xs-12">
                        <div class="widget-box widget-color-green2">
                           <div class="widget-header">
                              <h4 class="widget-title lighter smaller">Mis Reservas</h4>
                           </div>

                           <div class="widget-body">
                              <div class="widget-main padding-8">
                                 <ul class="collapsibleList">
                                    <li>
                                       <ul>
                                          <div id="carpetas">
                                             <%= session.getAttribute("arbolCarpetas") %>
                                          </div>
                                       </ul>
                                    </li>
                                 </ul>
                              </div>
                           </div>
                        </div>
                     </div>
                 </div>                                                                             
               </div>
            </div>
        </header>
        <section id="crear" class="sections">
         <div class="container">           
            <div class="row">
               <div class="heading">
                  <div class="title text-center arrow-right">
                     <h4 class="">INICIO</h4>
                     <img class="hidden-xs" src="assets/images/right-arrow.png" alt="" />

                  </div>
               </div>
               <div class="portfolio-wrap">
                  <div class="portfolio">
                     <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="widget-box">
                           <div class="widget-header">
                              <h4 class="widget-title">&nbsp;Hacer Reservacion</h4>
                           </div>
                           <div class="widget-body">
                              <div class="widget-main">                            
                                 <div class="form-group">
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="tarjeta" name="tarjeta" placeholder="Ingrese numero de tarjeta">
                                    </div>
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="habitacion" name="habitacion" placeholder="Ingrese numero de habitacion">
                                    </div>
                                    <div class="col-xs-12">
                                       <div class="input-group margin-bottom-sm">
                                          <span class="input-group-addon"><i class="fa fa-calendar fa-fw"></i>Fecha Ingreso</span>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="año" name="año"  placeholder="año"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="mes" name="mes"  placeholder="mes"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="dia" name="dia"  placeholder="dia"/>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-xs-12">
                                       <div class="input-group margin-bottom-sm">
                                          <span class="input-group-addon"><i class="fa fa-calendar fa-fw"></i>Fecha Salida</span>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="añoSalida" name="añoSalida"  placeholder="año"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="mesSalida" name="mesSalida"  placeholder="mes"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="diaSalida" name="diaSalida"  placeholder="dia"/>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-xs-12">
                                       <input class="ace" type="checkbox" id="netflix" name="extra" />
                                       <span class="lbl">Netflix</span>
                                       <input class="ace" type="checkbox" id="limpieza" name="extra" />
                                       <span class="lbl">Limpieza</span>
                                       <input class="ace" type="checkbox" id="cable" name="extra"/>
                                       <span class="lbl">Cable</span>
                                       <input class="ace" type="checkbox" id="internet" name="extra"/>
                                       <span class="lbl">Internet</span>
                                       <input class="ace" type="checkbox" id="hielo" name="extra"/>
                                       <span class="lbl">Hielo</span>
                                    </div>
                                    <label>
                                       <button id="reservar" name="reservar" value="reservar">
                                          <i class="ace-icon fa fa-arrow-right icon-on-right bigger-110">Reservar</i>
                                       </button>
                                    </label> 
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="widget-box">
                           <div class="widget-header">
                              <h4 class="widget-title">EliminarReserva</h4>
                           </div>
                           <div class="widget-body">
                              <div class="widget-main">                            
                                 <div class="form-group">
                                    <div class="col-xs-12">
                                       <div class="input-group margin-bottom-sm">
                                          <span class="input-group-addon"><i class="fa fa-calendar fa-fw"></i>Fecha Ingreso</span>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="añoEliminar" name="añoEliminar"  placeholder="año"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="mesEliminar" name="mesEliminar"  placeholder="mes"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="diaEliminar" name="diaEliminar"  placeholder="dia"/>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="habitacionEliminar" name="habitacionEliminar" placeholder="Ingrese numero de habitacion">
                                    </div>
                                    <label>
                                       <button id="eliminarReserva" name="eliminarReserva">Eliminar
                                          <i class="ace-icon fa fa-close bigger-110"></i>
                                       </button>
                                    </label>  
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>                      
                     <b><input  type="text" id="statusReserva" name="statusReserva" readonly=""></b>
                     <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="widget-box">
                           <div class="widget-header">
                              <h4 class="widget-title">Pago</h4>
                           </div>
                           <div class="widget-body">
                              <div class="widget-main">                            
                                 <div class="form-group">
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="tarjetaModificar" name="tarjetaModificar" placeholder="Ingrese numero de tarjeta">
                                    </div>
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="pagoModificar" name="pagoModificar" placeholder="Ingrese nuevo monto">
                                    </div>
                                    <label>
                                       <button id="modificarPago" name="modificarPago">Modificar Pago
                                          <i class="ace-icon fa fa-check-circle bigger-110"></i>
                                       </button>
                                    </label> 
                                    <label>
                                       <button id="eliminarPago" name="eliminarPago">Cancelar Pago
                                          <i class="ace-icon fa fa-close bigger-110"></i>
                                       </button>
                                    </label> 
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <b><input  type="text" id="statusPago" name="statusPago" readonly=""></b>
                     <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="widget-box">
                           <div class="widget-header">
                              <h4 class="widget-title">Modificar datos cliente de la reserva</h4>
                           </div>
                           <div class="widget-body">
                              <div class="widget-main">                            
                                 <div class="form-group">
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="nuevoNombre" name="nuevoNombre" placeholder="Ingrese nuevo nombre de cliente">
                                    </div>
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="nuevoTotal" name="nuevototal" placeholder="Ingrese nuevo monto">
                                    </div>
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="nuevoHabitacion" name="nuevoHabitacion" placeholder="Ingrese nueva habitacion">
                                    </div>
                                    <div class="col-xs-12">
                                       <div class="input-group margin-bottom-sm">
                                          <span class="input-group-addon"><i class="fa fa-calendar fa-fw"></i>Fecha Ingreso</span>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="añoNuevo" name="añoNuevo"  placeholder="año"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="mesNuevo" name="mesNuevo"  placeholder="mes"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="diaNuevo" name="diaNuevo"  placeholder="dia"/>
                                          </div>
                                       </div>
                                    </div>
                                    <div class="col-xs-12">
                                       <div class="input-group margin-bottom-sm">
                                          <span class="input-group-addon"><i class="fa fa-calendar fa-fw"></i>Fecha Salida</span>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="añoSalidaNuevo" name="añoSalidaNuevo"  placeholder="año"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="mesSalidaNuevo" name="mesSalidaNuevo"  placeholder="mes"/>
                                          </div>
                                          <div class="col-xs-12">
                                             <input class="form-control" type="text" id="diaSalidaNuevo" name="diaSalidaNuevo"  placeholder="dia"/>
                                          </div>
                                       </div>
                                    </div>
                                    <label>
                                       <button id="modificarInformacion" name="modificarInformacion">Modificar Informacion
                                          <i class="ace-icon fa fa-check-circle bigger-110"></i>
                                       </button>
                                    </label> 
                                    <label>
                                       <button id="eliminarInformacion" name="eliminarInformacion">Eliminar Informacion
                                          <i class="ace-icon fa fa-close bigger-110"></i>
                                       </button>
                                    </label> 
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="widget-box">
                           <div class="widget-header">
                              <h4 class="widget-title">Eliminar Habitacion</h4>
                           </div>
                           <div class="widget-body">
                              <div class="widget-main">                            
                                 <div class="form-group">
                                    <div class="col-xs-12">
                                       <input class="form-control" type="text" id="habitacionEliminar2" name="habitacionEliminar2" placeholder="Ingrese numero de habitacion">
                                    </div>
                                    <label>
                                       <button id="eliminarHabitacion" name="eliminarHabitacion">Eliminar
                                          <i class="ace-icon fa fa-close bigger-110"></i>
                                       </button>
                                    </label>  
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div> 
                     <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="widget-box">
                           <div class="widget-header">
                              <h4 class="widget-title">USUARIOS</h4>
                           </div>
                           <div class="widget-body">
                              <div class="widget-main">                            
                                 <div class="form-group">
                                    <div class="input-group margin-bottom-sm">
                                       <span class="input-group-addon"><i class="fa fa-envelope-o fa-fw"></i></span>
                                       <input class="form-control" type="text" id="user" name="user" placeholder="Email address">
                                    </div>
                                    <div class="input-group">
                                       <span class="input-group-addon"><i class="fa fa-key fa-fw"></i></span>
                                       <input class="form-control" type="password" id="pass" name="pass" placeholder="Password">
                                    </div>
                                    <div class="input-group margin-bottom-sm">
                                       <span class="input-group-addon"><i class="fa fa-home fa-fw"></i></span>
                                       <input class="form-control" type="text" id="address" name="address" placeholder="Address">
                                    </div>                                
                                    <div class="input-group margin-bottom-sm">
                                       <span class="input-group-addon"><i class="fa fa-phone fa-fw"></i></span>
                                       <input class="form-control" type="text" id="phone" name="phone" placeholder="Phone">
                                    </div>
                                    <div class="input-group margin-bottom-sm">
                                       <span class="input-group-addon"><i class="fa fa-gift fa-fw"></i></span>
                                       <input class="form-control" type="text" id="spinner" name="age"  placeholder="Age" />
                                    </div><br>
                                    <label>
                                       <button id="modificarUsuario" name="modificarUsuario">Modificar Informacion de usuario
                                          <i class="ace-icon fa fa-check-circle bigger-110"></i>
                                       </button>
                                    </label> 
                                    <label>
                                       <button id="eliminarUsuario" name="eliminarUsuario">Eliminar usuario
                                          <i class="ace-icon fa fa-close bigger-110"></i>
                                       </button>
                                    </label>  
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div> 
                  </div>                  
               </div>               
            </div>
         </div>
        </section>
      <div class="scroll-top">

         <div class="scrollup">
            <i class="fa fa-angle-double-up"></i>
         </div>

      </div>  
    </body>
</html>


<script src="assets/js/jquery.autosize.js"></script>
<script src="assets/js/bootstrap-tag.js"></script>

<!-- ace scripts -->
<script src="assets/js/ace/elements.fileinput.js"></script>
<script src="assets/js/ace/ace.js"></script>
<script src="assets/js/ace/ace.widget-box.js"></script>
<script src="assets/js/fuelux/fuelux.tree.js"></script>
<script src="assets/js/ace/elements.treeview.js"></script>
<script type="text/javascript">
   jQuery(function($){
      //spinner
     
      $("#comboCarpeta").change(function (){
         var nomCarpeta = $("#comboCarpeta").val();
         $("#nomCarpeta").attr("value",nomCarpeta);
      });
      $("#comboFile").change(function (){
         var nomCarpeta = $("#comboFile").val();
         $("#statusFile").attr("value",nomCarpeta);
      });
      $("button.carpeta").click(function() {
            var nombreVar = $(this).val();
            $.post('ActionServlet', {
                  nombre : nombreVar,
            }, function(responseText) {
                  $('#tabla').html(responseText);
            });
      });
        //reservar///////////////////////////
      $("#reservar").click(function() {
          var tarjeta = $('#tarjeta').val();
          var habitacion = $('#habitacion').val();
          var año = $('#año').val();
          var mes = $('#mes').val();
          var dia = $('#dia').val();
          var fechaIngreso = año + mes + dia;
          año = $('#añoSalida').val();
          mes = $('#mesSalida').val();
          dia = $('#diaSalida').val();
          var fechaSalida = año + mes + dia;
          var extras = 0
          $("input[type=checkbox]").each(function(){
               if($(this).is(":checked"))
                       extras++;
          });
          
          $.post('reservar', {
                tarjeta : tarjeta,
                habitacion : habitacion,
                fechaIngreso : fechaIngreso,
                fechaSalida : fechaSalida, 
                extras : extras,
          }, function(responseText) {
             console.log(responseText);
                $("#statusReserva").attr("value",responseText);
          });
      });
      ////////////////////////////////////////////////////
      $("#eliminarReserva").click(function() {
          var año = $('#añoEliminar').val();
          var mes = $('#mesEliminar').val();
          var dia = $('#diaEliminar').val();
          var fechaIngreso = año + mes + dia;
          var habitacion = $('#habitacionEliminar').val();
          $.post('borrarReserva', {
                fechaIngreso : fechaIngreso,
                habitacion : habitacion,
          }, function(responseText) {
               $("#statusReserva").attr("value",responseText);
          });
      });
      $("#modificarPago").click(function() {
          var tarjeta = $('#tarjetaModificar').val();
          var pago = $('#pagoModificar').val();
          console.log(pago);
          $.post('modificarPago', {
                tarjeta : tarjeta,
                pago : pago,
          }, function(responseText){
               $("#statusPago").attr("value",responseText);
          });
      });
      $("#eliminarPago").click(function() {
          var tarjeta = $('#tarjetaModificar').val();
          $.post('borrarPago', {
                tarjeta : tarjeta,
          }, function(responseText){
               $("#statusPago").attr("value",responseText);
          });
      });
      $("#modificarInformacion").click(function() {
          var nuevoNombre  = $('#nuevoNombre').val();
          var habitacion = $('#nuevoHabitacion').val();
          var año = $('#añoNuevo').val();
          var mes = $('#mesNuevo').val();
          var dia = $('#diaNuevo').val();
          var fechaIngreso = dia + mes + año;
          año = $('#añoSalidaNuevo').val();
          mes = $('#mesSalidaNuevo').val();
          dia = $('#diaSalidaNuevo').val();
          var fechaSalida = año + mes + dia;
          var total = $('#nuevoTotal').val();
          console.log(nuevoNombre+"--"+habitacion+"--"+fechaIngreso+"--"+fechaSalida+"--"+total)
          $.post('modificarInformacion', {
                nuevoNombre : nuevoNombre,
                habitacion : habitacion,
                idFechaIngreso : fechaIngreso,
                fechaSalida : fechaSalida, 
                total : total,
          }, function(responseText) {
             console.log(responseText);
                $("#statusReserva").attr("value",responseText);
          });
      });
      $("#eliminarInformacion").click(function() {
          var año = $('#añoNuevo').val();
          var mes = $('#mesNuevo').val();
          var dia = $('#diaNuevo').val();
          var fechaIngreso = dia + mes + año;
          $.post('borrarInformacion', {
                idFechaIngreso : fechaIngreso,
          }, function(responseText) {
             console.log(responseText);
                $("#statusReserva").attr("value",responseText);
          });
      });
      
      $("#eliminarHabitacion").click(function() {
          var habitacion = $('#habitacionEliminar2').val();
          console.log(habitacion)
          $.post('eliminarHabitacion', {
                habitacion : habitacion,
          }, function(responseText){
               $("#statusPago").attr("value",responseText);
          });
      });
      
      $("#modificarUsuario").click(function() {
          var user = $('#user').val();
          var pass = $('#pass').val();
          var address = $('#address').val();
          var phone = $('#phone').val();
          var age = $('#spinner').val();
          $.post('modificarUsuario', {
                user : user,
                pass : pass,
                address : address,
                phone : phone,
                age : age
                
                
          }, function(responseText){
               $("#statusPago").attr("value",responseText);
          });
      });
   });        
 
</script>