// formulario.js

document.getElementById('registrationForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que el formulario se envíe automáticamente

  var username = document.getElementById('username').value;
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;
  var confirmPassword = document.getElementById('confirm_password').value;
  var emailError = document.getElementById('emailError');
  var passwordError = document.getElementById('passwordError');
  var isValid = true;

  // Validar el formato del correo electrónico
  if (!email.includes('@')) {
    emailError.textContent = 'El correo electrónico debe contener "@"';
    isValid = false;
  } else {
    emailError.textContent = '';
  }

  // Validar que las contraseñas coincidan
  if (password !== confirmPassword) {
    passwordError.textContent = 'Las contraseñas no coinciden';
    isValid = false;
  } else {
    passwordError.textContent = '';
  }

  // Validaciones de seguridad para las contraseñas
  if (password.length < 8) {
    passwordError.textContent = 'La contraseña debe tener al menos 8 caracteres';
    isValid = false;
  } else if (password.length > 20) {
    passwordError.textContent = 'La contraseña no debe tener más de 20 caracteres';
    isValid = false;
  } else if (!/\d/.test(password)) {
    passwordError.textContent = 'La contraseña debe contener al menos un número';
    isValid = false;
  } else if (!/[a-zA-Z]/.test(password)) {
    passwordError.textContent = 'La contraseña debe contener al menos una letra';
    isValid = false;
  } else if (!/[!@#$%^&*]/.test(password)) {
    passwordError.textContent = 'La contraseña debe contener al menos un carácter especial (!@#$%^&*)';
    isValid = false;
  } else {
    passwordError.textContent = '';
  }

  // Si todo es válido, redirige al usuario a otra página (por ejemplo, "datos_ingresados.html")
  if (isValid) {
    // Construye la URL con los datos ingresados
    var url = 'datos_ingresados.html' + '?username=' + encodeURIComponent(username) + '&email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password);
    window.location.href = url; // Redirige al usuario
  }
});

