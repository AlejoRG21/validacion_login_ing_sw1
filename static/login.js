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
