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

// Perform select query to get voter details
$sql = "SELECT * FROM voters";
$result = $conn->query($sql);

// Check if there are any rows returned
if ($result->num_rows > 0) {
    // Loop through each row and print voter details
    while ($row = $result->fetch_assoc()) {
        echo "AADHAR: " . $row["aadhar"] . "\n";
        echo "Name: " . $row["name"] . "\n";
        echo "Birth Date: " . $row["birth_date"] . "\n\n";
    }
} else {
    echo "No voters found";
}

// Close connection
$conn->close();
?>
