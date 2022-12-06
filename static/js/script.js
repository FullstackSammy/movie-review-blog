document.addEventListener("DOMContentLoaded", function () {

    const contactBtn = document.getElementById('contact-btn');

    contactBtn.addEventListener("click", () => {
        const email = document.getElementById("exampleFormControlInput1").value;
        let templateParams = {
            email: email,
        };
        //Only checks if both inputs have value
        if (email === "") {
            alert('Please type a username and email');
        } else {
            emailjs.send("service_ie8ap9o", "template_xcpz6ol", templateParams, "R6A6UlPYHLb2KXBMs").
            then(function () {
                alert('Email with score was sent!');
                document.getElementById("exampleFormControlInput1").value = "";
            }, function (error) {
                alert('FAILED...', error);
            });
        }
    });

















});