function enableSubmit() {
            const form = document.getElementById("myForm");
            const submitButton = document.getElementById("submitButton");

            // Check if the form is valid (all required fields are filled)
            if (form.checkValidity()) {
                submitButton.removeAttribute("disabled");
            } else {
                submitButton.setAttribute("disabled", "disabled");
            }
        }