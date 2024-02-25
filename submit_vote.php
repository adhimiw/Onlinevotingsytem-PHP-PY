<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "voting_system";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["candidate"])) {
    $selected_candidate = $_POST["candidate"];

    // Update the votes for the selected candidate in the database
    $sql = "UPDATE candidates SET votes = votes + 1 WHERE name = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $selected_candidate);
    
    if ($stmt->execute()) {
        echo "Vote recorded successfully!";
    } else {
        echo "Error recording vote: " . $conn->error;
    }

    $stmt->close();
}

$conn->close();
?>
