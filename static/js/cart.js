// Cart Functionality

// Update cart quantity
function updateCartQuantity(itemId, quantity) {
    if (quantity < 1) {
        if (confirm('Remove this item from cart?')) {
            window.location.href = `/remove-from-cart/${itemId}/`;
        }
        return false;
    }
    
    if (quantity > 99) {
        alert('Maximum quantity is 99');
        return false;
    }
    
    return true;
}

// Add to cart with animation
function addToCart(button, itemId) {
    const originalText = button.textContent;
    const originalBg = button.style.background;
    
    button.textContent = '✓ Added to Cart!';
    button.style.background = '#27ae60';
    button.disabled = true;
    
    setTimeout(() => {
        button.textContent = originalText;
        button.style.background = originalBg;
        button.disabled = false;
    }, 1500);
}

// Calculate cart total
function calculateCartTotal() {
    let total = 0;
    const items = document.querySelectorAll('.cart-item');
    
    items.forEach(item => {
        const price = parseFloat(item.dataset.price);
        const quantity = parseInt(item.querySelector('.quantity-input').value);
        total += price * quantity;
    });
    
    const totalElement = document.querySelector('.cart-total');
    if (totalElement) {
        totalElement.textContent = `$${total.toFixed(2)}`;
    }
}

// Confirm remove from cart
function confirmRemoveFromCart(itemName) {
    return confirm(`Remove "${itemName}" from your cart?`);
}

// Update cart count in navigation
function updateCartCount() {
    const cartItems = document.querySelectorAll('.cart-item');
    const cartCount = document.querySelector('.cart-count');
    
    if (cartCount) {
        let totalItems = 0;
        cartItems.forEach(item => {
            const quantity = parseInt(item.querySelector('.quantity-input').value);
            totalItems += quantity;
        });
        cartCount.textContent = totalItems;
    }
}

// Initialize cart page
document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners to quantity inputs
    const quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            calculateCartTotal();
            updateCartCount();
        });
    });
    
    // Calculate initial total
    calculateCartTotal();
    updateCartCount();
});
