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
    window.location.href = ".././templates/login.html";
  });
});
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registerForm');

  form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevenir envío automático

    // Captura de datos del formulario
    const nombre = document.getElementById('nombre').value.trim();
    const apellido = document.getElementById('apellido').value.trim();
    const tipo_documento = document.getElementById('tipo_doc').value;
    const numero_documento = document.getElementById('num_doc').value.trim();
    const email = document.getElementById('correo').value.trim();
    const telefono = document.getElementById('telefono').value.trim();
    const usuario = document.getElementById('usuario').value.trim();
    const contrasena = document.getElementById('password').value.trim();

    // Validación rápida
    if (!nombre || !apellido || !tipo_documento || !numero_documento || !email || !telefono || !usuario || !contrasena) {
      Swal.fire('Error', 'Por favor completa todos los campos.', 'error');
      return;
    }

    // Estructura del JSON
    const datos = {
      nombre,
      apellido,
      tipo_documento,
      numero_documento,
      email,
      telefono,
      usuario,
      contrasena
    };

    try {
      const respuesta = await fetch('http://localhost:5000/api/usuarios', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
      });

      const resultado = await respuesta.json();

      if (respuesta.ok) {
        Swal.fire('¡Registro exitoso!', resultado.mensaje, 'success').then(() => {
          form.reset();
          window.location.href = './login.html';
        });
      } else {
        Swal.fire('Error', resultado.error || 'No se pudo registrar al usuario.', 'error');
      }

    } catch (error) {
      console.error('Error al registrar:', error);
      Swal.fire('Error', 'No se pudo conectar con el servidor.', 'error');
    }
  });
});
