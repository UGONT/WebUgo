
    function validarRut(){
        let rut = document.getElementById("rut").value;
        console.log(rut);
        if(String(rut).length >=9 && String(rut).length <=10){
            console.log("bien");
        };
    }


