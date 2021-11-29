function sendMail(contactForm) { 
    emailjs.send("service_4bl406b", "template_vm6mfpb", {
        "from_name" : contactForm.firstname.value,
        "from_lastname" : contactForm.lastname.value,
        "from_email" : contactForm.email.value,
        "message" : contactForm.message.value
    })
    .then(
        function(response){
            console.log("SUCCESS", response);
        },
        function(error){
             console.log("FAILED", error);
        });

    return false;
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal1');
    var instances = M.Modal.init(elems, options);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.modal1').modal();
  });
          
