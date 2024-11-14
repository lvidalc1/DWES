<?php
//inicia sesion
session_start();
//deestruye sesion
session_destroy();
//redirigimos a login
header('Location: login.html');
?>
