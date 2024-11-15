<?php
// Conexión a la base de datos
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb');
if (!$db) {
    die('Error de conexión: ' . mysqli_connect_error());
}

// Iniciar sesión
session_start();

// Obtener datos del formulario y validación básica
$email = isset($_POST['f_email']) ? trim($_POST['f_email']) : '';
$password = isset($_POST['f_password']) ? $_POST['f_password'] : '';
$password2 = isset($_POST['f_password2']) ? $_POST['f_password2'] : '';

// Verificar que las contraseñas coinciden
if ($password !== $password2) {
    die('Error: Las contraseñas no coinciden');
}

// Limpiar los datos de entrada para prevenir inyecciones SQL
$email = mysqli_real_escape_string($db, $email);

// Consultar si el correo está registrado en la base de datos
$query = "SELECT id, contraseña FROM tUsuarios WHERE email = '$email'";
$result = mysqli_query($db, $query);

if (mysqli_num_rows($result) == 0) {
    die('Error: Este correo NO está registrado');
}

// Obtener los datos del usuario
$row = mysqli_fetch_array($result);
$user_id = $row['id'];

// Cifrar la nueva contraseña
$password_hash = password_hash($password, PASSWORD_DEFAULT);

// Actualizar la contraseña en la base de datos
$update_query = "UPDATE tUsuarios SET contraseña = '$password_hash' WHERE email = '$email'";
$update_result = mysqli_query($db, $update_query);

// Verificar si la actualización fue exitosa
if ($update_result) {
    // Guardar el ID de usuario en la sesión
    $_SESSION['user_id'] = $user_id;
    header('Location: main.php');
    exit();
} else {
    die('Error: No se pudo completar el cambio de contraseña');
}

// Cerrar la conexión a la base de datos
mysqli_close($db);
?>
