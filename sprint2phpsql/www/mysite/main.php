<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<head>
<h1>Libros</h1>
<style>
table{
width: 100%;
border-collapse: collapse;
}
table, th, td {
border: 1px solid black;
}
th, td {
padding: 8px;
text-align: left;
}
img{
width: 100px;
heigth: 100px;
}
</style>
</head>
<body>
<?php

// Lanzar una query
$queryLibros = 'SELECT * FROM tLibros';
$resultLibros = mysqli_query($db, $queryLibros) or die('Query error');
//crear tabla
echo '<table>';
echo '<tr><th>Id</th><th>Nombre</th><th>Imagen</th><th>Autor</th><th>Año de Publicacion</th>';

// Recorrer el resultado
while ($row = mysqli_fetch_array($resultLibros)) {
    echo '<tr>';
    echo '<td><a href="detail.php?id='. ($row['id']) . '">' .($row['nombre']) . '</a></td>';
    echo '<td>' . ($row['nombre']) . '</td>';
    echo '<td><img src=' . ($row['url_imagen']). '></td>';
    echo '<td>' . ($row['nombreAutor']) . '</td>';
    echo '<td>' . ($row['año_publicacion']) . '</td>'; 
    echo '</tr>';
}

mysqli_close($db);
?>
</body>
</html>
