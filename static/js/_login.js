    function validateForm() {

        limpiarErrores()

        let dni = document.getElementById("InputDNI").value;
        let clave = document.getElementById("Inputclave").value;
        let errorDNI = document.getElementById("errorDNI");
        let errorClave = document.getElementById("errorClave");

        errorDNI.textContent = "";
        errorClave.textContent = "";

        let valid = true;

        if(dni == "" || dni == null) {
            errorDNI.textContent = "Por favor, ingrese su DNI.";
            valid = false;
        } else if(isNaN(dni) || dni.length != 8 || (Number.isInteger(dni) && isFinite(dni))) {
            errorDNI.textContent = "El DNI debe tener 8 números.";
            valid = false;
        } 

        var re = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;

        if(clave == "" || clave == null) {
            errorClave.textContent = "Por favor, ingrese su clave.";
            valid = false;
        } else if(!re.test(clave)){ 
            errorClave.textContent = "La clave debe tener mínimo 8 caracteres, 1 mayúscula, 1 número, 1 carácter especial.";
            valid = false;
        }

        return valid;

    }

    function showPassword() {
        var x = document.getElementById("Inputclave");
        var imagenojo = document.getElementById("imagenojo1");
        if (x.type === "password") {
            x.type = "text";
            imagenojo.src = "../static/img/ocultar_clave.png"
        } else {
            x.type = "password";
            imagenojo.src = "../static/img/mostrar_clave.png"
        }
    }

     function limpiarErrores() {
        var errores = ["errorDNI","errorClave","loginMsg"];
        for (var i = 0; i < errores.length; i++) {
            var error = document.getElementById(errores[i]);
            if (error) {
                error.textContent = ""; 
            }
        }
    }