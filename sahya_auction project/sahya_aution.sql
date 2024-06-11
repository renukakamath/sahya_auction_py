/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - sahya_auction
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sahya_auction` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `sahya_auction`;

/*Table structure for table `auction` */

DROP TABLE IF EXISTS `auction`;

CREATE TABLE `auction` (
  `auction_id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `auction` varchar(100) DEFAULT NULL,
  `weight` varchar(100) DEFAULT NULL,
  `auction_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `winner_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `stock_id` int(11) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`auction_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `auction` */

insert  into `auction`(`auction_id`,`seller_id`,`auction`,`weight`,`auction_date`,`end_date`,`time`,`amount`,`winner_id`,`status`,`stock_id`,`image`) values 
(1,2,'abcdef','100','2023-04-03','2023-04-04','12:00',200,0,'stop',1,NULL),
(2,2,'B1','100kg','2023-04-13','2023-04-13','20:34',1000,0,'start',1,NULL),
(3,2,'b8','100','0','0','0',0,0,'pending',1,'static/d99824c8-144a-4c55-8143-2202ec70c414erica-zhou-IHpUgFDn7zU-unsplash.jpg');

/*Table structure for table `auctioneer` */

DROP TABLE IF EXISTS `auctioneer`;

CREATE TABLE `auctioneer` (
  `auctioner_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `auctioner_name` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`auctioner_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `auctioneer` */

insert  into `auctioneer`(`auctioner_id`,`login_id`,`auctioner_name`,`place`,`phone`,`email`) values 
(1,6,'achuus','palakkad','7896541230','achu@gmail.com');

/*Table structure for table `auctionpayment` */

DROP TABLE IF EXISTS `auctionpayment`;

CREATE TABLE `auctionpayment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `auction_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `auctionpayment` */

insert  into `auctionpayment`(`payment_id`,`auction_id`,`amount`,`date`) values 
(1,1,'350','2023-04-03 15:59:43'),
(2,2,'4000','2023-04-05 14:15:48');

/*Table structure for table `bid` */

DROP TABLE IF EXISTS `bid`;

CREATE TABLE `bid` (
  `bid_id` int(11) NOT NULL AUTO_INCREMENT,
  `auction_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `buyer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`bid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `bid` */

insert  into `bid`(`bid_id`,`auction_id`,`amount`,`date`,`time`,`status`,`buyer_id`) values 
(1,1,200,'2023-04-03','12:00','pending',0),
(2,1,250,'2023-04-03','12:58:21','0',2),
(3,1,260,'2023-04-03','14:22:45','0',2),
(4,1,280,'2023-04-03','14:28:49','0',2),
(5,1,300,'2023-04-03','14:29:36','0',2),
(6,1,350,'2023-04-03','15:02:30','0',1),
(7,2,1000,'2023-04-06','10:00','pending',0),
(8,2,2000,'2023-04-05','14:11:36','0',1),
(9,2,2001,'2023-04-05','14:13:38','0',2),
(10,2,4000,'2023-04-05','14:13:54','0',2),
(11,2,10000,'2023-04-19','15:18','winner',0),
(12,2,1000,'2023-04-13','20:34','pending',0),
(13,2,5000,'2023-04-05','15:37:38','0',1);

/*Table structure for table `bookfertilizer` */

DROP TABLE IF EXISTS `bookfertilizer`;

CREATE TABLE `bookfertilizer` (
  `bookfertilizer_id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `fertilizer_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bookfertilizer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `bookfertilizer` */

insert  into `bookfertilizer`(`bookfertilizer_id`,`seller_id`,`fertilizer_id`,`quantity`,`amount`,`date`,`status`) values 
(1,2,1,'3','3000','2023-04-04','booked'),
(2,2,1,'4','4000','2023-04-04','booked'),
(3,2,1,'4','4000','2023-04-04','booked'),
(4,2,1,'6','6000','2023-04-04','booked'),
(5,2,1,'1','1000','2023-04-04','booked'),
(6,2,1,'6','6000','2023-04-04','booked'),
(7,2,1,'6','6000','2023-04-04','booked'),
(8,2,1,'4','4000','2023-04-04','booked'),
(9,2,1,'1','1000','2023-04-04','booked'),
(10,2,1,'3','3000','2023-04-05','booked');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`user_id`,`total`,`date`,`status`) values 
(1,1,'200','2023-04-21','paid');

/*Table structure for table `booking_child` */

DROP TABLE IF EXISTS `booking_child`;

CREATE TABLE `booking_child` (
  `bookingchild_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(10) DEFAULT NULL,
  `product_id` int(10) DEFAULT NULL,
  `quantity` varchar(10) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`bookingchild_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `booking_child` */

/*Table structure for table `bookingchild` */

DROP TABLE IF EXISTS `bookingchild`;

CREATE TABLE `bookingchild` (
  `bookingchild_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(10) DEFAULT NULL,
  `product_id` int(10) DEFAULT NULL,
  `quantity` varchar(10) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`bookingchild_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bookingchild` */

insert  into `bookingchild`(`bookingchild_id`,`booking_id`,`product_id`,`quantity`,`amount`) values 
(1,1,1,'10','1000');

/*Table structure for table `buyer` */

DROP TABLE IF EXISTS `buyer`;

CREATE TABLE `buyer` (
  `buyer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `buyer_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`buyer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `buyer` */

insert  into `buyer`(`buyer_id`,`login_id`,`buyer_name`,`place`,`phone`,`email`) values 
(1,8,'ammu','pala','12365478990','ammu@gmail.com'),
(2,9,'remi','varkala','7410236589','remi@gmail.com');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) DEFAULT NULL,
  `complaint` varchar(20) DEFAULT NULL,
  `reply` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`reply`,`date`) values 
(1,8,'hellooo','OKK','2023-04-03');

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fsrmer_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `farmer` */

insert  into `farmer`(`farmer_id`,`login_id`,`fsrmer_name`,`place`,`phone`,`email`) values 
(1,1,'dsfs','place','1234256546','we@gmail.com'),
(2,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `fertilizer` */

DROP TABLE IF EXISTS `fertilizer`;

CREATE TABLE `fertilizer` (
  `fertilizer_id` int(11) NOT NULL AUTO_INCREMENT,
  `fertilizer` varchar(20) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `price` varchar(10) DEFAULT NULL,
  `stock` varchar(10) DEFAULT NULL,
  `image` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`fertilizer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer` */

insert  into `fertilizer`(`fertilizer_id`,`fertilizer`,`details`,`price`,`stock`,`image`) values 
(1,'qqqzz','zaazz','1000','100','static/ead78e35-27fe-422f-9571-92efc182f9afimage_64086130caeab.jpg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'glim@email.com','7890','pending'),
(3,'glim@email.com','7890','farmer'),
(9,'remi','remi','buyer'),
(6,'achu','achu','auctioner'),
(7,'amal','amal','seller'),
(8,'ammu','ammu','buyer'),
(11,'user','user','user'),
(12,'hello','hello','user');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`date`) values 
(1,8,'4000','2023-04-04'),
(2,1,'1000','2023-04-21');

/*Table structure for table `price` */

DROP TABLE IF EXISTS `price`;

CREATE TABLE `price` (
  `price_id` int(11) NOT NULL AUTO_INCREMENT,
  `price` int(50) DEFAULT NULL,
  PRIMARY KEY (`price_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `price` */

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `quality_id` int(11) DEFAULT NULL,
  `product` varchar(20) DEFAULT NULL,
  `weight` varchar(10) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `rate` varchar(20) DEFAULT NULL,
  `stock` varchar(20) DEFAULT NULL,
  `imag` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`quality_id`,`product`,`weight`,`details`,`rate`,`stock`,`imag`) values 
(1,5,'asasa','100','mkmm','100','10','static/a4234360-56de-42f8-a87f-c1d09cbe68b9floriane-vita-FyD3OWBuXnY-unsplash.jpg');

/*Table structure for table `quality` */

DROP TABLE IF EXISTS `quality`;

CREATE TABLE `quality` (
  `quality_id` int(11) NOT NULL AUTO_INCREMENT,
  `quality` varchar(10) DEFAULT NULL,
  `percent` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`quality_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `quality` */

insert  into `quality`(`quality_id`,`quality`,`percent`) values 
(5,'average','C');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `Rated` varchar(10) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

/*Table structure for table `seller` */

DROP TABLE IF EXISTS `seller`;

CREATE TABLE `seller` (
  `seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `seller_name` varchar(20) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `seller` */

insert  into `seller`(`seller_id`,`login_id`,`seller_name`,`place`,`phone`,`email`) values 
(1,3,'akash','kattappana','90875645','glim@email.com'),
(2,7,'amal','kollam','7896541230','a@gmail.com');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `quality_id` int(11) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  `stock` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`stock_id`,`quality_id`,`seller_id`,`stock`) values 
(1,5,2,'10');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(10) DEFAULT NULL,
  `place` varchar(10) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`place`,`phone`,`email`) values 
(1,12,'gdgdgs','vxvdvd','hello','1234567891','re@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
