$(document).ready(function () {

    /* Funcion registrar */
    $("#btnRegistrar").click(function () {

        let user = $("#txtUser").val();
        let pass = $("#txtPass").val();
        let pass2 = $("#txtPass2").val();
        let email = $("#txtEmail").val();
        console.log(user);
        let resultado = validacionUser(user, pass, pass2, email);
        if (resultado) {

            $("#estado").html("<div class='alert alert-success w-50 mx-auto text-center' >Registro exitoso!</div>");
            setTimeout(() => {
                $("#formularioReg").submit()
            }, 1500);

        }
    })

    /* Funcion Validacion registrar */
    function validacionUser(user, pass, pass2, email) {

        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


        if (String(user).length < 4 || String(user).length > 12) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >El nombre de usuario debe ser entre 4 y 12 caracteres.</div>");
        } else if (String(pass).length < 8 || String(pass).length > 16) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >La contraseña debe ser entre 8 y 16 caracteres.</div>");
        } else if (String(pass2) != String(pass)) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >La contraseña no coincide.</div>");
        } else if (!emailPattern.test(email)) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >El correo no es valido.</div>");
        } else {
            return true;
        }

    }

    /* Funcion Enviar mensaje  */
    $("#botonEnviar").click(function () {

        let nombre = $("#nombre").val();
        let email = $("#correo").val();
        let asunto = $("#asunto").val();
        let mensaje = $("#mensaje").val();
        let resultado = validacionMensaje(nombre, email, asunto, mensaje);
        if (resultado) {
            $("#estado").html("<div class='alert alert-success w-50 mx-auto text-center' >Mensaje enviado!</div>");
            setTimeout(() => {
                $("#fomulario").submit()
            }, 1500);
        }
    })

    /* Funcion Validar mensaje */
    function validacionMensaje(nombre, email, asunto, mensaje) {

        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (String(nombre).length < 3 || String(nombre).length > 14) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >El nombre debe ser entre 3 y 14 caracteres.</div>");
        } else if (!emailPattern.test(email)) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >El correo no es valido.</div>");
        } else if (String(asunto).length < 20) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Asunto con muy pocos caracteres. (+20)</div>");
        } else if (String(mensaje).length < 20) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Mensaje con muy pocos caracteres. (+20)</div>");
        } else {
            return true;
        }
    }

    /* Funcion Validar login */
    $('#btnIniciar').click(function () {
        let email = $('#email').val();
        let pass = $('#pass').val();
        let emailGuardado = localStorage.getItem('email');
        let passGuardada = localStorage.getItem('password');
        if (email == emailGuardado && pass == passGuardada) {
            $("#estado").html("<div class='alert alert-primary w-50 mx-auto text-center' >Ingresaste correctamente!</div>");
            setTimeout(() => {
                $("#formularioIni").submit()
            }, 1500);

        } else {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Correo o contraseña incorrectos.</div>");
            /* setTimeout(() => {
                $("formulario").submit()
            }, 1500); */
            
        }
    })
})


