function cancelar(){
    var x = document.getElementById("hoy");
    const Borrar = document.getElementById("cancelar");
    if (x.innerHTML === "") {
        x.innerHTML = "<p class='datos'>Menu seleccionado: Milanesa con puré</p>" +
                        "<p>Fecha del pedido: 15-09-25 </p>";
    } else {
        x.innerHTML = ""
        Borrar.disabled = true;
    }
}
