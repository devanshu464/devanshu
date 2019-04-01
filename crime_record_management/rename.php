<html>
   
   <head>
    </head>
   <?php
   include('session.php');
   
?><?php

                echo  $login_session ;
				echo  $s ;
?>              

   <body>
      <?php
         if(isset($_POST['update'])) {
            $dbhost = 'localhost';
            $dbuser = 'root';
            $dbpass = '';
            
            $conn = mysql_connect($dbhost, $dbuser, $dbpass);
            
            if(! $conn ) {
               die('Could not connect: ' . mysql_error());
            }
            
              $username = $_POST['username'];
            $sql = "UPDATE data ". "SET username = '$username' ". 
               "WHERE sno = '$s'" ;
            mysql_select_db('crimedb');
            $retval = mysql_query( $sql, $conn );
            
            if(! $retval ) {
               die('Could not update data: ' . mysql_error());
            }
            echo "Updated data successfully\n";
            
            mysql_close($conn);
         }else {
            ?>
               <form method = "post" action = "<?php $_PHP_SELF ?>">
                  <table width = "400" border =" 0" cellspacing = "1" 
                     cellpadding = "2">
                  
                     <tr>
                        <td width = "100">username</td>
                        <td><input name = "username" type = "text" 
                           id = "username"></td>
                     </tr>
                  
                
                           <input name = "update" type = "submit" 
                              id = "update" value = "Update">
                        </td>
                     </tr>
                  
                  </table>
               </form>
            <?php
         }
      ?>
      
   </body>
</html>