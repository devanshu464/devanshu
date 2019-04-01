<center>
<style>
body{background-color:pink;
      }	  
</style>
<body>
<font color="blue"><h1>Welcome To Crime Management System</h1></font>
<font color="green"><h2>List Of Most Wanted Criminals:</h2>
</body><?php
 
$link = mysqli_connect("localhost", "root", "", "crimedb");
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
 $sql = "SELECT * FROM criminalrecord";
if($result = mysqli_query($link, $sql)){
    if(mysqli_num_rows($result) > 0){
        echo "<table>";
            echo "<tr>";
                echo "<th>slno</th></th>";
                echo "<th>name</th></th>";
				echo "<th>reward</th>";
				echo "<th>crime</th>";
				
               
            echo "</tr>";
        while($row = mysqli_fetch_array($result)){
            echo "<tr>";
                echo "<td>". $row['slno'] . "</td></td>";
                echo "<td>" . $row['name'] . "</td></td>";
				echo "<td>" . $row['reward'] . "</td></td>";
				echo "<td>" . $row['crime'] . "</td></td>";
				
                 
            echo "</tr>";
        }
        echo "</table>";
        mysqli_free_result($result);
    } else{
        echo "No records matching your query were found.";
    }
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 
// Close connection
mysqli_close($link);
?>
