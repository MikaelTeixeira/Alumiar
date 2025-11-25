document.getElementById("saveBtn").addEventListener("click", () => {
    document.getElementById("personalInfoForm").submit();
});


function updateDate() {
    const dateElement = document.querySelector('.date-text');
    if (!dateElement) return;

    const now = new Date();
    const timeString = now.toLocaleString('pt-BR', {
        timeZone: 'America/Sao_Paulo',
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });

    dateElement.textContent = timeString.charAt(0).toUpperCase() + timeString.slice(1);
}


function setupNavigation() {
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault();

            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');

            const text = this.textContent.trim();

            // DASHBOARD: redireciona por tipo de usuário
            if (text === "Dashboard") {
                if (typeof USER_TYPE !== "undefined" && USER_TYPE === "PAT") {
                    window.location.href = "/users/logged/homepage/";
                } else {
                    window.location.href = "/users/logged/psychologist-dashboard/";
                }
                return;
            }

            if (text === "Marcar Consulta") {
                window.location.href = "/users/logged/consulta/";
                return;
            }

            if (text === "Configurações") {
                const sidebar = document.querySelector('.sidebar');
                const menuToggle = document.querySelector('.menu-toggle');
                if (sidebar && menuToggle) {
                    sidebar.classList.remove("open");
                    menuToggle.classList.remove("open");
                }
                return;
            }
        });
    });
}

function setupMenuToggle() {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');

    if (!sidebar || !menuToggle) {
        console.warn("Sidebar ou menu-toggle não encontrados.");
        return;
    }

    menuToggle.addEventListener('click', function () {
        sidebar.classList.toggle('open');
        menuToggle.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', sidebar.classList.contains('open'));
    });

    document.addEventListener('click', function (e) {
        if (!sidebar.contains(e.target) && !menuToggle.contains(e.target)) {
            sidebar.classList.remove('open');
            menuToggle.classList.remove('open');
            menuToggle.setAttribute('aria-expanded', 'false');
        }
    });
}

function setupSaveButton() {
    const saveBtn = document.getElementById('saveBtn');
    const form = document.getElementById('personalInfoForm');

    saveBtn.addEventListener('click', function (e) {
        e.preventDefault();

        saveBtn.textContent = 'Salvando...';
        saveBtn.disabled = true;

        setTimeout(() => {
            saveBtn.textContent = 'Salvo!';
            setTimeout(() => {
                saveBtn.textContent = 'Salvar Alterações';
                saveBtn.disabled = false;
            }, 1500);
        }, 1000);

        form.submit();
    });
}


function setupDeleteAccount() {
    const deleteBtn = document.getElementById('deleteAccountBtn');

    deleteBtn.addEventListener('click', function () {
        const c1 = confirm("Tem certeza que deseja excluir sua conta?");
        if (!c1) return;

        const c2 = confirm("Última chance: excluir permanentemente?");
        if (!c2) return;

        alert("Conta excluída com sucesso.");
        window.location.href = "/users/logged/delete-account/";
    });
}


function setupToggles() {
    const toggles = document.querySelectorAll('.toggle input[type="checkbox"]');

    toggles.forEach(toggle => {
        toggle.addEventListener('change', function () {
            const parent = this.closest('.notification-item');
            const label = parent.querySelector('span').textContent;
            console.log(`${this.checked ? "Ativou" : "Desativou"}: ${label}`);
        });
    });
}

function setupFormValidation() {
    const inputs = document.querySelectorAll('.settings-form input');

    inputs.forEach(input => {
        input.addEventListener('blur', function () {
            if (this.type === 'email' && this.value && !validateEmail(this.value)) {
                this.style.borderColor = '#ef4444';
            }
        });

        input.addEventListener('input', function () {
            this.style.borderColor = '#e5e7eb';
        });
    });
}

function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}


document.addEventListener('DOMContentLoaded', function () {
    updateDate();
    setInterval(updateDate, 60000);

    setupNavigation();
    setupMenuToggle();
    setupSaveButton();
    setupDeleteAccount();
    setupToggles();
    setupFormValidation();

    console.log("configuration.js carregado com sucesso.");
});
