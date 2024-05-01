$(document).ready(function () {
    
    $("#btnEnviar").click(function () {
        $("#formulario").submit();
    })

    $("#btnGenerar").click(function () {
        let rut = $("#txtRut").val;
        
    })
    
    function validar(rut){
        if (String(rut).length < 9 || String(rut).length > 10 ) {
            
        }
        else if (condition) {
            
        }
    };
})
