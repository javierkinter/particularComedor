function mostrarFecha(){
    const fecha = new Date();
    const dia = fecha.getDate()
    const mes = fecha.getMonth()
    const anio = fecha.getFullYear()

    var meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    document.getElementById("fecha").innerHTML = dia + " de " + meses[mes] + " de " + anio;
    
    }
mostrarFecha()