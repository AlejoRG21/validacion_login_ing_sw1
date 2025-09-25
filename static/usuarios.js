document.addEventListener("DOMContentLoaded", () => {
  console.log("Página de usuarios cargada ✅");

  const filas = document.querySelectorAll("tbody tr");
  filas.forEach(fila => {
    fila.addEventListener("click", () => {
      alert(`Usuario: ${fila.cells[2].textContent}`);
    });
  });
});
