let currentStep = 1;
let selectedTopic = 'orientacao';
let calendar;

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
    
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');
            if (this.textContent.trim() === 'Marcar Consulta') {
                e.preventDefault();
                sidebar.classList.remove('open');
                menuToggle.classList.remove('open');
                menuToggle.setAttribute('aria-expanded', 'false');
            } else if (this.textContent.trim() === 'Dashboard' || this.textContent.trim() === 'Configurações') {
                // Permite o redirecionamento para home.html ou configuracao.html
                return; // Não impede o comportamento padrão do href
            }
        });
    });
}

function setupTopicSelection() {
    const topicCards = document.querySelectorAll('.topic-card');
    
    topicCards.forEach(card => {
        card.addEventListener('click', function() {
            topicCards.forEach(c => c.classList.remove('active'));
            this.classList.add('active');
            selectedTopic = this.getAttribute('data-topic');
            console.log('Tópico selecionado:', selectedTopic);
        });
    });
}

function setupContinueButton() {
    const continueBtn = document.getElementById('continueBtn');
    const dateStep = document.getElementById('dateStep');
    
    continueBtn.addEventListener('click', function() {
        if (currentStep === 1) {
            alert(`Avançando para a próxima etapa!\nTópico selecionado: ${selectedTopic === 'orientacao' ? 'Orientação de Enaites' : 'Aconselhamento Emocional'}`);
            currentStep = 2;
            dateStep.classList.remove('disabled');
            dateStep.classList.add('active');
            initializeCalendar();
        } else if (currentStep === 2) {
            alert('Avançando para a etapa de confirmação!');
            currentStep = 3;
            // Adicionar lógica para a etapa 3, se necessário
        }
    });
}

function initializeCalendar() {
    const calendarInput = document.getElementById('calendarInput');
    const calendarPlaceholder = document.getElementById('calendarPlaceholder');
    
    if (calendarInput && !calendar) {
        calendar = flatpickr(calendarInput, {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            minDate: new Date(), // Desativa datas passadas
            time_24hr: true,
            onReady: () => {
                calendarPlaceholder.style.display = 'none'; // Esconde o ícone placeholder
            },
            onChange: (selectedDates, dateStr, instance) => {
                console.log('Data e horário selecionados:', dateStr);
            }
        });
    }
}

function setupCancelButton() {
    const cancelBtn = document.getElementById('cancelBtn');
    
    cancelBtn.addEventListener('click', function() {
        if (confirm('Deseja realmente cancelar o agendamento?')) {
            alert('Agendamento cancelado!');
            window.location.href = 'index.html';
        }
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
    setInterval(updateDate, 1000); // Atualiza a cada segundo
    setupNavigation();
    setupTopicSelection();
    setupContinueButton();
    setupCancelButton();
    setupMenuToggle();
});