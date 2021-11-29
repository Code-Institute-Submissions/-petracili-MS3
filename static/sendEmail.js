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
            $('.modal').modal('open');
        },
        function(error){
             console.log("FAILED", error);
        });

    return false;
}

          
