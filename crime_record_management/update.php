<?php
   include('session.php');
   
?><?php
  
$servername = "localhost";
$u = "root";
$password = "";
$dbname = "crimedb";

// Create connection
$conn = new mysqli($servername, $u, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
 
 $sql = "DELETE  FROM data WHERE sno =    '$s'  ";

if ($conn->query($sql) === TRUE) {
    echo "Record deleted successfully";
} else {
    echo "Error deleting record: " . $conn->error;
}

$conn->close();
?>