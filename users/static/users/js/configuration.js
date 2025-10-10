function updateDate() {
    const dateElement = document.querySelector('.date-text');
    const days = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'];
    const months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
    
    const now = new Date();
    const dayName = days[now.getDay()];
    const day = now.getDate();
    const month = months[now.getMonth()];
    const year = now.getFullYear();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    
    dateElement.textContent = `${dayName}, ${day} de ${month} de ${year}, ${hours}:${minutes}`;
}

function setupNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');
            
            
            if (this.textContent.trim() === 'Dashboard') {
                window.location.href = 'home.html';
            }
            
            
            if (this.textContent.trim() === 'Marcar Consulta') {
                window.location.href = 'consulta.html';
            }
            
            
            if (this.textContent.trim() === 'Configurações') {
                sidebar.classList.remove('open');
                menuToggle.classList.remove('open');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    });
}

function setupSaveButton() {
    const saveBtn = document.getElementById('saveBtn');
    const form = document.getElementById('personalInfoForm');
    
    saveBtn.addEventListener('click', function(e) {
        e.preventDefault();
        const formData = new FormData(form);
        console.log('Salvando alterações...');
        saveBtn.textContent = 'Salvando...';
        saveBtn.disabled = true;
        setTimeout(() => {
            saveBtn.textContent = 'Salvo!';
            setTimeout(() => {
                saveBtn.textContent = 'Salvar Alterações';
                saveBtn.disabled = false;
            }, 1500);
        }, 1000);
        alert('Configurações salvas com sucesso!');
    });
}

function setupDeleteAccount() {
    const deleteBtn = document.getElementById('deleteAccountBtn');
    
    deleteBtn.addEventListener('click', function() {
        const confirmation = confirm('Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.');
        if (confirmation) {
            const doubleConfirmation = confirm('Esta é sua última chance. Realmente deseja excluir sua conta permanentemente?');
            if (doubleConfirmation) {
                alert('Conta excluída com sucesso. Você será redirecionado para a página inicial.');
                console.log('Conta excluída');
                
                window.location.href = 'login.html';
            }
        }
    });
}

function setupToggles() {
    const toggles = document.querySelectorAll('.toggle input[type="checkbox"]');
    
    toggles.forEach(toggle => {
        toggle.addEventListener('change', function() {
            const parent = this.closest('.notification-item');
            const label = parent.querySelector('span').textContent;
            if (this.checked) {
                console.log(`Notificação ativada: ${label}`);
            } else {
                console.log(`Notificação desativada: ${label}`);
            }
        });
    });
}

function setupFormValidation() {
    const inputs = document.querySelectorAll('.settings-form input');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.type === 'email' && this.value) {
                if (!validateEmail(this.value)) {
                    this.style.borderColor = '#ef4444';
                } else {
                    this.style.borderColor = '#e5e7eb';
                }
            }
        });
        
        input.addEventListener('input', function() {
            this.style.borderColor = '#e5e7eb';
        });
    });
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function setupMenuToggle() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
            menuToggle.classList.toggle('open');
            menuToggle.setAttribute('aria-expanded', sidebar.classList.contains('open'));
        });

        document.addEventListener('click', function(e) {
            if (!sidebar.contains(e.target) && !menuToggle.contains(e.target)) {
                sidebar.classList.remove('open');
                menuToggle.classList.remove('open');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    updateDate();
    setInterval(updateDate, 60000); 
    setupNavigation();
    setupSaveButton();
    setupDeleteAccount();
    setupToggles();
    setupFormValidation();
    setupMenuToggle();
    console.log('Sistema de Configurações carregado!');
});