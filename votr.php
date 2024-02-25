<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Voting System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 400px;
            text-align: center;
        }
        h2 {
            color: #333;
            margin-bottom: 20px;
        }
        input[type="text"], input[type="submit"] {
            padding: 10px;
            font-size: 16px;
            width: 100%;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        .candidate {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .candidate input[type="radio"] {
            margin-right: 10px;
        }
        .candidate img {
            width: 50px;
            height: auto;
            border-radius: 50%;
            margin-right: 10px;
        }
        .error {
            color: #f00;
            margin-top: 10px;
        }
        .success {
            color: #0c0;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Online Voting System</h2>
        
        <?php
            session_start(); // Start the session

            // Database connection parameters
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

            // Reset session data on page load or refresh
            if(isset($_SESSION['aadhar_verified'])) {
                unset($_SESSION['aadhar_verified']);
            }

            // Reset last interaction time on page load or refresh
            $_SESSION['last_interaction'] = time();

            // Check if Aadhar number is submitted
            if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["aadhar"])) {
                $aadhar = $_POST["aadhar"];

                // Verify Aadhar number
                $stmt = $conn->prepare("SELECT * FROM voters WHERE aadhar = ?");
                $stmt->bind_param("s", $aadhar);
                $stmt->execute();
                $result = $stmt->get_result();

                if ($result->num_rows > 0) {
                    $row = $result->fetch_assoc();
                    if ($row['voted'] == 1) {
                        echo "<p class='error'>You have already voted.</p>";
                    } else {
                        $_SESSION['aadhar_verified'] = true;

                        // Get the selected candidate
                        if(isset($_POST["candidate"])) {
                            $selected_candidate = $_POST["candidate"];

                            // Update the vote count for the selected candidate
                            $stmt_update_candidate = $conn->prepare("UPDATE candidates SET votes = votes + 1 WHERE name = ?");
                            $stmt_update_candidate->bind_param("s", $selected_candidate);
                            $stmt_update_candidate->execute();
                            $stmt_update_candidate->close();

                            // Update voted column to 1
                            $stmt_update_voter = $conn->prepare("UPDATE voters SET voted = 1 WHERE aadhar = ?");
                            $stmt_update_voter->bind_param("s", $aadhar);
                            $stmt_update_voter->execute();
                            $stmt_update_voter->close();

                            // Display success message
                            echo "<p class='success'>Your vote for ".$selected_candidate." has been recorded successfully!</p>";
                        } else {
                            echo "<p class='error'>Please select a candidate to vote.</p>";
                        }
                    }
                } else {
                    echo "<p class='error'>Invalid Aadhar number.</p>";
                }
            } elseif (isset($_SESSION['aadhar_verified']) && $_SESSION['aadhar_verified']) {
                // Aadhar number already verified, display message
                echo "<p class='success'>Aadhar number already verified.</p>";
            } else {
                // Prompt the user to enter their Aadhar number
                echo "<form action='" . htmlspecialchars($_SERVER["PHP_SELF"]) . "' method='post'>";
                echo "<input type='text' id='aadhar' name='aadhar' placeholder='Enter Aadhar Number' required>";
                echo "<br>";

                // Fetch and display candidates dynamically using PHP
                $sql = "SELECT * FROM candidates";
                $result = $conn->query($sql);

                if ($result->num_rows > 0) {
                    echo "<div class='candidates'>";
                    while($row = $result->fetch_assoc()) {
                        echo "<div class='candidate'>";
                        echo "<input type='radio' name='candidate' value='" . $row['name'] . "' required>";
                        echo "<img src='images/" . strtolower(str_replace(" ", "_", $row['name'])) . ".jpg' alt='" . $row['name'] . "'>";
                        echo "<span>" . $row['name'] . "</span>";
                        echo "</div>";
                    }
                    echo "</div>";
                } else {
                    echo "<p class='error'>No candidates available.</p>";
                }

                echo "<input type='submit' value='Vote'>";
                echo "</form>";
            }
            ?>

        <!-- Display candidate details -->
        <div class="candidate-details">
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["candidate"])) {
                $selected_candidate = $_POST["candidate"];
                echo "<h3>Candidate Details</h3>";
                echo "<p>Name: " . $selected_candidate . "</p>";
                echo "<img src='images/" . strtolower(str_replace(" ", "_", $selected_candidate)) . ".jpg' alt='" . $selected_candidate . "'>";
            }
            ?>
        </div>
    </div>
</body>
</html>
            