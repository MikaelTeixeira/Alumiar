function handleReturn() {
    console.log('Retornando...');
    
    
    const content = document.querySelector('.content');
    content.style.opacity = '0';
    content.style.transform = 'translateY(-20px)';
    
    setTimeout(() => {
        
        window.history.back();
        
        
    }, 300);
}


document.addEventListener('DOMContentLoaded', function() {
    const content = document.querySelector('.content');
    
    
    setTimeout(() => {
        content.classList.add('loaded');
    }, 200);
});


const checkIcon = document.querySelector('.check-icon');
if (checkIcon) {
    checkIcon.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.05)';
    });
    
    checkIcon.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
}


const returnButton = document.querySelector('.return-button');
if (returnButton) {
    returnButton.addEventListener('mousedown', function() {
        this.style.transform = 'translateY(0) scale(0.98)';
    });
    
    returnButton.addEventListener('mouseup', function() {
        this.style.transform = 'translateY(-2px) scale(1.02)';
    });
    
    returnButton.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
}


document.body.style.overflow = 'hidden';


document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        handleReturn();
    }
});