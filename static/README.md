# Static Files Organization

This folder contains all CSS and JavaScript files for the restaurant website.

## 📁 Folder Structure

```
static/
├── css/
│   ├── style.css       # Main stylesheet (base styles)
│   ├── cart.css        # Cart page specific styles
│   ├── checkout.css    # Checkout page specific styles
│   └── receipt.css     # Receipt page specific styles
│
└── js/
    ├── main.js         # Main JavaScript (global functions)
    ├── cart.js         # Cart functionality
    └── checkout.js     # Checkout validation and processing
```

## 🎨 CSS Files

### style.css (Main Stylesheet)
Contains all base styles including:
- Reset and base styles
- Navigation
- Buttons
- Forms
- Grid layouts
- Menu items
- Categories
- Footer
- Responsive design
- Utility classes

**Used by:** All pages (loaded in base.html)

### cart.css
Cart page specific styles:
- Cart table layout
- Quantity controls
- Remove buttons
- Empty cart message
- Cart actions

**Used by:** cart.html

### checkout.css
Checkout page specific styles:
- Two-column layout
- Payment method selection
- Order summary sidebar
- Form styling

**Used by:** checkout.html

### receipt.css
Receipt page specific styles:
- Success header
- Receipt layout
- Order details grid
- Print styles
- Thank you message

**Used by:** receipt.html

## 📜 JavaScript Files

### main.js (Main JavaScript)
Global functionality:
- Form validation
- Message dismiss
- Date/time validation
- Print functionality
- Loading spinner
- Utility functions

**Used by:** All pages (loaded in base.html)

### cart.js
Cart specific functionality:
- Quantity updates
- Cart total calculation
- Add to cart animation
- Remove confirmation
- Cart count update

**Used by:** cart.html, order_food.html

### checkout.js
Checkout specific functionality:
- Form validation
- Email validation
- Phone validation
- Payment method selection
- Processing animation

**Used by:** checkout.html

## 🔧 How to Use

### In Templates

**Load static files:**
```django
{% load static %}
```

**Include CSS:**
```django
{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/filename.css' %}">
{% endblock %}
```

**Include JavaScript:**
```django
{% block extra_js %}
<script src="{% static 'js/filename.js' %}"></script>
{% endblock %}
```

### Example Template Structure

```django
{% extends 'restaurant/base.html' %}
{% load static %}

{% block title %}Page Title{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/page-specific.css' %}">
{% endblock %}

{% block content %}
<!-- Page content here -->
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/page-specific.js' %}"></script>
{% endblock %}
```

## 🎯 Benefits of This Organization

### Separation of Concerns
- HTML structure in templates
- CSS styling in separate files
- JavaScript behavior in separate files

### Maintainability
- Easy to find and edit styles
- No inline styles in templates
- Organized by functionality

### Performance
- Browser caching of static files
- Minification possible
- Parallel loading

### Reusability
- Shared styles in main stylesheet
- Page-specific styles in separate files
- Modular JavaScript functions

### Scalability
- Easy to add new pages
- Easy to add new features
- Clear file structure

## 📝 CSS Classes Reference

### Layout Classes
- `.container` - Main content container (max-width: 1200px)
- `.hero` - Hero section with background image
- `.section-title` - Centered section titles

### Component Classes
- `.btn` - Primary button
- `.btn-secondary` - Secondary button
- `.menu-grid` - Grid layout for menu items
- `.menu-item` - Individual menu item card
- `.feature-box` - Feature box with icon
- `.category` - Category section

### Utility Classes
- `.text-center` - Center text
- `.mt-1`, `.mt-2`, `.mt-3` - Margin top
- `.mb-1`, `.mb-2`, `.mb-3` - Margin bottom
- `.p-1`, `.p-2`, `.p-3` - Padding
- `.bg-light` - Light background
- `.bg-primary` - Primary color background
- `.text-primary` - Primary color text
- `.text-success` - Success color text
- `.rounded` - Rounded corners
- `.shadow` - Box shadow

## 🎨 Color Scheme

```css
Primary: #e74c3c (Red)
Secondary: #2c3e50 (Dark Blue)
Success: #27ae60 (Green)
Light: #f8f9fa (Light Gray)
Text: #333 (Dark Gray)
Muted: #666 (Medium Gray)
```

## 📱 Responsive Breakpoints

```css
Mobile: max-width: 768px
Tablet: 769px - 1024px
Desktop: 1025px+
```

## 🔄 Loading Order

1. **base.html loads:**
   - style.css (main stylesheet)
   - main.js (global functions)

2. **Page-specific templates load:**
   - Page-specific CSS (via extra_css block)
   - Page-specific JS (via extra_js block)

## 🚀 Production Optimization

### For Production Deployment:

1. **Collect Static Files:**
   ```bash
   python manage.py collectstatic
   ```

2. **Minify CSS:**
   - Use tools like cssnano or clean-css
   - Reduces file size

3. **Minify JavaScript:**
   - Use tools like UglifyJS or Terser
   - Reduces file size

4. **Enable Compression:**
   - Configure web server (nginx/Apache)
   - Enable gzip compression

5. **Set Cache Headers:**
   - Configure long cache times
   - Use versioning for cache busting

## 📚 Adding New Styles

### To add a new page-specific stylesheet:

1. Create file in `static/css/`:
   ```bash
   static/css/newpage.css
   ```

2. Add styles:
   ```css
   /* New Page Specific Styles */
   .newpage-class {
       /* styles */
   }
   ```

3. Include in template:
   ```django
   {% block extra_css %}
   <link rel="stylesheet" href="{% static 'css/newpage.css' %}">
   {% endblock %}
   ```

### To add a new JavaScript file:

1. Create file in `static/js/`:
   ```bash
   static/js/newpage.js
   ```

2. Add functions:
   ```javascript
   // New Page Functionality
   function newFunction() {
       // code
   }
   ```

3. Include in template:
   ```django
   {% block extra_js %}
   <script src="{% static 'js/newpage.js' %}"></script>
   {% endblock %}
   ```

## 🐛 Troubleshooting

### Styles not loading?
1. Check if `{% load static %}` is at top of template
2. Run `python manage.py collectstatic`
3. Clear browser cache
4. Check file path is correct

### JavaScript not working?
1. Check browser console for errors
2. Verify file is loaded (Network tab)
3. Check function names are correct
4. Ensure jQuery is loaded if needed

### Changes not appearing?
1. Hard refresh browser (Ctrl+F5)
2. Clear browser cache
3. Restart Django server
4. Check if file is saved

## ✅ Best Practices

1. **Keep styles organized** - Group related styles together
2. **Use meaningful class names** - Descriptive and clear
3. **Avoid inline styles** - Use classes instead
4. **Comment your code** - Explain complex sections
5. **Test responsiveness** - Check on different screen sizes
6. **Validate CSS** - Use W3C CSS Validator
7. **Optimize images** - Compress before using
8. **Use relative units** - rem, em instead of px when appropriate

---

**This organization makes the codebase clean, maintainable, and scalable!** 🎨✨
