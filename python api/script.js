document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;
    // यहाँ आप कोड को भेजने का कोड जोड़ सकते हैं, जैसे AJAX अनुरोध या ईमेल भेजना
    console.log("नाम: " + name + "\nईमेल: " + email + "\nसंदेश: " + message);
});
