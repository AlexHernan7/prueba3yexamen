
const formulario = document.getElementById('formulario'); 
const arrayDatosFormulario = []; 

formulario.addEventListener('submit', function(evento) { 
  evento.preventDefault(); 
  


  const nombre = document.getElementById('name').value;
  const apPaterno = document.getElementById('apPaterno').value;
  const apMaterno = document.getElementById('apMaterno').value;
  const rut = document.getElementById('rut').value;
  const genero = document.getElementById('select-box').value;
  const direccion = document.getElementById('direccion').value;
  const email = document.getElementById('email').value;
  const telefono = document.getElementById('phone').value;
  const mensaje = document.getElementById('message').value;

  if (!nombre || !email) {
    alert('Por favor, complete todos los campos obligatorios.'); 
    return;
  }
  if (!apPaterno && !apMaterno) {
    alert('Ingrese un apellido valido'); 
    return;
  }
  if (!rut) {
    alert('Ingrese un rut valido'); 
    return;
  }
  if (!direccion) {
    alert('Ingrese una direccion valida'); 
    return;
  }
  if (!telefono) {
    alert('Ingrese un telefono valido'); 
    return;
  }

  const datosFormulario = {nombre, apPaterno, apMaterno, rut, genero, direccion, email, telefono, mensaje};


  arrayDatosFormulario.push(datosFormulario);


  console.log(arrayDatosFormulario);

  alert('Formulario enviado con exito..');

  document.getElementById("formulario").reset();
});

// Page Vehicles





