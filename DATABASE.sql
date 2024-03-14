/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - smart_tender
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_tender` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `smart_tender`;

/*Table structure for table `bidders` */

DROP TABLE IF EXISTS `bidders`;

CREATE TABLE `bidders` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `bidders` */

insert  into `bidders`(`id`,`name`,`email`,`pwd`,`addr`,`pno`) values (1,'Fathima','cse.takeoff@gmail.com','Fathima@506','Sri nihitha, balaji clony ,thirupati,chittoor dist, AP','6308989089'),(2,'Sirisha','nagamchenchulakshmi@gmail.com','Siri@506','ongile , AP','5647891230'),(3,'Sirisha','nagamchenchulakshmi@gmail.com','Siri@506','ongile , AP','5647891230'),(4,'Farhath','cse.takeoff@gmail.com','Farhath@123','Alipiri, Tirupati, AP','9902862544');

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `obj` varchar(100) DEFAULT NULL,
  `cost` varchar(100) DEFAULT NULL,
  `sdate` varchar(100) DEFAULT NULL,
  `edate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notifications` */

insert  into `notifications`(`id`,`email`,`obj`,`cost`,`sdate`,`edate`) values (1,'lakshmi@gmail.com','road construction issued by AP goverment','1,00,00,000','2021-10-09','2021-10-14'),(3,'rupesh452@gmail.com','We are initiating a tender on S.V music college','5,00,000,00','2021-10-11','2021-10-19');

/*Table structure for table `tender_files` */

DROP TABLE IF EXISTS `tender_files`;

CREATE TABLE `tender_files` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `tid` int(100) DEFAULT NULL,
  `temail` varchar(100) DEFAULT NULL,
  `obj` varchar(100) DEFAULT NULL,
  `cost` varchar(100) DEFAULT NULL,
  `sdate` varchar(100) DEFAULT NULL,
  `edate` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pan` varchar(100) DEFAULT NULL,
  `adhar` varchar(100) DEFAULT NULL,
  `file` longblob,
  `hash1` varchar(1000) DEFAULT NULL,
  `hash2` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time1` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tender_files` */

insert  into `tender_files`(`id`,`tid`,`temail`,`obj`,`cost`,`sdate`,`edate`,`email`,`pan`,`adhar`,`file`,`hash1`,`hash2`,`date`,`time1`,`status`) values (1,1,'lakshmi@gmail.com','road construction issued by AP goverment','1,00,00,000','2021-10-09','2021-10-15','cse.takeoff@gmail.com','SBVC1234556','90890989098','†E”÷-Ã@π©Ú·G\"b@bM6‰o÷üT	∂>∫ @Yù∑J>á™ö\\Ú∏.ö\nﬂ•∑‘¬’ºXlY≥˚±Ùü#','88d20fc0fcde30d82b1b3218010b88090eaa922a','0ce977bd372b861978401c4e476f5449b9d38c34','2021-10-09','17:31:48','Completed'),(2,1,'lakshmi@gmail.com','road construction issued by AP goverment','1,00,00,000','2021-10-09','2021-10-14','nagamchenchulakshmi@gmail.com','SBVC1234556','90890989098','†E”÷-Ã@π©Ú·G\"b@bM6‰o÷üT	∂>∫ @Yù∑J>á™ö\\Ú∏.ö\nﬂ•∑‘¬’ºXlY≥˚±Ùü#','88d20fc0fcde30d82b1b3218010b88090eaa922a','0ce977bd372b861978401c4e476f5449b9d38c34','2021-10-11','10:14:49','Cancel'),(3,3,'rupesh452@gmail.com','We are initiating a tender on S.V music college','5,00,000,00','2021-10-11','2021-10-19','cse.takeoff@gmail.com','SBVC1234556','90890989098','€êæCÍ›Àåx˚ÔˆCFÇÄx;+µIÌﬁ^ö∫§7/gëÿ6U? ˆ/\nÕq®◊∑PnÎEÔ4˘&ΩÍ≤mõÆ\\ATœJ]Xéº#0SÂ%','6860c94efe4982008ffaa99230e93d1bded432b7','08d3925c9ffd8461701328e362788dc3b8100f0e','2021-10-11','12:09:54','Completed');

/*Table structure for table `tenders` */

DROP TABLE IF EXISTS `tenders`;

CREATE TABLE `tenders` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tenders` */

insert  into `tenders`(`id`,`name`,`email`,`pwd`,`addr`,`pno`) values (1,'Lakshmi','lakshmi@gmail.com','Lakshmi@506','303, AVR Buildings, Balaji Colony  Opp S.V.music College, Tirupati, Chittoor Dist, Andhra Pradesh','9630258741'),(2,'Rupesh','rupesh452@gmail.com','Rupesh@123','Balaji colony, tirupati, AP','6308989089');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
