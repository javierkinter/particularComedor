function validateForm(){
    let fecha=document.getElementById("fecha").value;
    let platoP=document.getElementById("PlatoP").value;
    let guarnición=document.getElementById("Guarnición").value;
    let bebida=document.getElementById("Bebida").value;
    let postre=document.getElementById("Postre").value;
    let errorFecha=document.getElementById("errorFecha");
    let errorPlatoPrincipal=document.getElementById("errorPlatoPrincipal");
    let errorGuarnición=document.getElementById("errorGuarnición");
    let errorBebida=document.getElementById("errorBebida");
    let errorPostre=document.getElementById("errorPostre");

    let valid=true;

    errorPlatoPrincipal.textContent="";
    errorGuarnición.textContent="";
    errorBebida.textContent="";
    errorPostre.textContent="";
    errorFecha.textContent="";
        
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
    if(fecha==="") {
        errorFecha.textContent="Por favor, ingrese una fecha";
        valid=false;
    } else {
        var reg = /^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$/;
        if (!reg.test(fecha)) {
            errorFecha.textContent="Por favor, ingrese una fecha valida";
            valid=false;
        } else {
            var partes = fecha.split("-");
            var año = parseInt(partes[0], 10);
            var mes = parseInt(partes[1], 10) - 1; // los meses van de 0 a 11
            var dia = parseInt(partes[2], 10);

            // Creamos la fecha con los valores ingresados
            var fechaIngresada = new Date(año, mes, dia);
            var hoy = new Date();
            hoy.setHours(0, 0, 0, 0); // comparar solo la fecha sin horas

            if (fechaIngresada < hoy) {
                errorFecha.textContent="La fecha no puede estar en el pasado";
                valid = false;
            }
        }
    }
    return valid;
}


function menuCambiado(event){

    event.preventDefault();

    var valid = validateForm();
    var Cambios=document.getElementById("Cambios");

    Cambios.textContent="";

    if(valid){
        Cambios.textContent="Su pedido ha sido enviado con exito!";
        return true;
    } 
    return false;
    }
   


 function limpiarErrores() {
        var errores = ["errorPlatoPrincipal","errorGuarnición","errorBebida","errorPostre","errorFecha"];
        var Cambios=document.getElementById("Cambios");
        for (var i = 0; i < errores.length; i++) {
            var error = document.getElementById(errores[i]);
            if (error) {
                error.textContent = ""; 
               
            }
        }
        Cambios.textContent="";
    }
