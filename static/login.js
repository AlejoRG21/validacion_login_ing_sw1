document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('loginForm');

  if (!form) {
    console.error("Formulario no encontrado: asegúrate de que el ID 'loginForm' esté en el HTML.");
    return;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const usuario = document.getElementById('usuario').value.trim();
    const contrasena = document.getElementById('contrasena').value.trim();

    const soloLetras = /^[A-Za-z]+$/;
    const soloNumeros = /^\d+$/;

    if (!soloLetras.test(usuario)) {
      alert("El usuario solo debe contener letras.");
      return;
    }

    if (!soloNumeros.test(contrasena)) {
      alert("La contraseña solo debe contener números.");
      return;
    }

    alert("Inicio de sesión exitoso 🔓");
    // Aquí puedes redirigir al usuario o guardar datos si lo deseas.

        window.location.href = ".././templates/usuarios.html";

  });
});
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que se recargue la página

    const usuario = document.getElementById('usuario').value.trim();
    const contrasena = document.getElementById('contrasena').value.trim();

    if (!usuario || !contrasena) {
      alert('Por favor ingresa usuario y contraseña.');
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario, contrasena })
      });

      const result = await response.json();

      if (response.ok) {
        alert('Inicio de sesión exitoso');
        // Puedes guardar datos en localStorage/sessionStorage si usas JWT
        window.location.href = './dashboard.html'; // o a donde quieras redirigir
      } else {
        alert(result.error || 'Error al iniciar sesión');
      }

    } catch (error) {
      console.error('Error de red:', error);
      alert('Error al conectar con el servidor.');
    }
  });
});
