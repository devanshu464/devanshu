<?php
   include("config.php");
   session_start();
   
   if($_SERVER["REQUEST_METHOD"] == "POST") {
       
      $myusername = mysqli_real_escape_string($db,$_POST['username']);
      $mypassword = mysqli_real_escape_string($db,$_POST['password']); 
      
      $sql = "SELECT sno FROM data WHERE username = '$myusername' and password = '$mypassword'";
      $result = mysqli_query($db,$sql);
      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
       
      $count = mysqli_num_rows($result);
      
 		
      if($count == 1) {
          $_SESSION['login_user'] = $myusername;
         
         header("location: homepage.php");
      }else {
         $error = "Your Login Name or Password is invalid";
      }
   }
?><html>
<center>
<style>
body{background-color:white;
	img-float:left;
	text-align:center;}
	
#img-left{
	float:left;
}
#img-right{
	float:right;
}
form{border:solid;
     border-color:red;
      width:100px;
     background-color:lightblue;
	 padding:100px 100px 100px 100px;
	 height:100px;
	 }
</style>
<body>
<h1 style="background-color:red;"><font color="blue">Welcome To Crime Management System</h1>
<div id="img-left">
<img src="indiaflag.png" width="300"height="200"> 
</div>
<div id="img-right">
 <img src="crimeb.png" width="300" height="200">
 </div>
   <font color="green"> <h1>Login</h1><br></font>          
               <form action = "" method = "post">
                  <label>UserName  :</label><input type = "text" name = "username" class = "box"/><br /><br />
                  <label>Password  :</label><input type = "password" name = "password" class = "box" /><br/><br />
                  <input type = "submit" value = " Submit "/><br />
               </form>
			   
			 <a href="register.php">new user?click here</a>
     