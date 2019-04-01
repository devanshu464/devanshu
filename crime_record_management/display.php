<?php
 
$link = mysqli_connect("localhost", "root", "", "crimedb");
 
 if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
 $sql = "SELECT * FROM data";
if($result = mysqli_query($link, $sql)){
    if(mysqli_num_rows($result) > 0){
        echo "<table>";
            echo "<tr>";
                echo "<th>sno</th>";
                echo "<th>username</th>";
               
            echo "</tr>";
        while($row = mysqli_fetch_array($result)){
            echo "<tr>";
                echo "<td>" . $row['sno'] . "</td>";
                echo "<td>" . $row['username'] . "</td>";
                 
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