### info:
#    ENRUTAMIENTO DE LA PETICIÓN  
#    Recibe las peticiones http (get, post) de un cliente.
#    Invoca a la función ("enruta") que resuelve la petición. 
#   La función que resuelve la petición se encuentra en el 'controller'
#    Envía una respuesta al cliente que realizó la petición. La respuesta
#    a será un str que en la mayoría de los casos contiene html
#   
#    Dependencias:
#      pip install Flask
#      pip install Werkzeug
#
#    Referencias:
#      https://pypi.org/project/Flask/
#      https://flask.palletsprojects.com/en/2.3.x/
#      https://pythonbasics.org/flask-http-methods/
#      https://pypi.org/project/Werkzeug/
   

import os
from flask import Flask, render_template, request, redirect, session, flash, url_for  
from controller import *
from werkzeug.utils import secure_filename

def route(app):    #indica hacia donde ir dependiendo de la info que llegue
    @app.route("/", methods =["GET", "POST"])
    @app.route("/inicio", methods =["GET", "POST"])
    def home():
        # Info:
        #  Carga la pagina del inicio
        param={} 
        if not haySesion():
            return login_pagina(param)      # o login_pagina(param)
        if request.method=='POST': #si es un post hace esto
            return guardarPedido(param,request) 
        return inicio_pagina(param)
       
        
    
    @app.route("/login")
    def login():
        # Info:
        #   Carga la pagina del login  

        param={}
        return login_pagina(param)      
        
    
    @app.route("/registrarse")
    def register():
       
        return render_template("registro.html", show_sidebar=False) 

    
    @app.route("/signup", methods =["GET", "POST"])
    def signup():
        # Info:
        #  Recepciona la solicitud request que es enviada
        #  desde el formulario de registro 
        #  registroDeUsuario: Luego de realizar el proceso de 
        #     registro del usuario, retorna la pagina del login 
        
        param={}
        return registrarUsuario(param,request)


    @app.route('/signin', methods =["GET", "POST"])
    def signin(): 
        #Info: 
        # Recepciona la solicitud request que es enviada
        #  desde el formulario de login 
        #  retorna la pagina home en caso de exito 
        #          o la pagina login en caso de fracaso
        
        param={}
        return ingresoUsuarioValido(param,request)

 
    @app.route("/logout")
    def logout():  
        ''' Info: 
          Cierra la sesión.
          retorna la redirección a la pagina home   
        ''' 
        cerrarSesion()     
        return redirect('/login')
    

    @app.route("/MiPerfil")
    def pag04():
        param={}
        return Miperfil(param)
    
    @app.route("/ModificarPerfil")
    def pag07():
        param={}
        return ModificarPerfil(param)


    @app.route("/MisPedidos")
    def pag05():
        param={}
        return MisPedidos(param)   
    
    
    @app.route("/PedidoPersonalizado")
    def pag06():
        param={}
        return PedidoPersonalizado(param) 
    
    @app.route("/Pedidos")
    def pag08():
        param={}
        return Pedidos(param) 
    
    @app.route("/DetallesPedidos1")
    def pag09():
        param={}
        return DetallesPedidos1(param) 
    
    @app.route("/DetallesPedidos2")
    def pag10():
        param={}
        return DetallesPedidos2(param) 
    
    @app.route("/DetallesPedidos3")
    def pag11():
        param={}
        return DetallesPedidos3(param) 
    
    @app.route("/ModificarMenu")
    def pag12():
        param={}
        return ModificarMenu(param) 


    @app.route("/edit_user")
    def edit_user():
        ''' Info:
          Carga la edit_user
          Retorna la edit_user, si hay sesion; sino retorna la home.
        '''
        param={}
        return render_template("modificar_perfil.html")   
 

    @app.route("/update_user", methods =["GET", "POST"])
    def update_user():
        ''' Info:
          Recepciona la solicitud request que es enviada
              desde el formulario de edit_user 
          Retorna 
            si hay sesion: retorna la edit_user con los datos actualizados
               y un mensaje de exito o fracaso sobre el mismo form ; 
            si no hay sesion: retorna la home.
        '''
        param={}
        return actualizarDatosDeUsuarios(param,request)
    

    @app.route("/about")
    def about():
        ''' Info:
          Carga la pagina about
        '''
        param={}
        return acercaDe_pagina(param)      


    @app.route('/<name>')
    def noEncontrada(name):
        ''' Info:
          Entra en esta ruta todo direccionamiento recibido que 
          no machea con ningun otro route. Es decir no es un pagina (dirección)
            válida en el sistema.
          Retorna una pagina indicando el error. 
        '''  
        
        return paginaNoEncontrada(name)
    
 

   