// Restaurant Website - Main JavaScript

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all features
    initCartCounter();
    initFormValidation();
    initPrintButton();
    initMessageDismiss();
    initDateTimeValidation();
    
});

// ===== CART COUNTER =====
function initCartCounter() {
    // Update cart count in navigation if cart exists
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        // Cart count is already rendered by Django template
        // This function can be extended for AJAX cart updates
    }
}

// ===== FORM VALIDATION =====
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#e74c3c';
                } else {
                    field.style.borderColor = '#ddd';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });
}

// ===== PRINT RECEIPT =====
function initPrintButton() {
    const printButtons = document.querySelectorAll('[onclick*="print"]');
    
    printButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            window.print();
        });
    });
}

// ===== MESSAGE DISMISS =====
function initMessageDismiss() {
    const messages = document.querySelectorAll('.messages');
    
    messages.forEach(message => {
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.style.display = 'none';
            }, 300);
        }, 5000);
        
        // Add close button
        const closeBtn = document.createElement('span');
        closeBtn.innerHTML = '&times;';
        closeBtn.style.cssText = 'float: right; cursor: pointer; font-size: 1.5rem; font-weight: bold;';
        closeBtn.onclick = function() {
            message.style.display = 'none';
        };
        message.insertBefore(closeBtn, message.firstChild);
    });
}

// ===== DATE & TIME VALIDATION =====
function initDateTimeValidation() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    const timeInputs = document.querySelectorAll('input[type="time"]');
    
    // Set minimum date to today
    dateInputs.forEach(input => {
        const today = new Date().toISOString().split('T')[0];
        input.setAttribute('min', today);
    });
    
    // Validate time is within restaurant hours (11:00 - 22:00)
    timeInputs.forEach(input => {
        input.addEventListener('change', function() {
            const time = this.value;
            const [hours, minutes] = time.split(':').map(Number);
            
            if (hours < 11 || hours >= 22) {
                alert('Please select a time between 11:00 AM and 10:00 PM');
                this.value = '';
            }
        });
    });
}

// ===== QUANTITY VALIDATION =====
function validateQuantity(input) {
    const value = parseInt(input.value);
    if (value < 1) {
        input.value = 1;
    } else if (value > 99) {
        input.value = 99;
    }
}

// ===== CONFIRM REMOVE FROM CART =====
function confirmRemove(itemName) {
    return confirm(`Remove ${itemName} from cart?`);
}

// ===== SMOOTH SCROLL =====
function smoothScroll(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// ===== ADD TO CART ANIMATION =====
function addToCartAnimation(button) {
    const originalText = button.textContent;
    button.textContent = '✓ Added!';
    button.style.background = '#27ae60';
    
    setTimeout(() => {
        button.textContent = originalText;
        button.style.background = '';
    }, 1500);
}

// ===== LOADING SPINNER =====
function showLoading() {
    const spinner = document.createElement('div');
    spinner.id = 'loading-spinner';
    spinner.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
        background: rgba(0,0,0,0.8);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
    `;
    spinner.innerHTML = '<div style="font-size: 2rem;">⏳</div><div>Processing...</div>';
    document.body.appendChild(spinner);
}

function hideLoading() {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) {
        spinner.remove();
    }
}

// ===== FORM SUBMISSION WITH LOADING =====
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        // Show loading for forms that submit data
        if (this.method.toLowerCase() === 'post') {
            showLoading();
        }
    });
});

// ===== PAYMENT METHOD SELECTION =====
function selectPaymentMethod(method) {
    const radios = document.querySelectorAll('input[name="payment_method"]');
    radios.forEach(radio => {
        if (radio.value === method) {
            radio.checked = true;
        }
    });
}

// ===== TABLE NUMBER VALIDATION =====
function validateTableNumber(input) {
    const value = parseInt(input.value);
    if (value < 1) {
        input.value = 1;
    } else if (value > 50) {
        input.value = 50;
    }
}

// ===== GUEST COUNT VALIDATION =====
function validateGuestCount(input) {
    const value = parseInt(input.value);
    if (value < 1) {
        input.value = 1;
    } else if (value > 20) {
        alert('For parties larger than 20 guests, please call us at (555) 123-4567');
        input.value = 20;
    }
}

// ===== COPY ORDER ID =====
function copyOrderId(orderId) {
    const tempInput = document.createElement('input');
    tempInput.value = orderId;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    
    alert('Order ID copied to clipboard!');
}

// ===== BACK TO TOP BUTTON =====
window.addEventListener('scroll', function() {
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        if (window.pageYOffset > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    }
});

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// ===== CONSOLE WELCOME MESSAGE =====
console.log('%c🍽️ Welcome to Delicious Bites Restaurant! ', 'background: #e74c3c; color: white; font-size: 20px; padding: 10px;');
console.log('%cEnjoy your dining experience!', 'color: #2c3e50; font-size: 14px;');

// ===== EXPORT FUNCTIONS FOR INLINE USE =====
window.validateQuantity = validateQuantity;
window.confirmRemove = confirmRemove;
window.smoothScroll = smoothScroll;
window.addToCartAnimation = addToCartAnimation;
window.selectPaymentMethod = selectPaymentMethod;
window.validateTableNumber = validateTableNumber;
window.validateGuestCount = validateGuestCount;
window.copyOrderId = copyOrderId;
window.scrollToTop = scrollToTop;
