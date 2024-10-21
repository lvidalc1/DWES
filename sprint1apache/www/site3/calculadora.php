<html>
<body>
<h1>Calculadora</h1>
<p>Qué operación desea realizar?</p>
<?php
if ($_POST["fc1"]!= null){
	$v_unidad1 = $_POST["fc1"];
}else{
	$v_unidad1 = 0;
}
if ($_POST["fc2"] != null){
	$v_unidad2 = $_POST["fc2"];
}else{
	$v_unidad2 = 0;
}

switch ($_POST["tipoOp"]){
	case "suma":
		$v_resultado = $v_unidad1 + $v_unidad2;
		echo $v_unidad1." + ".$v_unidad2." = ".$v_resultado;
		break;
	case "resta":
                $v_resultado = $v_unidad1 - $v_unidad2;
                echo $v_unidad1." - ".$v_unidad2." = ".$v_resultado;
		break;
	case "multiplicacion":
                $v_resultado = $v_unidad1 * $v_unidad2;
                echo $v_unidad1." + ".$v_unidad2." = ".$v_resultado;
		break;
	case "division":
                $v_resultado = $v_unidad1 / $v_unidad2;
                echo $v_unidad1." / ".$v_unidad2." = ".$v_resultado;
		break;
}
?>
</p>
<p>Realice una operación:</p>
<form action"/calculadora.php" method="post">
        <label for="cantidad1">Cantidad 1:</label><br>
        <input type="text" id="cantidad1" name="fc1"><br>

        <label for="cantidad2">Cantidad 2:</label><br>
        <input type="text" id="cantidad2" name="fc2"><br>

        <select name="tipoOp">
        <option value="suma">Suma</option>
        <option value="resta">Resta</option>
        <option value="multiplicacion">Multiplicación</option>
        <option value="division">División</option>
        </select><br><br>
<input type="submit" value="Calcular">
</form>
</body>
</html>
