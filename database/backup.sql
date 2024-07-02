-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: pos
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('14f7a031e901');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brands`
--

DROP TABLE IF EXISTS `brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brands` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brands`
--

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;
INSERT INTO `brands` VALUES (4,'ALPURA'),(7,'BARCEL'),(2,'BIMBO'),(1,'COCA-COLA'),(18,'COLGATE'),(15,'DANONE'),(8,'GAMESA'),(12,'HERDEZ'),(20,'JOHNSON & JOHNSON'),(5,'JUMEX'),(16,'KELLOGG\'S'),(11,'KNORR'),(13,'LA COSTEÑA'),(3,'LALA'),(14,'NESTLÉ'),(19,'P&G'),(10,'PEPSI'),(9,'SABRITAS'),(17,'UNILEVER'),(6,'ZWAN');
/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (8,'ABARROTES'),(5,'BEBIDAS'),(4,'CARNES'),(7,'DULCES'),(1,'FRUTAS'),(10,'HIGIENE'),(3,'LÁCTEOS'),(9,'LIMPIEZA'),(6,'PAN'),(2,'VERDURAS');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `customers_chk_1` CHECK ((`age` >= 18))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `unit_id` int NOT NULL,
  `category_id` int NOT NULL,
  `brand_id` int NOT NULL,
  `quantity` int NOT NULL,
  `cost_price` decimal(10,2) NOT NULL,
  `selling_price` decimal(10,2) NOT NULL,
  `reorder_level` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brand_id` (`brand_id`),
  KEY `category_id` (`category_id`),
  KEY `unit_id` (`unit_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`),
  CONSTRAINT `products_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `products_ibfk_3` FOREIGN KEY (`unit_id`) REFERENCES `units` (`id`),
  CONSTRAINT `products_chk_1` CHECK ((`cost_price` >= 0)),
  CONSTRAINT `products_chk_2` CHECK ((`quantity` >= 0)),
  CONSTRAINT `products_chk_3` CHECK ((`reorder_level` >= 0)),
  CONSTRAINT `products_chk_4` CHECK ((`selling_price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,2,1,20,21,57.00,97.00,6),(2,3,7,2,4,9.00,12.00,7),(3,5,9,14,13,42.00,67.00,4),(4,6,10,18,0,94.00,75.00,5),(5,6,3,10,0,43.00,5.00,4),(6,1,6,12,4,84.00,85.00,10),(7,4,7,9,30,51.00,52.00,5),(8,5,6,13,11,28.00,8.00,9),(9,1,9,17,23,65.00,70.00,8),(10,3,3,2,6,81.00,68.00,5),(11,1,9,2,7,98.00,24.00,8),(12,1,9,11,30,92.00,62.00,2),(13,5,4,17,19,7.00,10.00,2),(14,6,9,1,0,95.00,10.00,6),(15,1,7,10,5,38.00,17.00,8),(16,6,6,20,0,39.00,83.00,6),(17,2,2,15,25,2.00,42.00,9),(18,4,4,10,2,72.00,6.00,4),(19,4,3,12,20,83.00,44.00,9),(20,5,5,1,7,47.00,26.00,2),(21,2,4,2,20,7.00,44.00,7),(22,5,8,18,10,28.00,23.00,3),(23,2,3,20,20,1.00,58.00,6),(24,6,2,14,0,10.00,33.00,9),(25,3,9,2,27,85.00,31.00,6),(26,1,8,4,9,36.00,58.00,9),(27,1,2,7,24,35.00,44.00,9),(28,6,6,13,1,9.00,45.00,10),(29,3,2,5,2,74.00,3.00,1),(30,3,3,2,21,32.00,95.00,1),(31,5,2,11,4,69.00,78.00,5),(32,4,9,12,2,39.00,91.00,5),(33,4,3,5,10,75.00,100.00,6),(34,6,3,7,22,89.00,16.00,4),(35,6,7,2,14,39.00,45.00,4),(36,3,2,11,14,12.00,73.00,7),(37,3,7,12,23,70.00,44.00,6),(38,5,7,1,28,56.00,35.00,4),(39,5,1,19,28,14.00,17.00,1),(40,3,5,19,13,39.00,37.00,9),(41,3,2,6,12,22.00,49.00,2),(42,6,9,7,11,27.00,13.00,8),(43,1,9,8,25,28.00,90.00,1),(44,3,6,1,6,57.00,30.00,5),(45,1,2,4,24,99.00,79.00,2),(46,4,1,16,30,45.00,39.00,9),(47,5,6,19,5,31.00,4.00,8),(48,5,10,13,30,57.00,66.00,5),(49,6,9,4,18,18.00,94.00,6),(50,6,8,5,6,72.00,95.00,7),(51,6,1,14,8,90.00,61.00,3),(52,4,4,15,3,76.00,55.00,6),(53,1,7,17,24,7.00,9.00,1),(54,6,7,17,14,59.00,22.00,3),(55,5,1,8,3,93.00,27.00,7),(56,6,1,4,30,24.00,52.00,8),(57,4,7,19,26,68.00,13.00,2),(58,5,5,18,26,27.00,23.00,3),(59,4,1,7,27,100.00,12.00,2),(60,2,1,10,9,89.00,63.00,4),(61,2,4,16,18,99.00,91.00,5),(62,6,2,2,25,81.00,72.00,9),(63,2,5,1,13,80.00,25.00,2),(64,1,1,1,13,45.00,19.00,9),(65,5,8,3,6,95.00,22.00,1),(66,2,6,12,30,14.00,33.00,4),(67,5,6,19,8,26.00,45.00,6),(68,3,5,4,11,56.00,71.00,8),(69,3,6,12,16,54.00,28.00,7),(70,6,6,18,8,56.00,57.00,8),(71,1,2,19,7,45.00,13.00,8),(72,6,6,3,25,63.00,22.00,4),(73,4,4,10,15,69.00,71.00,2),(74,5,1,15,22,44.00,5.00,7),(75,2,6,20,26,99.00,13.00,1),(76,3,10,10,30,47.00,36.00,4),(77,3,2,2,14,31.00,67.00,3),(78,1,7,17,19,80.00,81.00,10),(79,1,10,19,5,100.00,9.00,9),(80,4,9,16,22,68.00,98.00,1),(81,6,4,1,14,94.00,19.00,4),(82,6,8,19,11,30.00,91.00,3),(83,1,9,8,6,65.00,67.00,3),(84,2,10,18,26,81.00,79.00,4),(85,3,6,19,29,94.00,42.00,4),(86,2,3,1,5,95.00,97.00,1),(87,3,9,15,28,9.00,10.00,8),(88,1,3,17,23,93.00,25.00,6),(89,1,1,18,19,28.00,54.00,10),(90,4,9,3,30,91.00,82.00,7),(91,2,1,1,25,43.00,89.00,3),(92,1,8,2,1,66.00,8.00,2),(93,2,8,18,24,30.00,21.00,2),(94,3,8,12,28,2.00,82.00,3),(95,6,1,4,10,1.00,88.00,4),(96,5,3,6,16,16.00,47.00,10),(97,3,7,19,21,58.00,31.00,10),(98,6,4,14,30,33.00,46.00,4),(99,1,2,9,28,16.00,74.00,8),(100,6,8,6,25,57.00,24.00,9),(101,2,5,2,3,123.12,1145.21,3),(102,6,4,4,4,11.00,15.12,4),(103,6,4,4,1,1.00,1.00,1);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_details`
--

DROP TABLE IF EXISTS `purchase_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_details` (
  `purchase_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `unit_purchase_price` decimal(10,2) NOT NULL,
  `total_unit_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`purchase_id`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `purchase_details_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `purchase_details_ibfk_2` FOREIGN KEY (`purchase_id`) REFERENCES `purchases` (`id`),
  CONSTRAINT `purchase_details_chk_1` CHECK ((`quantity` > 0)),
  CONSTRAINT `purchase_details_chk_2` CHECK ((`total_unit_price` >= 0)),
  CONSTRAINT `purchase_details_chk_3` CHECK ((`unit_purchase_price` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_details`
--

LOCK TABLES `purchase_details` WRITE;
/*!40000 ALTER TABLE `purchase_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchase_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `supplier_id` int NOT NULL,
  `date` date NOT NULL,
  `total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `supplier_id` (`supplier_id`),
  CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`),
  CONSTRAINT `purchases_chk_1` CHECK ((`total` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_details`
--

DROP TABLE IF EXISTS `sale_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale_details` (
  `sale_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `unit_sale_price` decimal(10,2) NOT NULL,
  `total_unit_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`sale_id`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `sale_details_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `sale_details_ibfk_2` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`id`),
  CONSTRAINT `sale_details_chk_1` CHECK ((`quantity` > 0)),
  CONSTRAINT `sale_details_chk_2` CHECK ((`total_unit_price` >= 0)),
  CONSTRAINT `sale_details_chk_3` CHECK ((`unit_sale_price` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_details`
--

LOCK TABLES `sale_details` WRITE;
/*!40000 ALTER TABLE `sale_details` DISABLE KEYS */;
INSERT INTO `sale_details` VALUES (1,4,1,75.00,75.00),(1,5,1,5.00,5.00),(2,4,12,75.00,900.00),(2,5,2,5.00,10.00),(3,4,2,75.00,150.00),(3,5,10,5.00,50.00),(4,4,14,75.00,1050.00),(4,14,19,10.00,190.00),(5,20,7,26.00,182.00),(5,81,14,19.00,266.00),(7,4,1,75.00,75.00),(9,5,1,5.00,5.00),(10,16,12,83.00,996.00),(11,24,3,33.00,99.00),(12,24,12,33.00,396.00),(13,28,4,45.00,180.00),(14,28,1,45.00,45.00),(15,28,1,45.00,45.00),(16,34,1,16.00,16.00),(17,34,1,16.00,16.00),(18,35,1,45.00,45.00),(19,34,2,16.00,32.00),(19,42,2,13.00,26.00);
/*!40000 ALTER TABLE `sale_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `date` date NOT NULL,
  `total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `sales_chk_1` CHECK ((`total` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,NULL,'2024-07-02',80.00),(2,NULL,'2024-07-02',910.00),(3,NULL,'2024-07-02',200.00),(4,NULL,'2024-07-02',1240.00),(5,NULL,'2024-07-02',448.00),(6,NULL,'2024-07-02',0.00),(7,NULL,'2024-07-02',75.00),(8,NULL,'2024-07-02',75.00),(9,NULL,'2024-07-02',5.00),(10,NULL,'2024-07-02',996.00),(11,NULL,'2024-07-02',99.00),(12,NULL,'2024-07-02',396.00),(13,NULL,'2024-07-02',180.00),(14,NULL,'2024-07-02',45.00),(15,NULL,'2024-07-02',45.00),(16,NULL,'2024-07-02',16.00),(17,NULL,'2024-07-02',16.00),(18,NULL,'2024-07-02',45.00),(19,NULL,'2024-07-02',58.00);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` char(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'La Costeña','Calle 1, Colonia 2, Ciudad 3, Estado 4','1233567890','lacostena@example.com'),(2,'Bimbo','Calle 5, Colonia 6, Ciudad 7, Estado 8','0987854321','bimbo@example.com'),(3,'Sabritas','Calle 9, Colonia 10, Ciudad 11, Estado 12','9876543217','sabritas@example.com'),(4,'Coca-Cola','Calle 13, Colonia 14, Ciudad 15, Estado 16','0123456788','cocacola@example.com'),(5,'Pepsi','Calle 17, Colonia 18, Ciudad 19, Estado 20','9976543211','pepsi@example.com'),(6,'Nestlé','Calle 21, Colonia 22, Ciudad 23, Estado 24','0123456889','nestle@example.com'),(7,'Kellogg\'s','Calle 25, Colonia 26, Ciudad 27, Estado 28','9876543212','kelloggs@example.com'),(8,'Lala','Calle 29, Colonia 30, Ciudad 31, Estado 32','0123456789','lala@example.com'),(9,'Gamesa','Calle 33, Colonia 34, Ciudad 35, Estado 36','9876543210','gamesa@example.com'),(10,'Barcel','Calle 37, Colonia 38, Ciudad 39, Estado 40','0723456789','barcel@example.com');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `units` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
INSERT INTO `units` VALUES (6,'BOLSA'),(5,'CAJA'),(1,'KILOGRAMO'),(2,'LITRO'),(4,'METRO'),(3,'PIEZA');
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-02 11:22:17
