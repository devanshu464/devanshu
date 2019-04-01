 <style>
 body{
	 background-color:cyan;
 }</style>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "crimedb";
 
$conn = new mysqli($servername, $username, $password, $dbname);
 
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 


       $a=$_POST['username'];
$b=$_POST['email'];
$c=$_POST['city'];
$d=$_POST['state'];
$e=$_POST['phone_no'];
$f=$_POST['password'];

 
        $sql = "INSERT INTO data ( username,email,city,state,phone_no,password)           
VALUES (  '$a','$b','$c','$d','$e','$f' )";

if ($conn->query($sql) === TRUE) {
    echo "
<h3>Thanks for registration<br>";
echo "<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
echo "entered data successfully<br><br>";
echo "Your entered data is:<br><br>";
echo "Username:$a<br>";
echo "Email:$b<br>";
echo "City:$c<br>";
echo "State:$d<br>";
echo "Phone_no:$e<br>";
echo "Password:$f<br>";
$conn->close();
?>
