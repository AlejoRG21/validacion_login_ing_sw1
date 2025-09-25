document.addEventListener('DOMContentLoaded', () => {
  const tabla = document.getElementById('tabla-usuarios');

  fetch('http://localhost:5000/api/usuarios')
    .then(response => {
      if (!response.ok) {
        throw new Error('Error al obtener los usuarios');
      }
      return response.json();
    })
    .then(data => {
      data.forEach(usuario => {
        const fila = document.createElement('tr');

        fila.innerHTML = `
          <td>${usuario.nombre}</td>
          <td>${usuario.apellido}</td>
          <td>${usuario.tipo_documento} ${usuario.numero_documento}</td>
          <td>${usuario.email}</td>
          <td>${usuario.telefono || ''}</td>
        `;

        tabla.appendChild(fila);
      });
    })
    .catch(error => {
      console.error('Error:', error);
      const fila = document.createElement('tr');
      fila.innerHTML = `<td colspan="5">Error al cargar usuarios</td>`;
      tabla.appendChild(fila);
    });
});
