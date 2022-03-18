

   // to check whether email registered or not
   $(document).on('submit', '#checkEmailForm', function(e) {

    e.preventDefault();
    var email_entered = $('#email_entered').val();

    $.ajax({
      type: 'POST',
      url: 'http://kudos02.pythonanywhere.com/check-email/',
      data: {
        'email_entered': email_entered,
        csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val(),
      },
      success:function(response) {
        console.log(response.status);
        $('#email_message').text(response.status)
        if(response.status == "email not registered"){
          document.getElementById("email").value = email_entered;
          document.getElementById("checkEmailForm").style.display = "none";
          document.getElementById("registerForm").style.display = "block";
          document.getElementById("askPasswordForm").style.display = "block";
          document.getElementById("askNameForm").style.display = "none";
        }
        else{
          document.getElementById("login_email").value = email_entered;
          document.getElementById("checkEmailForm").style.display = "none";  
          document.getElementById("loginForm").style.display = "block";
      }
      }
    })
  })

  // to check whether username available or not
  $(document).on('submit', '#registerForm', function(e) {
    console.log("inside username verification function");
    e.preventDefault();
    var username_entered = $('#username_entered').val();
    var password_1 = $('#password_1').val();
    var password_2 = $('#password_2').val();
    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var email = $('#email').val();

    $.ajax({
      type: 'POST',
      url: 'http://kudos02.pythonanywhere.com/check-username/',
      data: {
        'username': username_entered,
        'password1': password_1,
        'password2': password_2,
        'first_name': first_name, 
        'last_name': last_name,
        'email': email,
        csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val(),
      },
      success:function(response) {
        console.log(response.status);
        $('#username_message').text(response.status)
        if(response.status == "username registered"){
          document.getElementById("username_message").innerHTML = "username already taken";
          document.getElementById("entered_username").value = "";
        }
        else{
          window.location = "http://kudos02.pythonanywhere.com/view-profile/"
        }
      }
    })
  })

  // to check whether password and confirm password matches or not
  function verifyPassword(){
    let pswd_1 = document.getElementById("password_1").value ;
    let pswd_2 = document.getElementById("password_2").value ;
    if(pswd_1 === pswd_2 && pswd_1.length >=8 ){
  
      document.getElementById("askPasswordForm").style.display = "none";
      document.getElementById("askNameForm").style.display = "block";
    }
    else{
      document.getElementById("password_matching_validation").innerHTML = "password not matched or length should of atleast 8 characters";
    }
  }

  // login with authentication
  $(document).on('submit', '#loginForm', function(e) {
  console.log("inside login function")
  e.preventDefault();
  var login_email = $('#login_email').val();
  var login_password = $('#password').val();
  console.log(login_email)
  console.log(login_password)

  $.ajax({
      type: 'POST',
      url: 'http://kudos02.pythonanywhere.com/login/',
      data: {
        'login_email': login_email,
        'login_password': login_password,
        csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val(),
      },
      success:function(response) {
        console.log(response.status);
        $('#login_validation').text(response.status)
        if(response.status == 'User Login Success'){
            document.getElementById("checkEmailForm").style.display = "none";
            $('#login_validation').text(response.status)
            window.location = 'http://kudos02.pythonanywhere.com/view-profile/'
        } 
        else{
            $('#login_validation').text(response.status)
        }
      }
    })
  })
  
