  $(document).ready(function(){
    $('#loginButton').on('click', function(){
        console.log("adnadnsa fhsaflhsbfalshbfsahd");
        var userEmail = $('#userEmail').val();
        var userPassword = $('#userPassword').val();


        var userInformation ={
            'username' : userEmail,
            'password': userPassword
        }

        $.ajax({
            url : './login/login',
            type : 'POST',
            data : userInformation,
            success : function(data) {
                window.location = '/homepage'
            },
            error : function(error)
            {

            }
        });
    });
  });
