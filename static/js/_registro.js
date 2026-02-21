    function validateFormRegistrarse() {

        limpiarErrores()

        let nombre = document.getElementById("Inputnombre").value;
        let apellido = document.getElementById("Inputapellido").value;
        let dni = document.getElementById("InputDNI").value;
        let clave1 = document.getElementById("Inputclave1").value;
        let clave2 = document.getElementById("Inputclave2").value;

        let errorNombre = document.getElementById("errorNombre");
        let errorApellido = document.getElementById("errorApellido");
        let errorDNI = document.getElementById("errorDNI");
        let errorClave1 = document.getElementById("errorClave1");
        let errorClave2 = document.getElementById("errorClave2");
        let errorClave = document.getElementById("errorClave");
        let errorForm = document.getElementById("errorForm");

        errorNombre.textContent = "";
        errorApellido.textContent = "";
        errorDNI.textContent = "";
        errorClave1.textContent = "";
        errorClave2.textContent = "";
        errorForm.textContent = "";

        let valid = true;

        if((nombre == "" || nombre == null) || (apellido == "" || apellido == null) || (dni == "" || dni == null) || (clave1 == "" || clave1 == null) || (clave2 == "" || clave2 == null)){
            errorForm.textContent = "Por favor llenar todos los campos.";
            valid = false;
        }

        if((nombre != "" && nombre != null) && !soloLetras(nombre)) { 
            errorNombre.textContent = "El nombre no puede contener numeros.";
            valid = false;
        } else if(!noSpaces(nombre)) {
            errorNombre.textContent = "El nombre no puede contener 2 o mas espacios seguidos.";
            valid = false;
        }

        if((apellido != "" && apellido != null) && !soloLetras(apellido)) { 
            errorApellido.textContent = "El apellido no puede contener numeros.";
            valid = false;
        } else if(!noSpaces(apellido)) {
            errorApellido.textContent = "El apellido no puede contener 2 o mas espacios seguidos.";
            valid = false;
        }
 
        if((dni != "" && (isNaN(dni) || dni.length != 8))){
            errorDNI.textContent = "El DNI debe tener 8 numeros.";
            valid = false;
        }

        var re = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;

        if((clave1 != "" && clave1 != null)  && (!re.test(clave1))) {
            errorClave1.textContent = "La clave debe tener minimo 8 caracteres, 1 mayuscula, 1 numero, 1 caracter especial.";
            valid = false;
        }

        if((clave2 != "" && clave2 != null) && (!re.test(clave2))) {
            errorClave2.textContent = "La clave debe tener minimo 8 caracteres, 1 mayuscula, 1 numero, 1 caracter especial.";
            valid = false;
        }
        
        if(clave1 != clave2) {
            errorClave.textContent = "Las claves deben coincidir.";
            valid = false;
        }

        if (!observaciones()) {
            valid = false;
        }

        return valid;

    }

    function showPassword1() {
        var x = document.getElementById("Inputclave1");
        var imagenojo = document.getElementById("imagenojo1");
        if (x.type === "password") {
            x.type = "text";
            imagenojo.src = "../static/img/ocultar_clave.png"
        } else {
            x.type = "password";
            imagenojo.src = "../static/img/mostrar_clave.png"
        }
    }

    function showPassword2() {
        var y = document.getElementById("Inputclave2");
        var imagenojo = document.getElementById("imagenojo2");

        if (y.type === "password") {
            y.type = "text";
            imagenojo.src = "../static/img/ocultar_clave.png"
        } else {
            y.type = "password";
            imagenojo.src = "../static/img/mostrar_clave.png"
        }
    }
    function soloLetras(input) {
        // Esta expresión regular comprueba si la cadena contiene solo letras (mayúsculas o minúsculas)
        // El ^ al inicio y el $ al final aseguran que toda la cadena coincida, no solo una parte.
        // El + indica que debe haber al menos un carácter.
        const regex = /^\p{L}+$/u;
        return regex.test(input);
    }
    function noSpaces(input){
        const regex = /^(?!.* {2,}).*$/;
        return regex.test(input);
    }


    function observaciones(){
        var checkboxObs = document.getElementById("restriccion4");
        var InputObs = document.getElementById("observaciones"); 
        var errorObs = document.getElementById("errorObs");

        errorObs.textContent = "";

        if (checkboxObs.checked && InputObs.value.trim() === ""){
            errorObs.textContent = "Debe ingresar su(s) observacion(es).";
            return false;
        }
        return true;
    }

    function limpiarErrores() {
        var errores = ["errorNombre","errorApellido","errorDNI","errorClave1","errorClave2","errorClave","errorForm","errorObs","Msg"];
        for (var i = 0; i < errores.length; i++) {
            var error = document.getElementById(errores[i]);
            if (error) {
                error.textContent = ""; 
            }
        }
    }