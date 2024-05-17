
window.addEventListener('scroll', function() {
    var btnVolverArriba = document.getElementById('btnVolverArriba');
    if (window.scrollY > 100) { 
      btnVolverArriba.style.display = 'block';
      
    } else {
      btnVolverArriba.style.display = 'none';
    }
  });

  document.getElementById('btnVolverArriba').addEventListener('click', function() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });