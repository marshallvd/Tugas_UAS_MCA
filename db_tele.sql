/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.4.32-MariaDB : Database - db_tele
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_tele` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `db_tele`;

/*Table structure for table `tb_cerita_rakyat` */

DROP TABLE IF EXISTS `tb_cerita_rakyat`;

CREATE TABLE `tb_cerita_rakyat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(255) NOT NULL,
  `isi` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_cerita_rakyat` */

LOCK TABLES `tb_cerita_rakyat` WRITE;

insert  into `tb_cerita_rakyat`(`id`,`judul`,`isi`) values 
(1,'Malin Kundang','Malin Kundang adalah anak durhaka yang dikutuk menjadi batu oleh ibunya karena tidak mengakui ibunya setelah menjadi kaya. Cerita ini mengajarkan pentingnya berbakti kepada orang tua dan akibat dari durhaka.'),
(2,'Sangkuriang','Sangkuriang jatuh cinta kepada Dayang Sumbi yang ternyata adalah ibunya sendiri. Setelah mengetahui kebenaran ini, Dayang Sumbi mengajukan syarat mustahil untuk menolak lamaran Sangkuriang. Cerita ini mengisahkan asal usul Gunung Tangkuban Perahu.'),
(3,'Bawang Merah Bawang Putih','Bawang Putih adalah anak yang baik hati yang selalu diperlakukan tidak adil oleh ibu tirinya, Bawang Merah. Namun, kebaikan hati Bawang Putih akhirnya membawa kebahagiaan dan keberuntungan bagi dirinya.'),
(4,'Timun Mas','Timun Mas adalah seorang gadis yang lahir dari timun emas yang diberikan oleh raksasa kepada sepasang suami istri. Untuk menghindari raksasa yang ingin memakannya, Timun Mas menggunakan benda-benda ajaib untuk melarikan diri.'),
(5,'Legenda Danau Toba','Legenda ini mengisahkan seorang nelayan yang menikahi seorang putri ikan dan memiliki anak bernama Samosir. Karena melanggar janji untuk tidak memberitahukan asal usul istrinya, sang istri kembali menjadi ikan dan terbentuklah Danau Toba.'),
(6,'Rangda dan Barong','Cerita ini menceritakan tentang pertempuran antara Rangda, penyihir jahat, dan Barong, makhluk mitos berbentuk singa atau babi yang melambangkan kebaikan dan perlindungan.'),
(7,'Keong Mas','Keong Mas adalah seorang putri yang lahir dari seekor keong emas. Ia dibesarkan oleh sepasang petani tua dan menjadi objek keinginan Raksasa Setan Kober yang ingin memakannya.'),
(8,'Jaka Tarub dan Nawang Wulan','Jaka Tarub adalah seorang pemuda yang menikahi Nawang Wulan, seorang bidadari dari langit. Mereka memiliki anak bersama sebelum Nawang Wulan akhirnya kembali ke surga.'),
(9,'Calon Arang','Calon Arang adalah seorang penyihir jahat yang mengutuk desa dengan menggunakan sihirnya setelah penduduk desa menolaknya. Ia digambarkan sebagai wanita yang memuja Kala Rauh dan memiliki ilmu hitam yang kuat.'),
(10,'Manik Angkeran','Manik Angkeran adalah seorang anak muda yang terkenal karena kecantikannya. Namun, ia harus menghadapi kejahatan dari saudara tirinya yang iri padanya.'),
(11,'Legenda Oleg Tamulilingan','Legenda ini menceritakan tentang keindahan tari Oleg Tamulilingan yang menceritakan kisah cinta antara seekor lebah dengan bunga.'),
(12,'Kesiman Jineng','Kesiman Jineng adalah cerita rakyat tentang seorang pemuda bernama Kesiman yang jatuh cinta pada seorang putri yang disegel di dalam Jineng (lumbung padi).'),
(13,'Lutung Kasarung','Lutung Kasarung adalah cerita tentang seorang putri yang diturunkan dari surga untuk mengajar moral kepada manusia. Ia juga memberikan petunjuk kepada Raden Panji, pangeran yang terbuang.'),
(14,'Sutasoma','Sutasoma adalah cerita tentang seorang pangeran Buddha yang menjadi raja di Kerajaan Magada. Ia mengajarkan nilai-nilai moral dan kebajikan kepada rakyatnya.'),
(15,'Legenda Dalem Balingkang','Legenda ini menceritakan tentang keberanian Dalem Balingkang dalam melawan musuh-musuhnya demi melindungi kerajaannya.'),
(16,'Rangda dan Ratu Kidul','Cerita ini menceritakan tentang pertemuan antara Rangda, penyihir jahat, dan Ratu Kidul, penguasa lautan selatan, yang terlibat dalam konflik.'),
(17,'Mendidihnya Taman Tirtagangga','Cerita ini menceritakan tentang bagaimana Taman Tirtagangga dibangun oleh raja Karangasem setelah seorang putranya yang tercinta meninggal dalam sebuah pertempuran.'),
(18,'Gong Wija dan Gong Wirang','Gong Wija dan Gong Wirang adalah dua gong keramat yang konon memiliki kekuatan magis untuk memanggil dewa-dewa dan menolak bencana.'),
(19,'Cerita Adipati Karna','Adipati Karna adalah cerita tentang kehidupan dan kepahlawanan Adipati Karna, tokoh penting dalam wiracarita Mahabharata yang dikenal karena kesetiaannya.'),
(20,'Barong Ket','Barong Ket adalah pertunjukan tari yang mengisahkan tentang perang antara dewa dan iblis, yang diwakili oleh Barong dan Rangda.'),
(21,'Pandji Tisna dan Karnapada','Pandji Tisna dan Karnapada adalah dua sahabat yang saling mencintai dan terlibat dalam petualangan untuk menghadapi raja setan dalam upaya menyelamatkan pangeran dari kutukan.');

UNLOCK TABLES;

/*Table structure for table `tb_inbox` */

DROP TABLE IF EXISTS `tb_inbox`;

CREATE TABLE `tb_inbox` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_inbox` */

LOCK TABLES `tb_inbox` WRITE;

insert  into `tb_inbox`(`id`,`user_id`,`message`,`timestamp`) values 
(1,'6090906462','halo','2024-06-19 00:41:39'),
(2,'6090906462','hai','2024-06-19 00:43:40'),
(3,'6090906462','halo','2024-06-19 00:45:17'),
(4,'6090906462','hai','2024-06-19 00:45:28'),
(5,'6090906462','hi','2024-06-19 00:45:31'),
(6,'6090906462','pantun','2024-06-19 00:48:20'),
(7,'6090906462','nama','2024-06-19 00:48:24'),
(8,'6090906462','apa kabar','2024-06-19 01:04:55'),
(9,'6090906462','p','2024-06-19 01:05:04'),
(10,'6090906462','bantuan','2024-06-19 01:05:16'),
(11,'6090906462','pantun','2024-06-19 09:26:44'),
(12,'6090906462','tes','2024-06-19 09:29:17'),
(13,'6090906462','1','2024-06-19 09:29:24'),
(14,'6090906462','pantun','2024-06-19 09:29:30'),
(15,'6090906462','akjsd','2024-06-19 09:31:33'),
(16,'6090906462','pantun','2024-06-19 09:32:02'),
(17,'6090906462','bisakah saat start itu kamu menjawab begini\nhai saya blablabla\nkemudian pesan baru\nberikut meupakan beberapa menu yang bisa saya lkukan\nkemudian pesan baru untuk menampilkan menu\n\nkemudian percantik menu mungkin dengan emoticon atau kreasi symbol','2024-06-19 09:33:42'),
(18,'6090906462','tes','2024-06-19 09:37:26'),
(19,'6090906462','pantun','2024-06-19 09:37:53'),
(20,'6090906462','jokes','2024-06-19 09:39:22'),
(21,'6090906462','malin kundang','2024-06-19 09:50:24'),
(22,'6090906462','sangkuriang','2024-06-19 09:54:03'),
(23,'6090906462','danau toba','2024-06-19 09:57:56'),
(24,'6090906462','test','2024-06-19 11:05:20'),
(25,'6090906462','malin','2024-06-19 11:05:58'),
(26,'6090906462','malin kundang','2024-06-19 11:06:04'),
(27,'6090906462','1','2024-06-19 11:23:26'),
(28,'6090906462','1','2024-06-19 11:26:43'),
(29,'6090906462','1','2024-06-19 11:36:54'),
(30,'6090906462','1','2024-06-19 11:38:20'),
(31,'6090906462','1','2024-06-19 11:41:02'),
(32,'6090906462','1','2024-06-19 11:57:19'),
(33,'6090906462','daftar','2024-06-19 11:57:52'),
(34,'6090906462','2','2024-06-19 11:58:04'),
(35,'6090906462','1','2024-06-19 12:03:27'),
(36,'6090906462','1','2024-06-19 12:05:54'),
(37,'6090906462','1','2024-06-19 12:09:42'),
(38,'6090906462','1','2024-06-19 12:12:05');

UNLOCK TABLES;

/*Table structure for table `tb_outbox` */

DROP TABLE IF EXISTS `tb_outbox`;

CREATE TABLE `tb_outbox` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_outbox` */

LOCK TABLES `tb_outbox` WRITE;

insert  into `tb_outbox`(`id`,`user_id`,`message`,`timestamp`) values 
(1,'6090906462','Echo: halo','2024-06-19 00:41:39'),
(2,'6090906462','Echo: hai','2024-06-19 00:43:40'),
(3,'6090906462','Sorry, I didn\'t understand that. Can you please rephrase?','2024-06-19 00:45:17'),
(4,'6090906462','Sorry, I didn\'t understand that. Can you please rephrase?','2024-06-19 00:45:28'),
(5,'6090906462','Hello! How can I help you today?','2024-06-19 00:45:31'),
(6,'6090906462','Ini dia pantun untuk Anda:\n\nJalan-jalan ke Kota Blitar,\nJangan lupa beli suvenir.\nHai teman yang pintar,\nTetaplah rajin belajar dan berpikir.','2024-06-19 00:48:20'),
(7,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi?','2024-06-19 00:48:24'),
(8,'6090906462','Saya hanyalah bot, jadi saya selalu baik! Ada yang bisa saya bantu?','2024-06-19 01:04:55'),
(9,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi?','2024-06-19 01:05:04'),
(10,'6090906462','Tentu! Bagaimana saya bisa membantu Anda hari ini?','2024-06-19 01:05:16'),
(11,'6090906462','Ini dia pantun untuk Anda:\n\nJalan-jalan ke Kota Blitar,\nJangan lupa beli suvenir.\nHai teman yang pintar,\nTetaplah rajin belajar dan berpikir.','2024-06-19 09:26:44'),
(12,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi?\n\nBerikut beberapa hal yang bisa saya lakukan:\n\n1. Pantun\nKetik \'pantun\' untuk mendapatkan pantun.\n\n2. Jokes\nKetik \'jokes\' untuk mendapatkan lelucon.\n\n3. Menyapa\nKetik \'halo\' atau \'hai\' untuk menyapa saya.\n\n4. Tanya Kabar\nKetik \'apa kabar\' atau \'bagaimana kabarmu\' untuk menanyakan kabar saya.\n\n5. Nama\nKetik \'siapa namamu\' untuk mengetahui nama saya.\n\n6. Bantuan\nKetik \'bantuan\' untuk mendapatkan bantuan.','2024-06-19 09:29:17'),
(13,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi?\n\nBerikut beberapa hal yang bisa saya lakukan:\n\n1. Pantun\nKetik \'pantun\' untuk mendapatkan pantun.\n\n2. Jokes\nKetik \'jokes\' untuk mendapatkan lelucon.\n\n3. Menyapa\nKetik \'halo\' atau \'hai\' untuk menyapa saya.\n\n4. Tanya Kabar\nKetik \'apa kabar\' atau \'bagaimana kabarmu\' untuk menanyakan kabar saya.\n\n5. Nama\nKetik \'siapa namamu\' untuk mengetahui nama saya.\n\n6. Bantuan\nKetik \'bantuan\' untuk mendapatkan bantuan.','2024-06-19 09:29:24'),
(14,'6090906462','Ini dia pantun untuk Anda:\n\nJalan-jalan ke Kota Blitar,\nJangan lupa beli suvenir.\nHai teman yang pintar,\nTetaplah rajin belajar dan berpikir.\n\nBerikut beberapa hal yang bisa saya lakukan:\n\n1. Pantun\nKetik \'pantun\' untuk mendapatkan pantun.\n\n2. Jokes\nKetik \'jokes\' untuk mendapatkan lelucon.\n\n3. Menyapa\nKetik \'halo\' atau \'hai\' untuk menyapa saya.\n\n4. Tanya Kabar\nKetik \'apa kabar\' atau \'bagaimana kabarmu\' untuk menanyakan kabar saya.\n\n5. Nama\nKetik \'siapa namamu\' untuk mengetahui nama saya.\n\n6. Bantuan\nKetik \'bantuan\' untuk mendapatkan bantuan.','2024-06-19 09:29:30'),
(15,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi?\n\nBerikut beberapa hal yang bisa saya lakukan:\n\n1. Pantun\nKetik \'pantun\' untuk mendapatkan pantun.\n\n2. Jokes\nKetik \'jokes\' untuk mendapatkan lelucon.\n\n3. Menyapa\nKetik \'halo\' atau \'hai\' untuk menyapa saya.\n\n4. Tanya Kabar\nKetik \'apa kabar\' atau \'bagaimana kabarmu\' untuk menanyakan kabar saya.\n\n5. Nama\nKetik \'siapa namamu\' untuk mengetahui nama saya.\n\n6. Bantuan\nKetik \'bantuan\' untuk mendapatkan bantuan.','2024-06-19 09:31:33'),
(16,'6090906462','Ini dia pantun untuk Anda:\n\nJalan-jalan ke Kota Blitar,\nJangan lupa beli suvenir.\nHai teman yang pintar,\nTetaplah rajin belajar dan berpikir.','2024-06-19 09:32:02'),
(17,'6090906462','Halo! Ada yang bisa saya bantu?','2024-06-19 09:33:42'),
(18,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi? ❓','2024-06-19 09:37:26'),
(19,'6090906462','Ini dia pantun untuk Anda:\n\nJalan-jalan ke Kota Blitar,\nJangan lupa beli suvenir.\nHai teman yang pintar,\nTetaplah rajin belajar dan berpikir. ?','2024-06-19 09:37:53'),
(20,'6090906462','Berikut adalah sebuah lelucon untuk Anda:\n\nKenapa sepeda tidak bisa berdiri sendiri?\nKarena sepeda hanya punya dua ‘roda’ (rida)! ?','2024-06-19 09:39:22'),
(21,'6090906462','? *Malin Kundang*\n\n? *Cerita Singkat:*\nMalin Kundang adalah anak durhaka yang dikutuk menjadi batu oleh ibunya karena tidak mengakui ibunya setelah menjadi kaya. Cerita ini mengajarkan pentingnya berbakti kepada orang tua dan akibat dari durhaka.','2024-06-19 09:50:24'),
(22,'6090906462','? *Sangkuriang*\n\n? *Cerita Singkat:*\nSangkuriang jatuh cinta kepada Dayang Sumbi yang ternyata adalah ibunya sendiri. Setelah mengetahui kebenaran ini, Dayang Sumbi mengajukan syarat mustahil untuk menolak lamaran Sangkuriang. Cerita ini mengisahkan asal usul Gunung Tangkuban Perahu.','2024-06-19 09:54:03'),
(23,'6090906462','? *Legenda Danau Toba*\n\n? *Cerita Singkat:*\nLegenda ini mengisahkan seorang nelayan yang menikahi seorang putri ikan dan memiliki anak bernama Samosir. Karena melanggar janji untuk tidak memberitahukan asal usul istrinya, sang istri kembali menjadi ikan dan terbentuklah Danau Toba.','2024-06-19 09:57:56'),
(24,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi? ❓','2024-06-19 11:05:20'),
(25,'6090906462','Maaf, saya tidak mengerti. Bisa tolong ulangi? ❓','2024-06-19 11:05:58'),
(26,'6090906462','? *Malin Kundang*\n\n? *Cerita Singkat:*\nMalin Kundang adalah anak durhaka yang dikutuk menjadi batu oleh ibunya karena tidak mengakui ibunya setelah menjadi kaya. Cerita ini mengajarkan pentingnya berbakti kepada orang tua dan akibat dari durhaka.','2024-06-19 11:06:04'),
(27,'6090906462','? *Daftar Cerita Rakyat:*\n\n\nKetik nomor atau judul cerita untuk membaca ceritanya.','2024-06-19 11:23:26'),
(28,'6090906462','? *Daftar Cerita Rakyat:*\n\n1. Malin Kundang\n2. Sangkuriang\n3. Bawang Merah Bawang Putih\n4. Timun Mas\n5. Legenda Danau Toba\n6. Rangda dan Barong\n7. Keong Mas\n8. Jaka Tarub dan Nawang Wulan\n9. Calon Arang\n10. Manik Angkeran\n11. Legenda Oleg Tamulilingan\n12. Kesiman Jineng\n13. Lutung Kasarung\n14. Sutasoma\n15. Legenda Dalem Balingkang\n16. Rangda dan Ratu Kidul\n17. Mendidihnya Taman Tirtagangga\n18. Gong Wija dan Gong Wirang\n19. Cerita Adipati Karna\n20. Barong Ket\n21. Pandji Tisna dan Karnapada\n\nKetik nomor atau judul cerita untuk membaca ceritanya.','2024-06-19 11:26:43'),
(29,'6090906462','Maaf, cerita yang Anda cari tidak ditemukan. Coba lagi dengan judul yang berbeda atau ketik \'1\' untuk melihat daftar cerita.','2024-06-19 11:57:52'),
(30,'6090906462','? *Daftar Cerita Rakyat:*\n\n1. Malin Kundang\n2. Sangkuriang\n3. Bawang Merah Bawang Putih\n4. Timun Mas\n5. Legenda Danau Toba\n6. Rangda dan Barong\n7. Keong Mas\n8. Jaka Tarub dan Nawang Wulan\n9. Calon Arang\n10. Manik Angkeran\n11. Legenda Oleg Tamulilingan\n12. Kesiman Jineng\n13. Lutung Kasarung\n14. Sutasoma\n15. Legenda Dalem Balingkang\n16. Rangda dan Ratu Kidul\n17. Mendidihnya Taman Tirtagangga\n18. Gong Wija dan Gong Wirang\n19. Cerita Adipati Karna\n20. Barong Ket\n21. Pandji Tisna dan Karnapada\n\nKetik nomor atau judul cerita untuk membaca ceritanya.','2024-06-19 12:03:27'),
(31,'6090906462','? *Daftar Cerita Rakyat:*\n\n1. Malin Kundang\n2. Sangkuriang\n3. Bawang Merah Bawang Putih\n4. Timun Mas\n5. Legenda Danau Toba\n6. Rangda dan Barong\n7. Keong Mas\n8. Jaka Tarub dan Nawang Wulan\n9. Calon Arang\n10. Manik Angkeran\n11. Legenda Oleg Tamulilingan\n12. Kesiman Jineng\n13. Lutung Kasarung\n14. Sutasoma\n15. Legenda Dalem Balingkang\n16. Rangda dan Ratu Kidul\n17. Mendidihnya Taman Tirtagangga\n18. Gong Wija dan Gong Wirang\n19. Cerita Adipati Karna\n20. Barong Ket\n21. Pandji Tisna dan Karnapada\n\nKetik nomor atau judul cerita untuk membaca ceritanya.','2024-06-19 12:05:54'),
(32,'6090906462','? *Daftar Cerita Rakyat:*\n\n1. Malin Kundang\n2. Sangkuriang\n3. Bawang Merah Bawang Putih\n4. Timun Mas\n5. Legenda Danau Toba\n6. Rangda dan Barong\n7. Keong Mas\n8. Jaka Tarub dan Nawang Wulan\n9. Calon Arang\n10. Manik Angkeran\n11. Legenda Oleg Tamulilingan\n12. Kesiman Jineng\n13. Lutung Kasarung\n14. Sutasoma\n15. Legenda Dalem Balingkang\n16. Rangda dan Ratu Kidul\n17. Mendidihnya Taman Tirtagangga\n18. Gong Wija dan Gong Wirang\n19. Cerita Adipati Karna\n20. Barong Ket\n21. Pandji Tisna dan Karnapada\n\nKetik nomor atau judul cerita untuk membaca ceritanya.','2024-06-19 12:09:42'),
(33,'6090906462','? *Daftar Cerita Rakyat:*\n\n1. Malin Kundang\n2. Sangkuriang\n3. Bawang Merah Bawang Putih\n4. Timun Mas\n5. Legenda Danau Toba\n6. Rangda dan Barong\n7. Keong Mas\n8. Jaka Tarub dan Nawang Wulan\n9. Calon Arang\n10. Manik Angkeran\n11. Legenda Oleg Tamulilingan\n12. Kesiman Jineng\n13. Lutung Kasarung\n14. Sutasoma\n15. Legenda Dalem Balingkang\n16. Rangda dan Ratu Kidul\n17. Mendidihnya Taman Tirtagangga\n18. Gong Wija dan Gong Wirang\n19. Cerita Adipati Karna\n20. Barong Ket\n21. Pandji Tisna dan Karnapada\n\nKetik nomor atau judul cerita untuk membaca ceritanya.','2024-06-19 12:12:05');

UNLOCK TABLES;

/*Table structure for table `tb_query` */

DROP TABLE IF EXISTS `tb_query`;

CREATE TABLE `tb_query` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query` text NOT NULL,
  `query_type` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_query` */

LOCK TABLES `tb_query` WRITE;

insert  into `tb_query`(`id`,`query`,`query_type`,`created_at`) values 
(1,'SELECT judul FROM tb_cerita_rakyat','list_stories','2024-06-19 11:57:19');

UNLOCK TABLES;

/*Table structure for table `tb_querylog` */

DROP TABLE IF EXISTS `tb_querylog`;

CREATE TABLE `tb_querylog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) NOT NULL,
  `query_type` varchar(50) NOT NULL,
  `query` text NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_querylog` */

LOCK TABLES `tb_querylog` WRITE;

insert  into `tb_querylog`(`id`,`user_id`,`query_type`,`query`,`timestamp`) values 
(1,'6090906462','menu_selection','menu_selection','2024-06-19 12:12:05');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
