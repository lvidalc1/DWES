<html>
<body>
<h1>Jubilación</h1>
<?php
function edad_en_3_años($edad) {
return $edad + 3;
}
function mensaje($age) {
if ((edad_en_3_años($age)-3)>65) {
return "Debería estar usted jubilado";
}else if ((edad_en_3_años($age)-3) == 65){
return "Este año se jubila";
}else if (edad_en_3_años($age) > 65) {
return "En ".(65 - (edad_en_3_años($age)-3))." años tendrás edad de jubilación";
} else {
return "¡Disfruta de tu tiempo!";
}
}
?>
<table>
<tr>
<th>Edad</th>
<th>Info</th>
</tr>
<?php
$lista = array(50,55,60,62,63,64,65,66,70);
foreach ($lista as $valor) {
echo "<tr>";
echo "<td>".$valor."</td>";
echo "<td>".mensaje($valor)."</td>";
echo "</tr>";
}
?>
</table>
</body>
</html>
