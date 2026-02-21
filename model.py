
from _mysql_db import *

def crearUsuario(di):
    '''### Información:
        Agrega un nuevo usuario (un registro) en la tabla usuario de la DB
        Recibe 'di' un diccionario con los datos del usuario a agegar en la tabla.
        Retorna True si realiza con existo el insert, False caso contrario.
    '''
    sQuery=""" 
        INSERT INTO usuario
        (id,nombre,apellido,dni,clave,tipo_usuario,observacion)
        VALUES
        (NULL, %s, %s, %s, %s, %s, %s);
    """
    val=(di.get('nombre'), di.get('apellido'), di.get('dni'), di.get('clave'), di.get('roles'), di.get('observaciones'))
    resul_insert=insertDB(BASE,sQuery,val)
    return resul_insert==1

def obtenerUsuarioXDNI(param,dni,clave='usuario'):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'email'.
       Carga la información obtenida de la BD en el dict 'param'
       Recibe 'param' in diccionario
       Recibe 'dni' que es el dni si se utiliza como clave en la búsqueda
       Recibe 'clave' que es a clave que se le colocará al dict 'param'
       
    '''
    
    res=False
    
    sSql="""SELECT id,nombre,apellido,dni,clave,tipo_usuario,observacion 
    FROM usuario WHERE  dni=%s;""" 
    val=(dni,)

    fila=selectDB(BASE,sSql,val)
    
    if fila!=[]:
        res=True
        
        param[clave]={}
        param[clave]['id']=fila[0][0]
        param[clave]['nombre']=fila[0][1]
        param[clave]['apellido']=fila[0][2]
        param[clave]['dni']=fila[0][3]
        param[clave]['clave']=fila[0][4]
        param[clave]['tipo_usuario']=fila[0][5]
        param[clave]['observacion']=fila[0][6]
        
    return res

def obtenerUsuarioXClave(result,dni,clave):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'dni'
         y del 'password'.
       Carga la información obtenida de la BD en el dict 'result'
       Recibe 'result' in diccionario donde se almacena la respuesta de la consulta
       Recibe 'dni' que es el dni si se utiliza como clave en la búsqueda
       Recibe 'clave' que se utiliza en la consulta. (Para validadar al usuario)
       Retorna:
        True cuando se obtiene un registro de u usuario a partir del 'dni' y la 'clave'.
        False caso contrario.
    '''
    res=False
    sSql="""SELECT id,nombre,apellido,dni,clave,tipo_usuario,observacion 
    FROM  usuario WHERE  dni=%s and clave=%s;"""
    val=(dni,clave)
    fila=selectDB(BASE,sSql,val)
    if fila!=[]:
        res=True
        result['id']=fila[0][0]
        result['nombre']=fila[0][1]
        result['apellido']=fila[0][2]
        result['dni']=fila[0][3] 
        result['clave']=fila[0][4]
        result['tipo_usuario']=fila[0][5]
        result['observacion']=fila[0][6]
    return res           

def actualizarUsuario(di,dni):
    '''### Información:
        Actualiza el registro de la tabla usuario para la clave 'dni'
        Recibe 'di' un dict con los campos que se requiere modificar.
        Recibe 'dni' que es la clave para identificar el regsitro a actualizar.
        Retorna True si realiza la actualización correctamente.
                False caso contrario.

    '''
    sQuery="""update usuario 
        SET nombre=%s, apellido=%s, clave=%s, tipo_usuario=%s, observacion=%s, 
        WHERE dni=%s;
        """
        
    val=(di.get('nombre'), di.get('apellido'), dni, di.get('clave'), di.get('tipo_usuario'), di.get('observacion'))
    
    resul_update=updateDB(BASE,sQuery,val=val)
    return resul_update==1   
    
def obtener_observacion_usuario(usuario_id):
    sQUery = """SELECT observacion FROM usuario WHERE id=%s LIMIT 1;"""
    fila = selectDB(BASE, sQUery, (usuario_id,))
    return fila[0][0] if fila else None

def obtener_restricciones_usuario(usuario_id):
    sql = """SELECT restriccion FROM restriccion_usuario WHERE usuario_id=%s;"""
    res = selectDB(BASE, sql, (usuario_id,))
    restricciones = []
    for fila in res:
        restricciones.append(fila[0])
    return restricciones

def obtenerMenuDelDia(fecha): #SELECT tablaA.columnaAObtener FROM tabla principal INNER JOIN tabla ON tablaA_id = (conexion de foreign keys) tablaprincipal.tablaA_id
    sql = """SELECT plato_principal.nombre_plato , guarnicion.nombre_guarnicion, bebida.nombre_bebida, postre.nombre_postre FROM menu 
    INNER JOIN plato_principal ON plato_principal_id = menu.plato_principal_id 
    INNER JOIN guarnicion ON guarnicion_id = menu.guarnicion_id 
    INNER JOIN bebida ON bebida_id = menu.bebida_id 
    INNER JOIN postre ON postre_id = menu.postre_id
    WHERE tipo='del dia' AND fecha=%s;"""
    #devuelve los nombres de cada id que tengo en menu para cada parte del plato pedido
    fila = selectDB(BASE, sql, fecha)
    return fila[0] if fila else None 

#DELETE,INSERT,SELECT,UPDATE
#delete y update no necesita return

#POST 
#INTERCAMBIO PYTHON A SQL, fuera de model.py es TOD PYTHON
def realizarPedido(di):
    sql="""INSERT INTO pedidos (usuario_id,menu_id,fecha,horario,obervacion) 
    VALUES (%s,%s,%s,%s,%s)"""
    val= (di.get('usuario_id'),di.get('menu.id'),di.get('fecha'),di.get('horario'),di.get('observacion'))
    
    result_insert = insertDB(BASE,sql,val=val)
    return result_insert==1 #si devuelve 1 fue exitoso el insert

def obtenerIDMenu(fecha,tipo):
    sql = """SELECT id FROM menu WHERE fecha='%s AND tipo='%s'"""
    val = (fecha,tipo)
    id = selectDB(BASE,sql,val)
    return id[0][0] if id else None
    
