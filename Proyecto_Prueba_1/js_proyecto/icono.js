// Mostrar el botón "Volver Arriba" cuando el usuario haga scroll hacia abajo
window.addEventListener('scroll', function() {
    var btnVolverArriba = document.getElementById('btnVolverArriba');
    if (window.scrollY > 100) { // Cambiar este valor según prefieras
      btnVolverArriba.style.display = 'block';
    } else {
      btnVolverArriba.style.display = 'none';
    }
  });
  
  // Desplazamiento suave hacia arriba cuando se hace clic en el botón
  document.getElementById('btnVolverArriba').addEventListener('click', function() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth' // Hace que el desplazamiento sea suave
    });
  });