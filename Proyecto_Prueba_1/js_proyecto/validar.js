$(document).ready(function () {

    $("#btnRegistrar").click(function () {

        let user = $("#txtUser").val();
        let pass = $("#txtPass").val();
        let pass2 = $("#txtPass2").val();
        let email = $("#txtEmail").val();
        console.log(user);
        let resultado = validacion(user, pass, pass2);
        if (resultado) {
            $("#estado").html("<div class='alert alert-success w-50 mx-auto text-center' >Registro exitoso!</div>");
            $("#formulario").submit();

        }
    })

    function validacion(user, pass, pass2) {

        if (String(user).length < 4 || String(user).length > 12) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >El nombre de usuario debe ser entre 4 y 12 caracteres.</div>");
        } else if (String(pass).length < 8 || String(pass).length > 16) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >La contraseña debe ser entre 8 y 16 caracteres.</div>");
        } else if (String(pass2) != String(pass)) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >La contraseña no coincide.</div>");
        }
        else {
            return true;
        }

    }

})
