document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('registroForm');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const contrasena = document.getElementById('contrasena').value;

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

    alert("Registro exitoso ✅");
  });
});
