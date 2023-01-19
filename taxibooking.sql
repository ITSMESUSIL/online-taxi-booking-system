-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2023 at 06:39 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `taxibooking`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `pickup_location` varchar(100) NOT NULL,
  `drop_location` varchar(100) NOT NULL,
  `sn` int(11) NOT NULL,
  `ride_status` varchar(100) DEFAULT NULL,
  `driver_id` int(100) DEFAULT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `date`, `time`, `pickup_location`, `drop_location`, `sn`, `ride_status`, `driver_id`, `price`) VALUES
(85, 'Thu,Jan 12 23', '10pm', 'kupandole', 'baneshwor', 20, 'completed', 5, 220),
(86, 'Thu,Jan 12 23', '10pm', 'kupandole', 'koteshwor', 21, 'completed', 5, 220);

-- --------------------------------------------------------

--
-- Table structure for table `customer_register`
--

CREATE TABLE `customer_register` (
  `sn` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `pay_method` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_register`
--

INSERT INTO `customer_register` (`sn`, `name`, `address`, `phone`, `email`, `password`, `pay_method`) VALUES
(12, 'sushil', 'kupandole', '9865630920', 'sushil@', 'sushil@', 'online payment'),
(13, 'dipesh', 'maitidevi', '87654', 'dipesh', 'dipesh', 'online payment'),
(14, 'rahul', 'cocacola', '789', 'rahul', 'rahul', 'online payment'),
(15, 'sudarshan', 'kandevsthan', '6789789', 'sudarshan', 'sudarshan', 'online payment'),
(16, 'ranjit', 'kupandole', '56789876', 'ranjit@', 'ranjit@', 'cash'),
(17, 'sagar', 'chitwan', '8767897678', 'sagar@gmail.como', 'sagar@', 'online payment'),
(18, 'pranish ', 'chitwan', '986789876', 'pranish@', 'pranish', 'select'),
(20, 'sushil kathayat', 'kupandole', '9865630920', 'sushil@gmail.com', 'sushil@gmail.com', 'online payment'),
(21, 'sushil kathayat', 'kupandole', '9865630920', 'sushil@gmail.com', 'sushil@', 'select');

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `driver_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `taxino` varchar(100) NOT NULL,
  `license` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`driver_id`, `name`, `phone`, `address`, `email`, `password`, `taxino`, `license`, `status`) VALUES
(1, 'manish mahatto', '9867473827', 'maitidevi,ktm', 'manish@gmail.com', 'manish@gmail12', '1', '345678jkjh3', 'available'),
(2, 'avinash chaudhary', '9876747362', 'kupandole,lalitpur', 'avinash@gmail.com', 'avinash@gmail12', '2', '23456as7hA', 'available'),
(3, 'anish panta', '9865678903', 'lokanthali,bhaktpur', 'anish@gmail.com', 'anish@12', '3', '18466ASj39', 'available'),
(4, 'zacky raila', '9876545678', 'dakshinkali,lalitpur', 'zacky@gmail.com', 'zacky@gmail12', '4', '89876789ABD245', 'available'),
(5, 'sushant Patel', '9867635234', 'balkumari,lalitpur', 'sushant@gmail.com', 'sushant@gmail12', '5', '677627877KL3Sf', 'available'),
(6, 'damon ktz', '0901283849', 'dipayal,doti', 'damon@gmail.com', 'damon@gmail12', '6', '12343ed', 'available');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sn` (`sn`),
  ADD KEY `driver_id` (`driver_id`);

--
-- Indexes for table `customer_register`
--
ALTER TABLE `customer_register`
  ADD PRIMARY KEY (`sn`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT for table `customer_register`
--
ALTER TABLE `customer_register`
  MODIFY `sn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`sn`) REFERENCES `customer_register` (`sn`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`driver_id`) REFERENCES `driver` (`driver_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
