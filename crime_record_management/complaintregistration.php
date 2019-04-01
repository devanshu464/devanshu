<!DOCTYPE html>
<html>
<center>
<style>
body{
	background-color:green;
}
form{border:solid;
     border-color:blue;
      width:300px;
     background-color:orange;
	 padding:100px 100px 100px 100px;
	 height:300px;
	 }
</style>
<body>
 <font color="red"><h1>Welcome To Crime Management System</h1></font>
 <font color="blue"><h2>Complaint Registration:</h2></font>
<form action="compregcon.php" method="post">
name:<input type="text" name="name"><br><br>
city:<input type="text" name="city"><br><br>
contactno:<input type="number" name="contactno"><br><br>
crimetype:<input type="text" name="crimetype"><br><br>
address:<input type="address" name="address"><br><br>
gender:<input type="radio" name="gender" value="male">male
		<input type="radio" name="gender" value="female">female
		<input type="radio" name="gender" value="other">other<br><br>
       <input type="submit" name="submit" value="submit">
	   </form>
	   </body>
	   </html>
