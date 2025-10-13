const form = document.querySelector("#form-cadastro");

if (form) {
  form.addEventListener("submit", (e) => {
    alert("Cadastro realizado com sucesso!");
  });
}

const inputFile = document.getElementById('foto_perfil');
const checkmark = document.getElementById('checkmark');

if (inputFile && checkmark) {
  inputFile.addEventListener('change', () => {
    if (inputFile.files.length > 0) {
      checkmark.style.display = 'inline';
    } else {
      checkmark.style.display = 'none';
    }
  });
}
