$(document).ready(function(){
  $('#submitButton').on('click', function(){
      var userName = $('#form1').val();
      var userEmail = $('#form2').val();
      var userPassword = $('#form3').val();
      var userStudentId = $('#form4').val();
      var userMajor = $('#form5').val();

      var userInformation ={
          'name' : userEmail,
          'password': userPassword,
          'studentId': userStudentId,
          'major': userMajor,
          'email': userEmail
      }

      $.ajax({
          url : './profile/update',
          type : 'POST',
          data : userInformation,
          success : function(data) {
              alert('Successsfully Updated in database.');
          },
          error : function(error)
          {
              alert("Failed to update in database.");
          }
      });
  });
});
