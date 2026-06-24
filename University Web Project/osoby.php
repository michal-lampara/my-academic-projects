<?php

$connection = @new mysqli('localhost', 'root', '', 'formularz') 
    or die('Brak połączenia z serwerem MySQL');

$db = @mysqli_select_db($connection, 'formularz')
    or die('Nie mogę połączyć się z bazą danych');

$imie=$_POST['imie'];
$nazwisko=$_POST['nazwisko'];
$login=$_POST['login'];
$haslo=password_hash($_POST['haslo'], PASSWORD_DEFAULT);
$email=$_POST['email']; 
$kod_pocztowy=$_POST['kod_pocztowy'];
$ulica=$_POST['ulica'];
$miasto=$_POST['miasto'];

$zapytanie = "INSERT INTO dane (imie,nazwisko,login,haslo,email,kod_pocztowy,ulica,miasto) VALUES ('$imie', '$nazwisko', '$login', '$haslo', '$email', '$kod_pocztowy', '$ulica', '$miasto')"
    or die(mysqli_error());

$wynik = mysqli_query($connection, $zapytanie);

if ($wynik) {echo ('Prawidłowo dodano do bazy danych');}

mysqli_close($connection);

?>