// Checkout Page Functionality

// Validate checkout form
function validateCheckoutForm(form) {
    const name = form.querySelector('[name="customer_name"]').value.trim();
    const email = form.querySelector('[name="customer_email"]').value.trim();
    const phone = form.querySelector('[name="customer_phone"]').value.trim();
    const tableNumber = form.querySelector('[name="table_number"]').value;
    const paymentMethod = form.querySelector('[name="payment_method"]:checked');
    
    if (!name) {
        alert('Please enter your name');
        return false;
    }
    
    if (!email || !isValidEmail(email)) {
        alert('Please enter a valid email address');
        return false;
    }
    
    if (!phone) {
        alert('Please enter your phone number');
        return false;
    }
    
    if (!tableNumber || tableNumber < 1 || tableNumber > 50) {
        alert('Please enter a valid table number (1-50)');
        return false;
    }
    
    if (!paymentMethod) {
        alert('Please select a payment method');
        return false;
    }
    
    return true;
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Phone validation
function isValidPhone(phone) {
    const phoneRegex = /^[\d\s\-\+\(\)]+$/;
    return phoneRegex.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

// Highlight selected payment method
function selectPayment(radio) {
    const options = document.querySelectorAll('.payment-option');
    options.forEach(option => {
        option.style.background = 'white';
        option.style.border = '1px solid #ddd';
    });
    
    const selectedOption = radio.closest('.payment-option');
    selectedOption.style.background = '#e8f5e9';
    selectedOption.style.border = '2px solid #27ae60';
}

// Show processing message
function processPayment() {
    const button = document.querySelector('button[type="submit"]');
    if (button) {
        button.textContent = 'Processing Payment...';
        button.disabled = true;
    }
}

// Initialize checkout page
document.addEventListener('DOMContentLoaded', function() {
    const checkoutForm = document.querySelector('form[action*="payment"]');
    
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function(e) {
            if (!validateCheckoutForm(this)) {
                e.preventDefault();
                return false;
            }
            processPayment();
        });
    }
    
    // Add event listeners to payment options
    const paymentRadios = document.querySelectorAll('[name="payment_method"]');
    paymentRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            selectPayment(this);
        });
        
        // Highlight if already selected
        if (radio.checked) {
            selectPayment(radio);
        }
    });
    
    // Real-time email validation
    const emailInput = document.querySelector('[name="customer_email"]');
    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            if (this.value && !isValidEmail(this.value)) {
                this.style.borderColor = '#e74c3c';
                alert('Please enter a valid email address');
            } else {
                this.style.borderColor = '#ddd';
            }
        });
    }
    
    // Real-time phone validation
    const phoneInput = document.querySelector('[name="customer_phone"]');
    if (phoneInput) {
        phoneInput.addEventListener('blur', function() {
            if (this.value && !isValidPhone(this.value)) {
                this.style.borderColor = '#e74c3c';
                alert('Please enter a valid phone number');
            } else {
                this.style.borderColor = '#ddd';
            }
        });
    }
});
