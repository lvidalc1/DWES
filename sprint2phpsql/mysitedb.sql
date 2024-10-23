-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `libro_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `libro_id` (`libro_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`libro_id`) REFERENCES `tLibros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
INSERT INTO `tComentarios` VALUES
(1,'Una historia apasionante que me ha tenido enganchado y fascinado de principio a fin.',3,1),
(2,'El Quijote es una obra maestra de la literatura española. Su lectura resulta muy satisfactoria gracias a sus capítulos cortos y su humor.',1,2),
(3,'Interesante visión de la mente humana cuando escapa de nuestra concepción de cordura.',5,3),
(4,'Libro entretenido y con un humor muy particular.',2,4),
(5,'Es una lectura fácil, amena y adictiva. Crea misterio desde las primeras páginas y la tensión va en aumento durante toda la obra',4,5);
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tLibros`
--

DROP TABLE IF EXISTS `tLibros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tLibros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(2000) DEFAULT NULL,
  `nombreAutor` varchar(60) DEFAULT NULL,
  `año_publicacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tLibros`
--

LOCK TABLES `tLibros` WRITE;
/*!40000 ALTER TABLE `tLibros` DISABLE KEYS */;
INSERT INTO `tLibros` VALUES
(1,'La sombra del viento','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.planetadelibros.com%2Flibro-la-sombra-del-viento%2F221322&psig=AOvVaw0Th43Ad7LBF0ZT6pp9ptfA&ust=1729765721260000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKDXnc2lpIkDFQAAAAAdAAAAABAE','Carlos Ruiz Zafón',2001),
(2,'Don Quijote de la Mancha','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.es%2FQuijote-Mancha-c%25C3%25B3mic-Austral-C%25C3%25B3mic%2Fdp%2F8408270885&psig=AOvVaw2yb34yl9KMGuHr3CA7b0SX&ust=1729765938512000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOib67SmpIkDFQAAAAAdAAAAABAE','Miguel de Cervantes Saavedra',1605),
(3,'Los renglones torcidos de Dios','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.planetadelibros.com%2Flibro-los-renglones-torcidos-de-dios%2F349885&psig=AOvVaw25xshiVXBYNvh1eo7jzVQH&ust=1729766038433000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiOhuWmpIkDFQAAAAAdAAAAABAE','Torcuato Luca de Tena',1979),
(4,'La conjura de los necios','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.anagrama-ed.es%2Flibro%2Fcompactos%2Fla-conjura-de-los-necios%2F9788433920423%2FCM_38&psig=AOvVaw2O629dC-L_Vh8LwO_f5JIK&ust=1729766149421000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjv75ynpIkDFQAAAAAdAAAAABAE','John Kennedy Toole',1980),
(5,'Diez negritos','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.casadellibro.com%2Flibro-diez-negritos%2F9788467045390%2F2575570&psig=AOvVaw2QoTJqBxZ-H39R8-FJ9SIv&ust=1729766367898000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPjj94GopIkDFQAAAAAdAAAAABAE','Agatha Christie',1939),
(6,'La sombra del viento','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.planetadelibros.com%2Flibro-la-sombra-del-viento%2F221322&psig=AOvVaw0Th43Ad7LBF0ZT6pp9ptfA&ust=1729765721260000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKDXnc2lpIkDFQAAAAAdAAAAABAE','Carlos Ruiz Zafón',2001),
(7,'Don Quijote de la Mancha','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.es%2FQuijote-Mancha-c%25C3%25B3mic-Austral-C%25C3%25B3mic%2Fdp%2F8408270885&psig=AOvVaw2yb34yl9KMGuHr3CA7b0SX&ust=1729765938512000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOib67SmpIkDFQAAAAAdAAAAABAE','Miguel de Cervantes Saavedra',1605),
(8,'Los renglones torcidos de Dios','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.planetadelibros.com%2Flibro-los-renglones-torcidos-de-dios%2F349885&psig=AOvVaw25xshiVXBYNvh1eo7jzVQH&ust=1729766038433000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiOhuWmpIkDFQAAAAAdAAAAABAE','Torcuato Luca de Tena',1979),
(9,'La conjura de los necios','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.anagrama-ed.es%2Flibro%2Fcompactos%2Fla-conjura-de-los-necios%2F9788433920423%2FCM_38&psig=AOvVaw2O629dC-L_Vh8LwO_f5JIK&ust=1729766149421000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjv75ynpIkDFQAAAAAdAAAAABAE','John Kennedy Toole',1980),
(10,'Diez negritos','https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.casadellibro.com%2Flibro-diez-negritos%2F9788467045390%2F2575570&psig=AOvVaw2QoTJqBxZ-H39R8-FJ9SIv&ust=1729766367898000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPjj94GopIkDFQAAAAAdAAAAABAE','Agatha Christie',1939);
/*!40000 ALTER TABLE `tLibros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
INSERT INTO `tUsuarios` VALUES
(1,'Pablo','Pérez López','pablopl@gmail.com','pabloPablito'),
(2,'Antonio','López López','antonioll@gmail.com','antoñito24'),
(3,'Sara','Fernández Castro','sarafc@gmail.com','sara123'),
(4,'Juan','Hernández Hernández','juanhh@gmail.com','juan678hernandez'),
(5,'María','López Gómez','marialg@gmail.com','mariaa22');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-23 14:06:49
