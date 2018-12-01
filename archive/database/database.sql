-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2018 at 03:05 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

SET AUTOCOMMIT = 0;

START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


--
-- Database: `database`
--

-- --------------------------------------------------------

--
-- 
Table structure for table `bank`
--


CREATE TABLE `bank` (
  `Bank_ID` int(5) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Bank_Type` varchar(50) NOT NULL,
  `Ownership` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
--
 Dumping data for table `bank`
--


INSERT INTO `bank` (`Bank_ID`, `Name`, `Bank_Type`, `Ownership`) VALUES
(1, 'Sonali Bank Limited', 'SOCB', 'State'),
(2, 'Janata Bank Limited', 'SOCB', 'State'),
(3, 'Agrani Bank Limited', 'SOCB', 'State'),
(4, 'Rupali Bank Limited', 'SOCB', 'State'),
(5, 'BASIC Bank Limited', 'SOCB', 'State'),
(6, 'Bangladesh Development Bank Limited', 'SOCB', 'State'),
(7, 'Bangladesh Krishi Bank ', 'SDB', 'State'),
(8, 'Rajshahi Krishi Unnayan Bank', 'SDB', 'State'),
(9, 'Probashi Kallyan Bank', 'SDB', 'State'),
(10, 'AB Bank', 'PCB', 'Private');

-- --------------------------------------------------------

--
--
 Table structure for table `card`
--


CREATE TABLE `card` (
  `CardID` int(100) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `BankName` varchar(50) NOT NULL,
  `URL` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `InterestRate` varchar(10) NOT NULL,
  `Cash withdrawal limit per transaction` varchar(50) NOT NULL,
  `Cash withdrawal limit per day` varchar(50) NOT NULL,
  `Credit limit max` varchar(50) NOT NULL,
  `International transaction` tinyint(1) NOT NULL,
  `Balance transfer available` tinyint(1) NOT NULL,
  `Dual currency` tinyint(1) NOT NULL,
  `Reward supplementary card` tinyint(1) NOT NULL,
  `Reward airport lounge` tinyint(1) NOT NULL,
  `Reward cashback available` tinyint(1) NOT NULL,
  `Reward luxury resort` tinyint(1) NOT NULL,
  `Reward insurance plan` tinyint(1) NOT NULL,
  `Reward travel benefit` tinyint(1) NOT NULL,
  `Reward fine dining` tinyint(1) NOT NULL,
  `Reward buffet discount` tinyint(1) NOT NULL,
  `Reward medical discount` tinyint(1) NOT NULL,
  `Reward shopping` tinyint(1) NOT NULL,
  `Reward airlines ticket` tinyint(1) NOT NULL,
  `Reward point program` tinyint(1) NOT NULL,
  `EMI available` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `card`
--


INSERT INTO `card` (`CardID`, `Name`, `BankName`, `URL`, `Type`, `InterestRate`, `Cash withdrawal limit per transaction`, `Cash withdrawal limit per day`, `Credit limit max`, `International transaction`, `Balance transfer available`, `Dual currency`, `Reward supplementary card`, `Reward airport lounge`, `Reward cashback available`, `Reward luxury resort`, `Reward insurance plan`, `Reward travel benefit`, `Reward fine dining`, `Reward buffet discount`, `Reward medical discount`, `Reward shopping`, `Reward airlines ticket`, `Reward point program`, `EMI available`) VALUES
(1, 'Sonali Debit Card', 'Sonali Bank Limited', 'https://www.sonalibank.com.bd/debit_Card.php', 'Debit', '0', '30000', '30000', 'N/A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(2, 'Janata Debit Card', 'Janata Bank Limited', 'http://www.janatabank-bd.com/atm-services/', 'Debit', '0', 'N/G', 'N/G', 'N/A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(5, 'Agrani Debit Card', 'Agrani Bank Limited ', 'https://www.agranibank.org/debit_card.php', 'Debit', '0', 'N/G', 'N/G', 'N/A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(6, 'Rupali Debit Card', 'Rupali Bank Limited', 'http://www.rupalibank.org/', 'Debit', '0', '20000', '50000', 'N/A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(7, 'Krishi Bank Debit Card', 'Bangladesh Krishi Bank', 'http://www.krishibank.org.bd/atm-service/', 'Debit', '0', '20000', '20000', 'N/A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(8, 'AB Bank Debit Card', 'AB Bank', 'http://abbl.com/ebiz/cards/debit-card/', 'Debit', '0', '200000', '300000', 'N/A', 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
(9, 'AB Bank World MasterCard', 'AB Bank', 'http://abbl.com/ebiz/cards/credit-card/world-maste', 'Credit', 'N/G', '500000', '500000', '1000000', 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1),
(10, 'AB Bank Titanium MasterCard', 'AB Bank', 'http://abbl.com/ebiz/cards/credit-card/titanium-ma', 'Credit', 'N/G', '500000', '500000', '1000000', 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1),
(11, 'AB Bank Gold MasterCard', 'AB Bank', 'http://abbl.com/ebiz/cards/credit-card/gold-card/', 'Credit', 'N/G', '250000', '250000', '500000', 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1);


--
-- Indexes for dumped tables
--

--
--
 Indexes for table `bank`
--

ALTER TABLE `bank`
  ADD PRIMARY KEY (`Bank_ID`);


--
-- Indexes for table `card`
--

ALTER TABLE `card`
  ADD KEY `ID` (`CardID`);


--
-- AUTO_INCREMENT for dumped tables
--

--
--
 AUTO_INCREMENT for table `bank`
--
ALTER TABLE `bank`
  MODIFY `Bank_ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;


--
-- AUTO_INCREMENT for table `card`
--

ALTER TABLE `card`
  MODIFY `CardID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
