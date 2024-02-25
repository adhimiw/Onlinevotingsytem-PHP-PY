<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "voting_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare data for insertion (sanitize to prevent SQL injection)
$aadhar = mysqli_real_escape_string($conn, $_POST['aadhar']);
$name = mysqli_real_escape_string($conn, $_POST['name']);
$birth_date = mysqli_real_escape_string($conn, $_POST['birth_date']);

// Attempt insert query execution
$sql = "INSERT INTO voters (aadhar, name, birth_date) VALUES ('$aadhar', '$name', '$birth_date')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
