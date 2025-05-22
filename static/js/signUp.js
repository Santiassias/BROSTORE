$(document).ready(function () {
  $('#signupForm').on('submit', function (e) {
    e.preventDefault();

    $.ajax({
      url: '/signUp',
      type: 'POST',
      data: {
        inputName: $('#inputName').val(),
        inputEmail: $('#inputEmail').val(),
        inputPassword: $('#inputPassword').val()
      },
      success: function (response) {
        $('#msg').removeClass().addClass('alert alert-success').html(response.message || "¡Registro exitoso!").show();
      },
      error: function (xhr) {
        const error = xhr.responseJSON?.error || "Error desconocido.";
        $('#msg').removeClass().addClass('alert alert-danger').html(error).show();
      }
    });
  });
});

