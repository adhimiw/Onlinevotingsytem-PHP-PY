<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vote Count</title>
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

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

// Retrieve updated vote list from the candidate table
$sql = "SELECT * FROM candidates";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<h3>Vote Count</h3>";
    echo "<table>";
    echo "<tr><th>Candidate</th><th>Votes</th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row['name'] . "</td><td>" . $row['votes'] . "</td></tr>";
    }
    echo "</table>";
} else {
    echo "No candidates available";
}

$conn->close();
?>

</body>
</html>
