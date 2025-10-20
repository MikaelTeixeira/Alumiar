const form = document.getElementById("form-cadastro");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  alert("Cadastro realizado com sucesso!");
  window.location.href = registeredUrl; 
});
