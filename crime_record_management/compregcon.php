
 

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "crimedb";
 
$conn = new mysqli($servername, $username, $password, $dbname);
 
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 


       $a=$_POST['name'];
$b=$_POST['city'];
$c=$_POST['contactno'];
$d=$_POST['crimetype'];
$e=$_POST['address'];
$f=$_POST['gender'];

 
        $sql = "INSERT INTO compregcon( name,city,contactno,crimetype,address,gender)           
VALUES (  '$a','$b','$c','$d','$e','$f' )";

if ($conn->query($sql) === TRUE) {
    echo "
<h3>Thanks for registration";
echo "<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
echo "entered data successfully";
echo "Name:$a<br>";
echo "City:$b<br>";
echo "Contact No.:$c<br>";
echo "CrimeType:$d<br>";
echo "address$e<br>";
echo "Gender:$f<br>";
$conn->close();
?>
