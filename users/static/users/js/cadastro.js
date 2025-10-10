document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.option-btn');
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const target = button.getAttribute('data-target');
      window.location.href = target;
    });
  });
});