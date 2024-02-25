<?php
// Retrieve voter information from POST request
$aadhar = $_POST['aadhar'];
$name = $_POST['name'];
$birth_date = $_POST['birth_date'];

// Example: Replace with your own voter authentication logic
// Here, we simply check if the name is "adhi" and the birth date is "01-12-2004"
if ($name === 'adhi' && $birth_date === '01-12-2004') {
    // Voter is eligible
    http_response_code(200); // OK status code
} else {
    // Voter is not eligible
    http_response_code(403); // Forbidden status code
}
?>
