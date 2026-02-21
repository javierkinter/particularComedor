# Active: 1765485388518@@127.0.0.1@3306@base
# info:
#     CONTROL 
#   Dependencias:
#      pip install uuid
#
#    Referencias:
#        https://pypi.org/project/uuid/
#       https://docs.python.org/3/library/uuid.html
    

from flask import request, session,redirect,render_template
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from appConfig import config

##########################################################################
# + + I N I C I O + + MANEJO DE  REQUEST + + + + + + + + + + + + + + + + +
##########################################################################
#tiene la logica de como funciona la pagina
def getRequest(diResult):
    if request.method=='POST':
        for name in request.form.to_dict().keys():
            li=request.form.getlist(name)
            if len(li)>1:
                diResult[name]=request.form.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""
    elif request.method=='GET':  
        for name in request.args.to_dict().keys():
            li=request.args.getlist(name)
            if len(li)>1:
                diResult[name]=request.args.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""     


##########################################################################
# - - F I N - - MANEJO DE  REQUEST - - - - - - - - - - - - - - - - - - - -
##########################################################################


##########################################################################
# + + I N I C I O + + MANEJO DE  SESSION + + + + + + + + + + + + + + + + +
##########################################################################

def cargarSesion(dicUsuario):
    '''info:
        Realiza la carga de datos del usuario
        en la variable global dict 'session'.
        recibe 'dicUsuario' que es un diccionario con datos
               de un usuario.
        Comentario: Usted puede agregar en 'session' las claves que necesite
    '''

    session['id']         = dicUsuario['id']
    session['nombre']     = dicUsuario['nombre']
    session['apellido']   = dicUsuario['apellido']
    session['dni']        = dicUsuario['dni'] 
    session['clave']      = dicUsuario['clave']
    session['tipo_usuario'] = dicUsuario['tipo_usuario']
    session["time"]       = datetime.now().strftime('%Y-%m-%d') #lo convierte en string y le indica el formato que tiene de solo fecha (saca el horario en este caso)

def crearSesion(request):
    '''info:
        Crea una sesion. Consulta si los datos recibidos son validos.
        Si son validos carga una sesion con los datos del usuario
        recibe 'request' una solicitud htpp con los datos 'dni' y 'clave' de 
        un usuario.
        retorna True si se logra un session, False caso contrario
    '''
    sesionValida=False
    mirequest={}
    try: 
        #Carga los datos recibidos del form cliente en el dict 'mirequest'.          
        getRequest(mirequest)
        print("DEBUG login:", mirequest)
        # CONSULTA A LA BASE DE DATOS. Si usuario es valido => crea session
        dicUsuario={}
        if obtenerUsuarioXClave(dicUsuario,mirequest.get("dni"),mirequest.get("clave")):
            # Carga sesion (Usuario validado)
            cargarSesion(dicUsuario)
            sesionValida = True
    except ValueError as e:                              
        pass
    return sesionValida

def haySesion():  
    '''info:
        Determina si hay una sesion activa observando si en el dict
        session se encuentra la clave 'dni'
        retorna True si hay sesión y False si no la hay.
    '''
    return session.get("dni")!=None

def cerrarSesion():
    '''info:
        Borra el contenido del dict 'session'
    '''
    try:    
        session.clear()
    except:
        pass

##########################################################################
# - - F I N - - MANEJO DE  SESSION - - - - - - - - - - - - - - - - - - - -
##########################################################################


##########################################################################
# + + I N I C I O + + PAGINA login, home y/o principal    + + + + + + + + 
##########################################################################

def inicio_pagina(param): 
    ''' Info:
      Carga la pagina home.
      Recibe 'param' el diccionario de parametros
      Retorna la pagina 'inicio' renderizada.
    '''
    fecha=session.get('time')
    param['menuDia']=obtenerMenuDelDia((fecha,)) #tupla con un unico valor para que corra y no tire error
    return render_template('inicio.html',param=param,show_sidebar=True) #aca le indico cual es el archivo que tengo que reenderizar 
#le paso los param que necesito para que ESA pagina funcione

def login_pagina(param):
    ''' Info:
      Carga la pagina login.
      Recibe 'param' el diccionario de parametros
      Retorna la pagina 'login' renderizada.
    '''
    return render_template('login.html',param=param,show_sidebar=False)

##########################################################################
# - - F I N - - PAGINA login, home y/o principal   - - - - - - - - - - - -
##########################################################################


##########################################################################
# + + I N I C I O + + USUARIO: registro, edicion, actualizacion  + + + + + 
##########################################################################

def ingresoUsuarioValido(param,request):
    '''info:
        Valida el usuario y el pass contra la BD.
        recibe 'param' dict de parámetros
        recibe 'request' una solicitud http con los datos usuario y pass
        retorna: 
            Si es valido el usuario y pass => crea una session y retorna 
            la pagina home.
            Si NO es valido el usuario y pass => retorna la pagina login
            y agrega en el diccionario de parámetros una clave con un mensaje 
            de error para ser mostrada en la pagina login.
    '''
    if crearSesion(request):
        res=render_template('inicio.html',param=param,show_sidebar=True)
    else:
        param['error_msg_login']="Error: Usuario y/o password inválidos"
        res= login_pagina(param)        
    return res  

def registro_pagina(param):
    '''info:
        Carga la pagina 'register'
    '''     
    return render_template('registro.html',param=param,show_sidebar=False  )

def ValidarFormularioRegistro(di):
    res=True
    res= res and di.get('nombre')!=""
    res= res and di.get('apellido')!=""
    res= res and di.get('dni')!=""
    res= res and di.get('clave')!=""
    res= res and di.get('clave2')!=""
    return res

def registrarUsuario(param,request):
    '''info:
      Realiza el registro de un usuario en el sistema, es decir crea un nuevo usuario
      y lo registra en la base de datos.
      recibe 'param' el diccionario de parámetros.
      recibe request es la solicitud (post o get) proveniente del cliente
      retorna la pagina del login, para forzar a que el usuario realice el login con
      el usuario creado.
    '''
    mirequest={}
    getRequest(mirequest)
    print(mirequest)
    
    if ValidarFormularioRegistro(mirequest):
        # CONSULTA A LA BASE DE DATOS: Realiza el insert en la tabla usuario
        if crearUsuario(mirequest):
            
            #Obtengo el usuario_id para ingreasar las restricciones si las hay
            
            dni = mirequest.get("dni")
            fila = selectDB(BASE, "SELECT id FROM usuario WHERE dni=%s LIMIT 1;", (dni,))
            usuario_id = fila[0][0] if fila else None

            restricciones = request.form.getlist("restricciones") 
            validas = {"celiaco","vegano","vegetariano"}
            for r in restricciones:
                if r in validas:
                    insertDB(BASE,
                             "INSERT INTO restriccion_usuario (usuario_id, restriccion) VALUES (%s,%s);",
                             (usuario_id, r))
            
            param['succes_msg_login']="Se ha creado el usuario con exito"
            cerrarSesion()           # Cierra sesion existente(si la hubiere)
            res=login_pagina(param)  # Envia al login para que vuelva a loguearse el usuario
        else:
            param['error_msg_register']="Error: No se ha podido crear el usuario"
            res=registro_pagina(param)
    else:
        param['error_msg_register']="Error: Problema en la validacion de los campos"
        res=registro_pagina(param)

    # obtenerSidebar(param)
    return res 

def editarUsuario_pagina(param):
    '''info:
        Carga la pagina edit_user
        Retorna la pagina edit_user, si hay sesion; sino retorna la home.
    '''
    res= redirect('/') # redirigir al home o a la pagina del login

    if haySesion():    # hay session?
        # Confecciona la pagina en cuestion
        obtenerUsuarioXDNI(param,session.get('dni'), 'edit_user')
        res= render_template('modificar_perfil.html',param=param,show_sidebar=True)
           
    return res  


def actualizarDatosDeUsuarios(param,request):
    '''info:
            Recepciona la solicitud request que es enviada
            desde el formulario de edit_user 
          Retorna 
            si hay sesion: retorna la edit_user con los datos actualizados
               y un mensaje de exito o fracaso sobre el mismo form ; 
            si no hay sesion: retorna la home.
    '''
    res=False
    msj=""
    mirequest={}
    try:     
        getRequest(mirequest)      
        # *** ACTUALIZAR USUARIO ***
        
        if actualizarUsuario(mirequest,session.get("dni")):
            res=True
            param['succes_msg_updateuser']="Se ha ACTUALIZADO el usuario con exito"
        else:
            #error
            res=False
            param['error_msg_updateuser']="Error: No se ha podido ACTUALIZAR el usuario"

        editarUsuario_pagina(param)
        res= render_template('modificar_perfil.html',param=param)  
    except ValueError as e :                   
        pass
    return res 

##########################################################################
# - - F I N - - USUARIO: registro, edicion, actualizacion  - - - - - - - -
##########################################################################
 

##########################################################################
# + + I N I C I O + +  OTRAS PAGINAS     + + + + + + + + + + + + + + + + +
##########################################################################

def Miperfil(param):  
    if haySesion():       # hay session?            
        # Confecciona la pagina en cuestion 
        param['page-header']="Mi Perfil, Acceso con logeo"
        
        usuario_id = session.get("id_usuario")

        param["obs_usuario"] = obtener_observacion_usuario(usuario_id)
        param["restricciones"] = obtener_restricciones_usuario(usuario_id)
        
        res= render_template('perfil.html',param=param,show_sidebar=True )
    else:
        res= redirect('/')   # redirigir al home o a la pagina del login
    return res  

def ModificarPerfil(param):  
    if haySesion():       # hay session?            
        # Confecciona la pagina en cuestion 
        param['page-header']="Modificar Perfil, Acceso con logeo"
        res= render_template('modificar_perfil.html',param=param,show_sidebar=True )
    else:
        res= redirect('/')   # redirigir al home o a la pagina del login
    return res  
    

def MisPedidos(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Mis Pedidos, Acceso con logeo"
        res= render_template('historial_pedidos.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 

def PedidoPersonalizado(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Pedido Persnalizado, Acceso con logeo"
        res= render_template('pedido_personalizado.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 


def Pedidos(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Pedidos, Acceso con logeo (admin)"
        res= render_template('admin_pedidos.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 

def DetallesPedidos1(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Detalles Pedidos, Acceso con logeo (admin)"
        res= render_template('admin_detalles1.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 

def DetallesPedidos2(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Detalles Pedidos, Acceso con logeo (admin)"
        res= render_template('admin_detalles2.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 

def DetallesPedidos3(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Detalles Pedidos, Acceso con logeo (admin)"
        res= render_template('admin_detalles3.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 

def ModificarMenu(param):  
    if haySesion():   # hay session?
        # Confecciona la pagina en cuestion 
        param['page-header']="Modificar Menú, Acceso con logeo (admin)"
        res= render_template('admin_modificar_menu.html',param=param,show_sidebar=True)
    else:
        res= redirect('/') # redirigir al home o a la pagina del login
    return res 


def acercaDe_pagina(param): 
    ''' Info:
        Carga la pagina about
    ''' 
    param['page-header']="ABOUT, Acceso SIN LOGEO"
    return render_template('inicio.html',param=param,show_sidebar=True) 
  

def paginaNoEncontrada(name):
    ''' Info:
      Retorna una pagina generica indicando que la ruta 'name' no existe
    '''
    res='Pagina "{}" no encontrada<br>'.format(name)
    res+='<a href="{}">{}</a>'.format("/","Inicio")
    
    return res

####
def guardarPedido(param,request):
   formulario = {}
   getRequest(formulario) #ahora formulario tiene todo lo que hay en el formulario request
   #getRequest guarda la info del request en lo que va dentro del parentesis
   
   #modificar html para formulario inicio (nombres)

   idMenu= obtenerIDMenu(session.get('time'),'del dia') #para personalizado le cambio el tipo
   
   pedido = {"usuario_id":session.get('id'),"menu_id":idMenu,"fecha":session.get('time'),"horario": formulario.get("horario"),"observacion":formulario.get("observacion")} 
   
   realizarPedido(pedido)
   
   return inicio_pagina(param) #el controller puede interactuar consigo mismo






##########################################################################
# - - F I N - -   OTRAS PAGINAS    - - - - - - - - - - - - - - - - - - - -
##########################################################################