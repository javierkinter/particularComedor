function validateForm(){
    var horario=document.getElementById("horario1").value;
    let errorHorario=document.getElementById("errorHorario");
    let valid=true;

    errorHorario.textContent="";
        
    if (horario===""){
        errorHorario.textContent="Por favor, ingrese su horario";
        valid=false;
    }

    return valid;
}

function mostrarFecha(){
    const fecha = new Date();
    const dia = fecha.getDate();
    const mes = fecha.getMonth();
    const anio = fecha.getFullYear();

    var meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"];
    document.getElementById("fecha").innerHTML = dia + " de " + meses[mes] + " de " + anio;
}
mostrarFecha();

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
