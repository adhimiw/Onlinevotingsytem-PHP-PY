<?php
// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if the AADHAR ID parameter is provided
    if (isset($_POST["aadhar"])) {
        // Get the AADHAR ID from the request
        $aadhar = $_POST["aadhar"];

        // Connect to the database (replace with your database credentials)
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "voting_system";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Prepare a SQL statement to delete the voter data based on AADHAR ID
        $sql = "DELETE FROM voters WHERE aadhar = '$aadhar'";

        // Execute the SQL statement
        if ($conn->query($sql) === TRUE) {
            echo "Voter data deleted successfully";
        } else {
            echo "Error deleting voter data: " . $conn->error;
        }

        // Close the database connection
        $conn->close();
    } else {
        // AADHAR ID parameter not provided
        echo "AADHAR ID parameter is missing";
    }
} else {
    // Invalid request method
    echo "Invalid request method";
}
?>
