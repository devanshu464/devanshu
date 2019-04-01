<?php
   include('session.php');
?> 
<!DOCTYPE html>
<html>
<head>
<style>
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    background-color: #111;
}

.active {
    background-color: #4CAF50;
}
p{
	background-color:yellow;
}
body{
	background-color:cyan;
}
</style>
</head>
<body>User <?php

                echo  $login_session ;
				echo  $s ;
?>               

<ul>
<li> <a class="active" href="homepage.php">Home</li></a>
<li> <a href="complaintregistration.php">complaint registration</li></a>
<li> <a href="complaintstatus.php">complaint status</li></a>
<li> <a href="criminalrecord.php">criminal record</li></a>
<li> <a href="emergencycontact.php">Emergency Contact number</li></a>
<li> <a href="aboutus.php">About Us</li></a>
</ul>
<div>
<article>
<font color="blue"><h2>Today's Headlines:</h2></font>
 <font color="green"><h3>Cricket conflict:</h3></font>
<p> Separately Mr Modi has also questioned the right of the Board of Control for Cricket in India (BCCI) - which also runs the IPL- to convene a meeting on Monday where, according to reports, a number of a members may ask him to step down.
But there have been questions about the impartiality of the board.
India's Sports Minister MS Gill said there was a question of conflict of interest for certain people who have interests in both the BCCI and the IPL: one selector is a brand ambassador for an IPL team, while another board member owns an IPL team
. "You can't be regulator, controller, owner of the team you are creating," Mr Gill said.
He said the government was giving tax concessions to the IPL and providing security for the matches. "You have to charge from people benefiting commercially," he said. The allegations were sparked off by a row between the IPL commissioner, Lalit Modi, and a government minister, Shashi Tharoor, over the ownership of a new IPL franchise.
Mr Tharoor was forced to resign after Mr Modi revealed that a close female friend of the minister was one of the stakeholders of the team for Kochi Mr Tharoor helped to set up. 
Mr Tharoor denies any wrongdoing. The IPL has become a multi-billion dollar industry, which attracts some of India's wealthiest businessmen and women. </p>
</article>
<img src="lalitmodi.jpg"width="500"height="400">
</div>

</body>
</html><form method="post" action="update.php">
<input type="submit" name="submit" value=delete>
</form>
<form method="post" action="rename.php">
<input type="submit" name="submit" value=up>