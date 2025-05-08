// Toggle password visibility
const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');

togglePassword.addEventListener('click', function() {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});

// Form submission
const form = document.querySelector('.login-form');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    // Authentication logic would go here
    console.log('Form submitted');
});