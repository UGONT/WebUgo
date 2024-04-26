function validar(){

    const user = document.getElementById("user").value;
    const pass = document.getElementById("pass").value;
    if(String(user).length >= 5 && String(user).length <= 30){
        if(String(pass).length >=8){
            document.getElementById("resultado").innerHTML="<div class='alert alert-success mx-auto'>hola mundo</div>"
        }else{
            document.getElementById("resultado").innerHTML="<div class='alert alert-danger mx-auto'>Contraseña no valida</div>"
        }
    }else{
        document.getElementById("resultado").innerHTML="<div class='alert alert-danger mx-auto'>Usuario no valido</div>"
    }
}

function validar2(){
    
}