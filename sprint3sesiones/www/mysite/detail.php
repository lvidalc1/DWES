
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
if (!isset($_GET['id'])) {
die('No se ha especificado un libro');
}
$id = $_GET['id'];
$query = 'SELECT * FROM tLibros WHERE id='.$id;
$result = mysqli_query($db, $query) or die('Query error');
$only_row = mysqli_fetch_array($result);
echo '<h1>'.$only_row['nombre'].'</h1>';
echo '<h2>'.$only_row['año_publicacion'].'</h2>';
echo '<img src="' . $only_row['url_imagen'] . '"/>'
?>
<h3>Comentarios :</h3>
<ul>
<?php
$query2 = 'SELECT * FROM tComentarios WHERE libro_id='.$id;
$result2 = mysqli_query($db, $query2) or die('Query error');
while ($comentario = mysqli_fetch_array($result2)) {
    echo '<li>' . $comentario['comentario'] . '</li>';
    echo '<p>Fecha del comentario: ';
    echo $comentario['fecha'].'</p>';
  }
?>
</ul>

<p>Deja un nuevo comentario:</p>
<form action="/comment.php" method="post">
<textarea rows="4" cols="50" name="new_comment"></textarea><br>
<input type="hidden" name="id" value="<?php echo $id; ?>">
<input type="submit" value="Comentar">
</form>
<?php
//mostrar el enlace de logout si el usuario está logueado
if (isset($_SESSION['id'])) {  // verificar si el usuario está logueado
    echo '<p><a href="logout.php">Cerrar sesión</a></p>';
} else {
    echo '<p><a href="login.php">Iniciar sesión</a></p>';
}
mysqli_close($db);
?>

</body>
</html>
