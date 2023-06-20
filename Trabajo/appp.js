const marcaSelect = document.getElementById("marca");
const modeloSelect = document.getElementById("modelo");
const resultadoDiv = document.getElementById("resultado");

function cargarModelos() {
  modeloSelect.innerHTML = "<option value=''>Seleccione un modelo</option>";

  const marcaSeleccionada = marcaSelect.value;

  if (marcaSeleccionada !== "") {
    fetch("vehiculos.json")
      .then(response => response.json())
      .then(data => {
        const marca = data.marcas.find(m => m.nombre === marcaSeleccionada);

        if (marca) {
          // recorrer el arreglo de marcas buscando el modelo
          marca.modelos.forEach(modelo => {
            const option = document.createElement("option");
            option.value = modelo.nombre;
            option.text = modelo.nombre;
            // agregar modelos al option
            modeloSelect.appendChild(option);
          });
        }
      })
      .catch(error => {
        console.error("Error:", error);
      });
  }
}

// mostrar info del vehiculo seleccionado
function mostrarInfo() {
  const marcaSeleccionada = marcaSelect.value;
  const modeloSeleccionado = modeloSelect.value;

  if (marcaSeleccionada !== "" && modeloSeleccionado !== "") {
    fetch("vehiculos.json")
      .then(response => response.json())
      .then(data => {
        const marca = data.marcas.find(m => m.nombre === marcaSeleccionada);

        if (marca) {
          // buscar el modelo ya teniendo la marca seleccionada
          const modelo = marca.modelos.find(m => m.nombre === modeloSeleccionado);

          if (modelo) {
            // modelo del html replicado
            const html = `
              <h2>${marcaSeleccionada} ${modeloSeleccionado}</h2>
              <img style="max-width: 370px; max-height: 370px;" src="${modelo.imagen}" alt="${marcaSeleccionada} ${modeloSeleccionado}">
              <p>Kilometraje: ${modelo.kilometraje}</p>
              <p>Estado: ${modelo.estado}</p>
              <p>Monto: ${modelo.monto}</p>
              <p>País: ${modelo.pais}</p>
            `;
            resultadoDiv.innerHTML = html;
          }
        }
      })
      .catch(error => {
        console.error("Error:", error);
      });
  } else {
    resultadoDiv.innerHTML = "";
  }
}