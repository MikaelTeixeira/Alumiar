const form = document.querySelector("#form-cadastro");

if (form) {
  form.addEventListener("submit", () => {
    const button = document.querySelector("#register-button");
    if (button) {
      button.textContent = "Enviando...";
      button.disabled = true;
    }
  });
}
