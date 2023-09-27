function calculateAge() {
            const dobInput = document.getElementById("dob");
            const ageInput = document.getElementById("age");

            // Get the entered date of birth
            const dob = new Date(dobInput.value);

            // Calculate the age
            const today = new Date();
            const age = today.getFullYear() - dob.getFullYear();

            // Set the age value in the age input field
            ageInput.value = age;
        }