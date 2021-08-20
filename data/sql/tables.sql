-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql6.freemysqlhosting.net
-- Generation Time: Aug 18, 2021 at 06:53 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql6430075`
--
CREATE DATABASE IF NOT EXISTS `sql6430075` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sql6430075`;

-- --------------------------------------------------------

--
-- Table structure for table `dim_Date`
--

CREATE TABLE `dim_Date` (
  `Date_Key` int(11) NOT NULL,
  `Date_Text` varchar(20) DEFAULT NULL,
  `Day_Name` varchar(20) DEFAULT NULL,
  `Month_Name` varchar(20) NOT NULL,
  `Month_Number` int(11) NOT NULL,
  `Year` int(11) NOT NULL,
  `IsHoliday_NSW` tinyint(1) NOT NULL,
  `IsHoliday_VIC` tinyint(1) NOT NULL,
  `IsHoliday_QLD` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dim_Date`
--

INSERT INTO `dim_Date` (`Date_Key`, `Date_Text`, `Day_Name`, `Month_Name`, `Month_Number`, `Year`, `IsHoliday_NSW`, `IsHoliday_VIC`, `IsHoliday_QLD`) VALUES
(20200620, '20/06/2021', 'Sunday', 'June', 6, 2021, 1, 1, 1),
(20200621, '21/06/2021', 'Monday', 'June', 6, 2021, 0, 0, 0),
(20200622, '22/06/2021', 'Tuesday', 'June', 6, 2021, 0, 0, 0),
(20210614, '14/06/2021', 'Monday', 'June', 6, 2021, 1, 1, 0),
(20210615, '15/06/2021', 'Tuesday', 'June', 6, 2021, 0, 0, 0),
(20210616, '16/06/2021', 'Wednesday', 'June', 6, 2021, 0, 0, 0),
(20210617, '17/06/2021', 'Thursday', 'June', 6, 2021, 0, 0, 0),
(20210618, '18/06/2021', 'Friday', 'June', 6, 2021, 0, 0, 0),
(20210619, '19/06/2021', 'Saturday', 'June', 6, 2021, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `dim_Department`
--

CREATE TABLE `dim_Department` (
  `Department_Key` int(11) NOT NULL,
  `Department_Name` varchar(50) NOT NULL,
  `Department_Location` varchar(250) NOT NULL,
  `Front_Desk_Phone` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dim_Department`
--

INSERT INTO `dim_Department` (`Department_Key`, `Department_Name`, `Department_Location`, `Front_Desk_Phone`) VALUES
(311001, 'Bondi Branch', '111 X Road, Bondi Junction', '02-90000000'),
(311007, 'Burwood Branch', '333 Z Road, Burwood', '02-90000009'),
(311025, 'North Sydney Branch', '222 Y Road, North Sydney', '02-90000002'),
(311123, 'Chatswood Branch', '444 A Road, Chatswood', '02-90000004'),
(311345, 'Blacktown Branch', '555 B Road, Blacktown', '02-90000007');

-- --------------------------------------------------------

--
-- Table structure for table `dim_Maintenance_Job`
--

CREATE TABLE `dim_Maintenance_Job` (
  `Maintenance_Job_Key` int(11) NOT NULL,
  `Maintenance_Job_TypeCode` varchar(50) NOT NULL,
  `Maintenance_Job_Desc` varchar(255) NOT NULL,
  `IsHoliday` tinyint(1) NOT NULL,
  `HourRate` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dim_Maintenance_Job`
--

INSERT INTO `dim_Maintenance_Job` (`Maintenance_Job_Key`, `Maintenance_Job_TypeCode`, `Maintenance_Job_Desc`, `IsHoliday`, `HourRate`) VALUES
(562341, 'MTSCNS', 'Software configuration and network set up', 1, 100),
(562342, 'MTSCNS', 'Software configuration and network set up', 0, 80),
(562343, 'MTCCW', 'Changing copper wire', 1, 120),
(562344, 'MTCCW', 'Changing copper wire', 0, 100),
(562345, 'MTBTR', 'Battery replacement', 1, 80),
(562346, 'MTBTR', 'Battery replacement', 0, 70),
(562347, 'MTCFOC', 'Connection of fiber optical cable', 1, 120);

-- --------------------------------------------------------

--
-- Table structure for table `dim_Staff`
--

CREATE TABLE `dim_Staff` (
  `Staff_ID` int(20) NOT NULL,
  `Natural key Staff_ID` varchar(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Contact phone` varchar(20) NOT NULL,
  `Home address` varchar(250) NOT NULL,
  `Email address` varchar(50) NOT NULL,
  `Department` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dim_Staff`
--

INSERT INTO `dim_Staff` (`Staff_ID`, `Natural key Staff_ID`, `Name`, `Contact phone`, `Home address`, `Email address`, `Department`) VALUES
(211001, '010101', 'John Smith', '0415-222-555', '111 X Street, North Sydney', 'John.Smith@TelcoXYZ.com.au', 'Bondi'),
(211082, '020102', 'Bob Wong', '0424-111-222', '222 Y level Sydney Tower', 'Bob.Wong@TelcoXYZ.com.au', 'Bondi'),
(211105, '030102', 'Ann Li', '0411-111-222', '333 Z street Burwood', 'Ann.Li@TelcoXYZ.com.au', 'North Sydney');

-- --------------------------------------------------------

--
-- Table structure for table `dim_Travel_Allowance_Policy`
--

CREATE TABLE `dim_Travel_Allowance_Policy` (
  `Travel_Allowance_Policy_Key` int(11) NOT NULL,
  `Travel_Allowance_Policy_ID` varchar(20) NOT NULL,
  `Vehicle_Type` varchar(20) NOT NULL,
  `Allowance_per_km` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dim_Travel_Allowance_Policy`
--

INSERT INTO `dim_Travel_Allowance_Policy` (`Travel_Allowance_Policy_Key`, `Travel_Allowance_Policy_ID`, `Vehicle_Type`, `Allowance_per_km`) VALUES
(411111, 'TAPMT', 'motorcycles', 0.52),
(411234, 'TAP4WD', '4WD', 0.85),
(411321, 'TAPSD', 'SEDAN', 0.72),
(411654, 'TAPUV', 'utility vehicle', 0.82);

-- --------------------------------------------------------

--
-- Table structure for table `dim_Weather_Allowance_Policy`
--

CREATE TABLE `dim_Weather_Allowance_Policy` (
  `Weather_Allowance_Policy_Key` int(11) NOT NULL,
  `Policy_Key` varchar(20) NOT NULL,
  `Weather` varchar(20) NOT NULL,
  `Temperature` varchar(20) NOT NULL,
  `Weather_Allowance` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dim_Weather_Allowance_Policy`
--

INSERT INTO `dim_Weather_Allowance_Policy` (`Weather_Allowance_Policy_Key`, `Policy_Key`, `Weather`, `Temperature`, `Weather_Allowance`) VALUES
(612345, 'WAHRH', 'HeavyRain', 'High', 200),
(613568, 'WASCL', 'SunnyCloud', 'Low', 100),
(623552, 'WAHRN', 'HeavyRain', 'Normal', 200),
(646785, 'WARN', 'Rain', 'Normal', 80),
(654321, 'WAHRL', 'HeavyRain', 'Low', 200),
(675433, 'WASL', 'Snow', 'Low', 120),
(675445, 'WASCL', 'SunnyCloud', 'High', 100),
(677899, 'WARH', 'Rain', 'High', 120),
(678345, 'WASCN', 'SunnyCloud', 'Normal', 0),
(678543, 'WARL', 'Rain', 'Low', 120);

-- --------------------------------------------------------

--
-- Table structure for table `fact_Maintenance_Contractor_Payment`
--

CREATE TABLE `fact_Maintenance_Contractor_Payment` (
  `Payment_ID` int(11) NOT NULL,
  `Date_Key` int(11) NOT NULL,
  `Maintenance_Job_Key` int(11) NOT NULL,
  `Staff_Key` int(11) NOT NULL,
  `Department_Key` int(11) NOT NULL,
  `Travel_Allowance_Policy_Key` int(11) NOT NULL,
  `Weather_Allowance_Policy_Key` int(11) NOT NULL,
  `Maintenance_Hours` double NOT NULL,
  `Holiday_Payment` double NOT NULL,
  `Length_of_Travel` double NOT NULL,
  `Travel_Allowance_Amount` double NOT NULL,
  `Weather_Condition` varchar(20) NOT NULL,
  `Weather_Allowance_Amount` double NOT NULL,
  `Total_Amount_Paid` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dim_Date`
--
ALTER TABLE `dim_Date`
  ADD PRIMARY KEY (`Date_Key`);

--
-- Indexes for table `dim_Department`
--
ALTER TABLE `dim_Department`
  ADD PRIMARY KEY (`Department_Key`);

--
-- Indexes for table `dim_Maintenance_Job`
--
ALTER TABLE `dim_Maintenance_Job`
  ADD PRIMARY KEY (`Maintenance_Job_Key`);

--
-- Indexes for table `dim_Staff`
--
ALTER TABLE `dim_Staff`
  ADD PRIMARY KEY (`Staff_ID`);

--
-- Indexes for table `dim_Travel_Allowance_Policy`
--
ALTER TABLE `dim_Travel_Allowance_Policy`
  ADD PRIMARY KEY (`Travel_Allowance_Policy_Key`);

--
-- Indexes for table `dim_Weather_Allowance_Policy`
--
ALTER TABLE `dim_Weather_Allowance_Policy`
  ADD PRIMARY KEY (`Weather_Allowance_Policy_Key`);

--
-- Indexes for table `fact_Maintenance_Contractor_Payment`
--
ALTER TABLE `fact_Maintenance_Contractor_Payment`
  ADD PRIMARY KEY (`Payment_ID`),
  ADD KEY `FK_DATE_KEY` (`Date_Key`),
  ADD KEY `FK_M_J_KEY` (`Maintenance_Job_Key`),
  ADD KEY `Department_Key` (`Department_Key`),
  ADD KEY `FK_T_A_P_KEY` (`Travel_Allowance_Policy_Key`),
  ADD KEY `FK_W_A_P_KEY` (`Weather_Allowance_Policy_Key`),
  ADD KEY `FK_STAFF_KEY` (`Staff_Key`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fact_Maintenance_Contractor_Payment`
--
ALTER TABLE `fact_Maintenance_Contractor_Payment`
  ADD CONSTRAINT `FK_STAFF_KEY` FOREIGN KEY (`Staff_Key`) REFERENCES `dim_Staff` (`Staff_ID`),
  ADD CONSTRAINT `fact_Maintenance_Contractor_Payment_ibfk_1` FOREIGN KEY (`Department_Key`) REFERENCES `dim_Department` (`Department_Key`),
  ADD CONSTRAINT `FK_DATE_KEY` FOREIGN KEY (`Date_Key`) REFERENCES `dim_Date` (`Date_Key`),
  ADD CONSTRAINT `FK_M_J_KEY` FOREIGN KEY (`Maintenance_Job_Key`) REFERENCES `dim_Maintenance_Job` (`Maintenance_Job_Key`),
  ADD CONSTRAINT `FK_T_A_P_KEY` FOREIGN KEY (`Travel_Allowance_Policy_Key`) REFERENCES `dim_Travel_Allowance_Policy` (`Travel_Allowance_Policy_Key`),
  ADD CONSTRAINT `FK_W_A_P_KEY` FOREIGN KEY (`Weather_Allowance_Policy_Key`) REFERENCES `dim_Weather_Allowance_Policy` (`Weather_Allowance_Policy_Key`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
