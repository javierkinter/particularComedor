function validateForm(){
    let platoP=document.getElementById("PlatoP").value;
    let guarnición=document.getElementById("Guarnición").value;
    let bebida=document.getElementById("Bebida").value;
    let postre=document.getElementById("Postre").value;
    let horario=document.getElementById("horario1").value;
    let errorPlatoPrincipal=document.getElementById("errorPlatoPrincipal");
    let errorGuarnición=document.getElementById("errorGuarnición");
    let errorBebida=document.getElementById("errorBebida");
    let errorPostre=document.getElementById("errorPostre");
    let errorHorario=document.getElementById("errorHorario");
    let valid=true;

    errorPlatoPrincipal.textContent="";
    errorGuarnición.textContent="";
    errorBebida.textContent="";
    errorPostre.textContent="";
    errorHorario.textContent="";
        
    if(platoP==="") {
        errorPlatoPrincipal.textContent="Por favor, ingrese su eleccion de plato principal";
        valid=false;
    }
    if(guarnición==="") {
        errorGuarnición.textContent="Por favor, ingrese su eleccion de guarnición";
        valid=false;
    }
    if(bebida==="") {
        errorBebida.textContent="Por favor, ingrese su eleccion de bebida";
        valid=false;
    }
    if(postre==="") {
        errorPostre.textContent="Por favor, ingrese su eleccion de postre";
        valid=false;
    }
    if(horario==="") {
        errorHorario.textContent="Por favor, ingrese su horario";
        valid=false;
    }

    return valid;
}

function pedidoEnviado(event){

    event.preventDefault();

    var valid = validateForm();
    var Pedido=document.getElementById("Pedido");

    Pedido.textContent="";

    if(valid){
        Pedido.textContent="Su pedido ha sido enviado con exito!";
        return true;
    } 
    return false;
}

 function limpiarErrores() {
        var errores = ["errorPlatoPrincipal","errorGuarnición","errorBebida","errorPostre","errorHorario"];
        var Pedido=document.getElementById("Pedido");
        for (var i = 0; i < errores.length; i++) {
            var error = document.getElementById(errores[i]);
            if (error) {
                error.textContent = ""; 
              
            }
        }
        Pedido.textContent="";
    }

/* Esta funcion entrega el form pero no muestra el mensaje
function pedidoEnviado(){
    var valid = validateForm();
    var Pedido=document.getElementById("Pedido");

    Pedido.textContent="";

    if(valid){
        Pedido.textContent="Su pedido ha sido enviado con exito!";
    } 
    return valid;
    }

*/