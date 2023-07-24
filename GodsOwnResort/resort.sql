-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 31, 2020 at 10:07 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `resort`
--

-- --------------------------------------------------------

--
-- Table structure for table `accomodation`
--

CREATE TABLE IF NOT EXISTS `accomodation` (
  `acid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) DEFAULT NULL,
  `acname` varchar(50) DEFAULT NULL,
  `descr` varchar(500) DEFAULT NULL,
  `charge` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`acid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `accomodation`
--

INSERT INTO `accomodation` (`acid`, `rid`, `acname`, `descr`, `charge`, `image`) VALUES
(1, 1, 'ZURI ROOM', 'The Zuri rooms are ideal for both—a holiday as well as a short business stay, and will leave you wishing to return to This oasis of peace and luxury.', '20000', 'static/media/zuri-room-banner-new.jpg'),
(2, 1, 'ZURI DELUXE ROOM', 'Located on the first floor, the 42 square meter Zuri Deluxe room in Kumarakom is an epitome of luxury. Featuring a spacious balcony overlooking a beautiful lagoon, it offers spectacular views of the surrounding areas, while cradling you in absolute comfort.', '45000', 'static/media/kumarakom-zuri-deluxe-room-banner_K9z08wy.jpg'),
(3, 1, 'ZURI COTTAGE', 'Recreating the charm of Kerala, the quaint Zuri cottages offer a world of modern luxury and natural beauty. Beautiful interiors complement the stunning views of the blue lagoon that stretches across the horizon. Choose to stay in the Zuri Cottage and be transported to an ethereal world of beauty and luxury.', '60000', 'static/media/zuri-presidential-pool-villa_YoDKVtQ.jpg'),
(4, 1, 'Zuri Pool Villas', 'he Zuri prides itself on being one of the few resorts with private pool villas in Kumarakom, Kerala. Spread out over 70 square metres, the Presidential Villa comprises of a living and dining room, master bedroom, semi-outdoor bathroom and a private garden overlooking an independent pool. ', '75000', 'static/media/pool-villa-banner-new.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `acco_booking`
--

CREATE TABLE IF NOT EXISTS `acco_booking` (
  `abid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `roomid` int(11) NOT NULL,
  `checkin` varchar(50) NOT NULL,
  `checkout` varchar(50) NOT NULL,
  `numroom` int(11) NOT NULL,
  `totamt` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`abid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `acco_booking`
--

INSERT INTO `acco_booking` (`abid`, `rid`, `cid`, `roomid`, `checkin`, `checkout`, `numroom`, `totamt`, `status`) VALUES
(6, 1, 1, 1, '2020-01-28', '2020-01-31', 1, '60000', 'Accept');

-- --------------------------------------------------------

--
-- Table structure for table `ayurvedha`
--

CREATE TABLE IF NOT EXISTS `ayurvedha` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `aname` varchar(100) NOT NULL,
  `adesc` varchar(4000) NOT NULL,
  `amount` int(11) NOT NULL,
  `days` varchar(100) NOT NULL,
  `image` varchar(200) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `ayurvedha`
--

INSERT INTO `ayurvedha` (`aid`, `rid`, `aname`, `adesc`, `amount`, `days`, `image`) VALUES
(1, 1, 'REJUVENATION PACKAGE', 'Rejuvenation – The term itself means “reversing the aging process” and this program aims at making one feel younger. This program includes treatments using herbal oils and therapies, which revitalizes and detoxifies your body thus purifying you and making you feel completely rejuvenated. This therapy helps to slow down the aging process. The major benefits of this treatment is to prolong life span, strengthen sense organs, improve memory, obtain perfect health, youthfulness and increased physical endurance.', 35000, '21 Nights', 'static/media/ayurveda-package-6_kL3Lqg6.jpg'),
(2, 1, 'PANCHAKARMA PROGRAMME', 'Panchakarma – These are the body purificatory procedures which are mentioned in Ayurveda to purify our body. According to Ayurveda the human body is prone to get accumulate the toxins in the body due to improper food habits, life style, which in long term leads to various diseases. By having the purification of the body on regular basis we will be healthy. This program includes treatments using medicated herbal oils and also Vastis (medicated enemas which will help in removing the toxins away from the body), which revitalizes and detoxifies your body. The major benefits of this treatment is to prolong life span, strengthen sense organs, improve memory, obtain perfect health, youthfulness and increased physical endurance.', 75000, '14 Nights', 'static/media/ayurveda-package-3-1.jpg'),
(3, 1, 'DETOXIFICATION PROGRAMME', 'A Detoxification programme is vital to help you to prevent disease and to facilitate an incredible sense of well-being and happiness. It is a passive process of purifying the whole body by eliminating the toxins accumulated as a result of improper diet and lifestyle. This enables you to attain proper balance of Vata, Pitta and Kapha, the bio regulating forces in your body resulting in improved immunity and optimum functioning of the body systems.', 45000, '14 Nights', 'static/media/ayurveda-package-4-1.jpg'),
(4, 1, 'WEIGHT MANAGEMENT PROGRAMME', 'From the perspective of Ayurveda, losing weight is not about starving or suppressing the appetite. It is about balancing your fat metabolism. You do not have to starve yourself or exercise until you drop. Balance is the key with this therapy that will be tailor made to suit your constitution.', 55000, '21 Nights', 'static/media/ayurveda-package-1-1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `ayur_booking`
--

CREATE TABLE IF NOT EXISTS `ayur_booking` (
  `aybid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `aid` int(11) NOT NULL,
  `checkin` varchar(50) NOT NULL,
  `dbook` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`aybid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `ayur_booking`
--


-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
  `catid` int(11) NOT NULL AUTO_INCREMENT,
  `catname` varchar(50) NOT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`catid`, `catname`) VALUES
(1, 'Wildlife'),
(2, 'Beach side'),
(3, 'Lake side'),
(4, 'Islands'),
(5, 'Spa'),
(6, 'Cities');

-- --------------------------------------------------------

--
-- Table structure for table `cust_reg`
--

CREATE TABLE IF NOT EXISTS `cust_reg` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `cust_reg`
--

INSERT INTO `cust_reg` (`cid`, `cname`, `address`, `country`, `state`, `phone`, `email`, `password`) VALUES
(1, 'Jithin', 'LCC', 'India', 'Kerala', '9638527410', 'jithin@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `dining`
--

CREATE TABLE IF NOT EXISTS `dining` (
  `dinid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `dname` varchar(50) DEFAULT NULL,
  `ddesc` varchar(500) DEFAULT NULL,
  `damt` varchar(50) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dinid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `dining`
--

INSERT INTO `dining` (`dinid`, `rid`, `dname`, `ddesc`, `damt`, `image`) VALUES
(1, 1, 'LIME TREE', 'Breathe in the fresh sea breeze that carries the exotic fragrance of Lime Tree’s array of exotic dishes ranging from regional favourites to classics and continental to Pan-Asian awash with soft lights', '2000', 'static/media/Speciality-Restaurant.jpg'),
(2, 1, 'THE TRUNK CALL BAR', 'Overlooking the lush green landscaped garden and the calm waters of the Vembanad Lake, Zuri’s Trunk Call Bar offers a quaint dining experience. ', '3000', 'static/media/the-trunk-call-bar.jpg'),
(3, 1, 'LAGUNA BASS', 'Experience the rich flavours and fragrance of Kerala’s sea food at Laguna Bass with an innovative interactive kitchen. You can even choose from the freshest live catch of the day! ', '5000', 'static/media/lagunabar-banner-new.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `dining_booking`
--

CREATE TABLE IF NOT EXISTS `dining_booking` (
  `dbid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `rest` int(11) NOT NULL,
  `guest` int(11) NOT NULL,
  `bdate` varchar(50) NOT NULL,
  `dbook` varchar(50) NOT NULL,
  `time` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`dbid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `dining_booking`
--


-- --------------------------------------------------------

--
-- Table structure for table `district`
--

CREATE TABLE IF NOT EXISTS `district` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `dname` varchar(50) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `district`
--

INSERT INTO `district` (`did`, `dname`) VALUES
(1, 'Trivandrum'),
(2, 'Kollam'),
(3, 'Pathanamthitta'),
(4, 'Alappuzha'),
(5, 'Kottayam'),
(6, 'Idukki'),
(7, 'Ernakulam'),
(8, 'Thrissur'),
(9, 'Palakkad'),
(10, 'Malappuram'),
(11, 'Kozhikkod'),
(12, 'Wayanadu'),
(13, 'Kannur'),
(14, 'Kasargode');

-- --------------------------------------------------------

--
-- Table structure for table `facility`
--

CREATE TABLE IF NOT EXISTS `facility` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(50) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `fimage` varchar(200) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `facility`
--

INSERT INTO `facility` (`fid`, `rid`, `fname`, `fimage`) VALUES
(1, 1, 'Swimming Pool', 'static/media/slide1.jpg'),
(2, 1, 'Fitness Center', 'static/media/PPTIRT_Fitness_Center_1000x600_29686.jpg'),
(3, 1, 'Wifi', 'static/media/tim-hortons-wifi.jpg'),
(4, 1, 'Infinity Swimming Pool', 'static/media/1%20(1).jpg');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  `fdate` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `feedback`
--


-- --------------------------------------------------------

--
-- Table structure for table `hall`
--

CREATE TABLE IF NOT EXISTS `hall` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) DEFAULT NULL,
  `hname` varchar(50) DEFAULT NULL,
  `hcap` varchar(50) DEFAULT NULL,
  `harea` varchar(50) DEFAULT NULL,
  `hamt` varchar(50) DEFAULT NULL,
  `himage` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `hall`
--

INSERT INTO `hall` (`hid`, `rid`, `hname`, `hcap`, `harea`, `hamt`, `himage`) VALUES
(1, 1, 'WEDDING VENUE', '750', '1500 sqft', '40000', 'static/media/kumarakom-wedding-banner_lq2VVsg.jpg'),
(2, 1, 'BUSINESS HOTEL', '70', '300 Sqft', '25000', 'static/media/kumarakom-meeting-banner.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `hall_booking`
--

CREATE TABLE IF NOT EXISTS `hall_booking` (
  `hbid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `hid` int(11) NOT NULL,
  `bdate` varchar(50) NOT NULL,
  `dbook` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`hbid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `hall_booking`
--

INSERT INTO `hall_booking` (`hbid`, `rid`, `cid`, `hid`, `bdate`, `dbook`, `amount`, `status`) VALUES
(1, 1, 1, 2, '2020-01-30', '2020-01-28', '25000', 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `homepage`
--

CREATE TABLE IF NOT EXISTS `homepage` (
  `desid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `accotitle` varchar(50) NOT NULL,
  `aimage` varchar(100) NOT NULL,
  `dintitle` varchar(50) NOT NULL,
  `dimage` varchar(100) NOT NULL,
  `haltitle` varchar(50) NOT NULL,
  `himage` varchar(100) NOT NULL,
  `aytitle` varchar(100) NOT NULL,
  `ayimage` varchar(200) NOT NULL,
  `packtitle` varchar(100) NOT NULL,
  `packimage` varchar(200) NOT NULL,
  `patitle` varchar(50) NOT NULL,
  `pimage` varchar(100) NOT NULL,
  PRIMARY KEY (`desid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `homepage`
--

INSERT INTO `homepage` (`desid`, `rid`, `accotitle`, `aimage`, `dintitle`, `dimage`, `haltitle`, `himage`, `aytitle`, `ayimage`, `packtitle`, `packimage`, `patitle`, `pimage`) VALUES
(1, 1, 'ENTER THE WORLD FOR LUXURY', 'static/media/zuri-presidential-pool-villa.jpg', 'ADVENTURE FOR YOUR TASTE BUDS', 'static/media/lime-tree2.jpg', 'ENJOY EVERY MOMENTS WITH US', 'static/media/conference.jpg', 'THE PERFECT VACATION', 'static/media/ayurveda2.jpg', 'THE DREAM SETTING OF YOUR DREAMS', 'static/media/hp.jpg', 'FACILITIES', 'static/media/spa.jpg.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `uname` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `pass`, `utype`) VALUES
('jithin@gmail.com', '123', 'Customer'),
('zuri@gmail.com', '123', 'Resort'),
('admin@gmail.com', 'admin', 'Admin');

-- --------------------------------------------------------

--
-- Table structure for table `package`
--

CREATE TABLE IF NOT EXISTS `package` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `pname` varchar(500) NOT NULL,
  `pdesc` varchar(4000) NOT NULL,
  `details` varchar(4000) NOT NULL,
  `night` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `package`
--

INSERT INTO `package` (`pid`, `rid`, `pname`, `pdesc`, `details`, `night`, `amount`, `image`) VALUES
(1, 1, 'HONEYMOON PACKAGE', 'Fall in love with our custom-made couple''s holiday package. Be it an awaited honeymoon or a well-deserved romantic getaway, The ZuriKumarakom Resort and Spa is the perfect destination for two.', 'Accommodation in well-appointed rooms for 2 nights and 3 days for a couple Refreshing welcome drink on arrival & Fruit basket in the room on the day of arrival Bottle of wine & a delicious cake in the room on arrival Chocolate platter every day during your stay Evening Tea/Coffee with cookies High Speed Wireless Internet Romantic Floral bath in room once during the stay Lavish buffet spread for breakfast on a daily basis. (In room breakfast on fixed menu for Pool Villa booking) Half day sightseeing of Kottayam in your own private air-conditioned car', '2 NIGHTS', 45000, 'static/media/honeymoon-package_djxyOPq.jpg'),
(2, 1, 'THE ZURI KUMARAKOM PACKAGE', 'Fishing in lagoon & cycling Pedal boat at Lagoon between 11 AM to 6 PM Yoga and meditation at Body Temple 7.00am -8.00am Cultural program including live music entertainment at “Natya – Our Exclusive Amphitheatre” by The Lime Tree Restaurant Deck Evening cruise through pristine backwaters for 45 minutes once during the stay (subject to weather conditions) Activities for Kids', 'Traditional Welcome drink on arrival Accommodation in well-appointed rooms as per category for 2 nights Fruit basket in the room on the day of arrival Centrally air conditioned rooms with Tea/Coffee makers, in-room safes and data ports Buffet meals as per room plan at our all day dining restaurant “Lime Tree”. Evening Tea/Coffee with cookies Complimentary use of Swimming Pool, Jacuzzi, Gymnasium Sauna & Steam(Prior appointments required)', '2 NIGHTS / 3 DAYS', 40000, 'static/media/kumrakom-offer.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `package_booking`
--

CREATE TABLE IF NOT EXISTS `package_booking` (
  `pbid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `cdate` varchar(50) NOT NULL,
  `dbook` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`pbid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `package_booking`
--

INSERT INTO `package_booking` (`pbid`, `rid`, `cid`, `pid`, `cdate`, `dbook`, `status`) VALUES
(1, 1, 1, 2, '2020-02-01', '2020-01-28', 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `resort_reg`
--

CREATE TABLE IF NOT EXISTS `resort_reg` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `district` varchar(50) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `mobile` varchar(50) NOT NULL,
  `officeno` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `rimage` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `r_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `resort_reg`
--

INSERT INTO `resort_reg` (`rid`, `name`, `address`, `district`, `location`, `mobile`, `officeno`, `email`, `category`, `rimage`, `password`, `r_status`) VALUES
(1, 'The Zuri Kumarakom', 'V 235 A1 to A54, Karottukayal, Kumarakom, Kottayam', '5', 'Kumarakom', '7418529630', '+91 481 252 7272', 'zuri@gmail.com', '3', 'static/media/zuri_kumarakom_complimentary_amen_S1CzYsR.jpg', '123', 'Accept');
