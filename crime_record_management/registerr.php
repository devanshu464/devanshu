<?php

// Grab User submitted information
$user = $_POST["username"];
$pass = $_POST["password"];

// Connect to the database
$con = mysql_connect("localhost","root","");
// Make sure we connected successfully
if(! $con)
{
    die('Connection Failed'.mysql_error());
}

// Select the database to use
mysql_select_db("crimedb",$con);

$result = mysql_query("SELECT username, password FROM data WHERE username = $user");

$row = mysql_fetch_array($result);

if($row["username"]==$user && $row["password"]==$pass)
    echo"You are a validated user.";
else
    echo"Sorry, your credentials are not valid, Please try again.";
?>