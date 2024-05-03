$(document).ready(function () {
    
    $("#btnEnviar").click(function () {
        $("#formulario").submit();
    })

    $("#btnGenerar").click(function () {
        let rut = $("#txtRut").val();
        let nombre = $("#txtNombre").val();
        let apellidoPat = $("#txtApellidoPat").val();
        let apellidoMat = $("#txtApellidoMat").val();
        let edad = $("#txtEdad").val();
        let valorSeleccionado = $("#optGenero").val();
        let textoSeleccionado = $("#optGenero").find("option:selected").text();
        let celular = $("#txtCelular").val();
        
        let res = validar(rut,nombre,apellidoPat,apellidoMat,edad,valorSeleccionado,celular);
        if(res){
            $("#estado").html("<div class='alert alert-success w-50 mx-auto text-center' >WEna</div>");
            
        };
        
    })
    
    function validar(rut,nombre,apellidoPat,apellidoMat,edad,valorSeleccionado,celular){
        if (String(rut).length < 9 || String(rut).length > 10 ) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Rut debe tener largo entre 9 y 10 caracteres.</div>");
   
        }else if (String(nombre).length < 3 || String(nombre).length > 20)  {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Nombre debe tener largo entre 3 y 20 caracteres.</div>");

        }else if (String(apellidoPat).length < 3 || String(apellidoPat).length > 20)  {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Paterno debe tener largo entre 3 y 20 caracteres.</div>");

        }else if (String(apellidoMat).length < 3 || String(apellidoMat).length > 20)  {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Materno debe tener largo entre 3 y 20 caracteres.</div>");
        
        }else if (Number(edad) < 18 || Number(edad) > 35) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Edad debe ser entre 18 y 35 años.</div>");
        
        }else if (Number(valorSeleccionado) == 0) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Debes seleccionar un genero.</div>");
        
        }else if (String(celular).length < 9 || String(celular).length > 12) {
            $("#estado").html("<div class='alert alert-danger w-50 mx-auto text-center' >Numero de celular no valido, debe ser entre 9 y 12 digitos.</div>");
        }
        else{
            return true;
        }
    };
});
