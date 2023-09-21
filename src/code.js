const url = 'http://127.0.0.1:8000/';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Error en la solicitud');
    }
    return response.json();
  })
  .then(data => {
  var htmlContent = ``;
  for (var i = 0; i < data.length ; i++){ 
	  htmlContent += `<div class="nota"> <p> nota: ${data[i][0]} fecha: ${data[i][1]} </p> </div>`;
}		  
document.getElementById("notes").innerHTML = htmlContent;
  })
  .catch(error => {
    console.error('Error:', error); // Manejar errores de la solicitud
});

async function newNote(){
  var txt = document.getElementById("textNote").value;
  const postUp = await fetch('http://127.0.0.1:8000/add/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ txt })
  });
    
  if (postUp.ok) {
    console.log('ok');
  } else {
    console.error('Error');
  } 
}
