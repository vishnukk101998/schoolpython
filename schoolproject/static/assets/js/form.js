// Define a JavaScript function to update the Courses dropdown based on the selected Department
        function updateCoursesDropdown() {
            const departmentDropdown = document.getElementById("department");
            const coursesDropdown = document.getElementById("courses");

            // Define the courses options for each department
            const coursesOptions = {
                commerce: ["BBA", "BCom", "MBA"],
                science: ["BSc", "MSc", "PhD"],
                arts: ["BA", "MA", "MFA"],
                engineering: ["ECE", "EE", "CE","MECH","SAFETY"]
                // Add more departments and their courses as needed
            };

            // Get the selected department
            const selectedDepartment = departmentDropdown.value;

            // Clear the current options in the Courses dropdown
            coursesDropdown.innerHTML = '';

            // Populate the Courses dropdown with options based on the selected department
            coursesOptions[selectedDepartment].forEach(course => {
                const option = document.createElement("option");
                option.text = course;
                coursesDropdown.add(option);
            });
        }