-- MySQL dump 10.13  Distrib 8.4.7, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.4.7

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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(254) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(254) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test1','test@test.com','test',10,'2025-11-13 22:35:19'),(2,'allen','allen@test.com','allentest',100,'2025-11-14 22:35:19'),(3,'jack','jack@test.com','jacktest',9999,'2025-11-17 22:35:19'),(4,'edison','edison@test.com','edisontest',345,'2025-11-16 22:35:19'),(5,'morgan','morgan@test.com','morgantest',213,'2025-11-15 22:35:19'),(6,'test3','test3@test.com','test3',0,'2025-11-21 23:47:43'),(7,'大雄','bigbear@test.com','bigbear',0,'2025-11-22 12:48:48'),(8,'dora','dora@test.com','dora',0,'2025-11-22 12:50:50'),(9,'kay@test.com','kay@test.com','kay@test.com',0,'2025-11-22 12:57:36'),(10,'王曉明','wang@test.com','wang',0,'2025-11-22 12:58:24'),(11,'gorden@test.com','gorden@test.com','gorden@test.com',0,'2025-11-23 00:47:36'),(12,'yoyo@test.com','yoyo@test.com','yoyo@test.com',0,'2025-11-23 09:49:22'),(13,'happy','happy@test.com','happy',0,'2025-11-29 20:49:28');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int unsigned NOT NULL,
  `content` mediumtext NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (3,3,'hi',888,'2025-11-14 22:09:48'),(4,4,'nice to meet you',999,'2025-11-14 22:09:48'),(5,5,'what a beautiful day',666,'2025-11-14 22:09:48'),(10,1,'03',0,'2025-11-22 11:05:27');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `queryhistory`
--

DROP TABLE IF EXISTS `queryhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `queryhistory` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `inquirer_member_id` int unsigned NOT NULL,
  `queried_member_id` int unsigned NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `queryhistory`
--

LOCK TABLES `queryhistory` WRITE;
/*!40000 ALTER TABLE `queryhistory` DISABLE KEYS */;
INSERT INTO `queryhistory` VALUES (1,1,2,'2025-11-29 18:58:51'),(2,1,3,'2025-11-29 18:59:41'),(3,1,4,'2025-11-29 18:59:43'),(4,1,5,'2025-11-29 18:59:44'),(5,2,1,'2025-11-29 19:01:19'),(6,2,3,'2025-11-29 19:01:23'),(7,2,4,'2025-11-29 19:01:24'),(8,2,5,'2025-11-29 19:01:25'),(9,2,6,'2025-11-29 19:01:47'),(10,2,7,'2025-11-29 19:01:48'),(11,2,8,'2025-11-29 19:01:50'),(12,2,9,'2025-11-29 19:01:52'),(13,2,10,'2025-11-29 19:01:54'),(14,2,11,'2025-11-29 19:02:00'),(15,2,12,'2025-11-29 19:02:20'),(16,2,12,'2025-11-29 19:08:17'),(17,3,2,'2025-11-29 19:50:10'),(18,4,2,'2025-11-29 19:52:18'),(19,5,2,'2025-11-29 19:52:36'),(20,13,2,'2025-11-29 20:54:12'),(21,1,2,'2025-11-29 21:04:22'),(22,1,3,'2025-11-29 21:04:24'),(23,7,2,'2025-11-29 21:06:07');
/*!40000 ALTER TABLE `queryhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-29 21:14:04
