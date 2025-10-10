function updateDate() {
    const dateElement = document.querySelector('.date-text');
    if (!dateElement) {
        console.error('Elemento .date-text não encontrado no DOM');
        return;
    }
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
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    
    if (!sidebar || !menuToggle) {
        console.error('Elemento .sidebar ou .menu-toggle não encontrado no DOM');
        return;
    }
    
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
           
            if (this.getAttribute('href') === '#') {
                e.preventDefault();
            }
            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');
            sidebar.classList.remove('open');
            menuToggle.classList.remove('open');
            menuToggle.setAttribute('aria-expanded', 'false');
        });
    });
}

function setupQuickButtons() {
    const quickButtons = document.querySelectorAll('.quick-button');
    
    quickButtons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonText = this.querySelector('span').textContent;
            
        });
    });
}

function setupMenuToggle() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (!menuToggle || !sidebar) {
        console.error('Elemento .menu-toggle ou .sidebar não encontrado no DOM');
        return;
    }
    
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

document.addEventListener('DOMContentLoaded', function() {
    updateDate();
    setInterval(updateDate, 1000);
    setupNavigation();
    setupQuickButtons();
    setupMenuToggle();
    console.log('Script carregado. Atualizando data em tempo real e configurando menu toggle.');
});
