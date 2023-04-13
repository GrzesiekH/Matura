-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 30 Mar 2023, 11:23
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `matura`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auta`
--

CREATE TABLE `auta` (
  `nr_rejestracyjny` varchar(5) DEFAULT NULL,
  `marka` varchar(8) DEFAULT NULL,
  `model` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `auta`
--

INSERT INTO `auta` (`nr_rejestracyjny`, `marka`, `model`) VALUES
('AA001', 'Citroen', 'Jumper'),
('AA002', 'Fiat', 'Ducato'),
('AA003', 'Citroen', 'Berlingo'),
('AA004', 'Ford', 'Transit'),
('AA005', 'Fiat', 'Ducato'),
('AA006', 'Iveco', 'Daily'),
('AA007', 'Ford', 'Transit'),
('AA008', 'Citroen', 'Jumper'),
('AA009', 'Mercedes', 'Vito'),
('AA010', 'Ford', 'Transit'),
('AA011', 'Citroen', 'Berlingo'),
('AA012', 'Fiat', 'Ducato'),
('AA013', 'Mercedes', 'Sprinter'),
('AA014', 'Citroen', 'Jumper'),
('AA015', 'Fiat', 'Ducato'),
('AA016', 'Mercedes', 'Vito'),
('AA017', 'Citroen', 'Berlingo'),
('AA018', 'Iveco', 'Daily'),
('AA019', 'Mercedes', 'Sprinter'),
('AA020', 'Citroen', 'Jumper'),
('AA021', 'Opel', 'Vivaro'),
('AA022', 'Mercedes', 'Sprinter'),
('AA023', 'Citroen', 'Berlingo'),
('AA024', 'Ford', 'Transit'),
('AA025', 'Iveco', 'Daily'),
('AA026', 'Mercedes', 'Sprinter'),
('AA027', 'Citroen', 'Jumper'),
('AA028', 'Fiat', 'Ducato'),
('AA029', 'Mercedes', 'Vito'),
('AA030', 'Ford', 'Transit');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `naprawy`
--

CREATE TABLE `naprawy` (
  `id_naprawy` varchar(3) DEFAULT NULL,
  `nazwa` varchar(36) DEFAULT NULL,
  `cena_materialow` int(4) DEFAULT NULL,
  `cena_roboczo_h` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `naprawy`
--

INSERT INTO `naprawy` (`id_naprawy`, `nazwa`, `cena_materialow`, `cena_roboczo_h`) VALUES
('p1', 'wymiana klocków hamulcowych', 360, 80),
('p2', 'wymiana tarcz hamulcowych', 432, 80),
('p3', 'wymiana paska klinowego', 50, 35),
('p4', 'wymina amortyzatora', 400, 90),
('p5', 'wymiana końcówki drążka', 35, 45),
('p6', 'wymiana koła pasowego wału korbowego', 130, 85),
('p7', 'wymiana filtra paliwa', 190, 35),
('p8', 'wymiana filtra powietrza', 100, 30),
('p9', 'wymiana filtra oleju', 55, 30),
('p10', 'wymiana filtra kabinowego', 136, 45),
('p11', 'wymiana chłodnicy silnika', 680, 85),
('p12', 'wymiana sprężyny zawieszenia', 420, 95),
('p13', 'wymiana panewek wału korbowego', 690, 130),
('p14', 'wymiana wachaczy', 1000, 110),
('p15', 'wymiana świec', 200, 70),
('p16', 'wymiana mechanizmu sprzęgła ', 1900, 155),
('p17', 'wymiana koła zamachowego dwumasowego', 1800, 140),
('p18', 'wymiana pompy spryskiwacza', 100, 75),
('p19', 'wymiana linki gazu', 145, 46),
('p20', 'wymiana pompy paliwa', 650, 84),
('p21', 'wymiana łożyska koła', 505, 135),
('p22', 'wymiana resora', 605, 145);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `serwis`
--

CREATE TABLE `serwis` (
  `nr_rejestracyjny` varchar(5) DEFAULT NULL,
  `id_naprawy` varchar(3) DEFAULT NULL,
  `czasnaprawy` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `serwis`
--

INSERT INTO `serwis` (`nr_rejestracyjny`, `id_naprawy`, `czasnaprawy`) VALUES
('AA001', 'p2', '2,76666666666667'),
('AA003', 'p9', '0,9'),
('AA004', 'p11', '2,5'),
('AA005', 'p6', '2,93333333333333'),
('AA006', 'p4', '2,78333333333333'),
('AA008', 'p16', '2,76666666666667'),
('AA009', 'p13', '2,71666666666667'),
('AA010', 'p4', '2,08333333333333'),
('AA011', 'p2', '1,75'),
('AA013', 'p5', '2,61666666666667'),
('AA014', 'p4', '0,683333333333333'),
('AA015', 'p15', '0,966666666666667'),
('AA016', 'p6', '1,31666666666667'),
('AA017', 'p3', '0,516666666666667'),
('AA019', 'p14', '2,2'),
('AA020', 'p1', '1,73333333333333'),
('AA021', 'p18', '0,516666666666667'),
('AA022', 'p7', '0,633333333333333'),
('AA024', 'p2', '2,41666666666667'),
('AA025', 'p6', '2,3'),
('AA026', 'p5', '2,25'),
('AA027', 'p11', '1,68333333333333'),
('AA028', 'p7', '0,566666666666667'),
('AA029', 'p4', '2,51666666666667'),
('AA019', 'p19', '0,616666666666667'),
('AA001', 'p19', '0,9'),
('AA005', 'p12', '2,06666666666667'),
('AA006', 'p8', '0,55'),
('AA007', 'p2', '1,98333333333333'),
('AA008', 'p2', '1,3'),
('AA009', 'p6', '1,33333333333333'),
('AA010', 'p5', '2,58333333333333'),
('AA011', 'p19', '1,11666666666667'),
('AA013', 'p8', '0,866666666666667'),
('AA014', 'p15', '0,916666666666667'),
('AA015', 'p18', '0,516666666666667'),
('AA016', 'p8', '0,75'),
('AA017', 'p15', '0,866666666666667'),
('AA018', 'p2', '2,68333333333333'),
('AA019', 'p16', '2,76666666666667'),
('AA020', 'p5', '1,43333333333333'),
('AA021', 'p19', '1,35'),
('AA022', 'p18', '1,01666666666667'),
('AA024', 'p10', '0,6'),
('AA025', 'p16', '2,53333333333333'),
('AA026', 'p6', '2,35'),
('AA027', 'p13', '1,63333333333333'),
('AA028', 'p4', '2,3'),
('AA029', 'p12', '1,7'),
('AA030', 'p5', '2,18333333333333'),
('AA001', 'p18', '1,11666666666667'),
('AA002', 'p8', '0,783333333333333'),
('AA003', 'p13', '1,71666666666667'),
('AA004', 'p1', '0,866666666666667'),
('AA005', 'p15', '0,616666666666667'),
('AA006', 'p2', '1,88333333333333'),
('AA007', 'p4', '2,43333333333333'),
('AA008', 'p18', '0,7'),
('AA009', 'p12', '2,33333333333333'),
('AA010', 'p3', '0,7'),
('AA011', 'p1', '1,46666666666667'),
('AA012', 'p14', '1,78333333333333'),
('AA013', 'p20', '1,61666666666667'),
('AA014', 'p11', '1,88333333333333'),
('AA015', 'p3', '0,983333333333333'),
('AA016', 'p2', '1,3'),
('AA017', 'p13', '2,2'),
('AA018', 'p15', '0,516666666666667'),
('AA019', 'p11', '2,21666666666667'),
('AA020', 'p7', '0,933333333333333'),
('AA021', 'p5', '1,35'),
('AA022', 'p2', '1,6'),
('AA019', 'p3', '0,383333333333333'),
('AA024', 'p22', '2,1'),
('AA025', 'p11', '1,9'),
('AA026', 'p20', '1,6'),
('AA027', 'p2', '2,05'),
('AA028', 'p22', '2,25'),
('AA029', 'p20', '1,53333333333333'),
('AA030', 'p15', '0,85'),
('AA001', 'p15', '0,75'),
('AA002', 'p19', '1,03333333333333'),
('AA003', 'p17', '2,7'),
('AA004', 'p21', '2,5'),
('AA005', 'p8', '0,833333333333333'),
('AA006', 'p8', '0,6'),
('AA007', 'p22', '2,65'),
('AA008', 'p7', '0,766666666666667'),
('AA009', 'p3', '0,616666666666667'),
('AA010', 'p6', '1,8'),
('AA011', 'p4', '2,86666666666667'),
('AA012', 'p13', '1,66666666666667'),
('AA013', 'p21', '2,68333333333333'),
('AA014', 'p22', '2,13333333333333'),
('AA015', 'p11', '0,966666666666667'),
('AA016', 'p10', '0,583333333333333'),
('AA017', 'p21', '0,633333333333333'),
('AA019', 'p3', '1,43333333333333'),
('AA019', 'p6', '2,81666666666667'),
('AA020', 'p13', '2,71666666666667'),
('AA021', 'p19', '1,21666666666667'),
('AA022', 'p13', '2,7'),
('AA019', 'p9', '1,13333333333333'),
('AA024', 'p13', '1,71666666666667'),
('AA025', 'p22', '2,83333333333333'),
('AA026', 'p22', '2,76666666666667'),
('AA027', 'p10', '0,716666666666667'),
('AA028', 'p19', '0,983333333333333'),
('AA029', 'p8', '0,6'),
('AA030', 'p5', '1,95'),
('AA001', 'p9', '1'),
('AA002', 'p14', '2,21666666666667'),
('AA003', 'p8', '0,45'),
('AA004', 'p5', '1,8'),
('AA005', 'p7', '0,716666666666667'),
('AA006', 'p5', '1,75'),
('AA007', 'p21', '2,35'),
('AA008', 'p4', '1,91666666666667'),
('AA009', 'p11', '2,1'),
('AA010', 'p12', '2,11666666666667'),
('AA019', 'p9', '0,683333333333333'),
('AA012', 'p8', '0,533333333333333'),
('AA013', 'p1', '1,35'),
('AA014', 'p3', '0,816666666666667'),
('AA015', 'p8', '0,816666666666667'),
('AA016', 'p2', '2,7'),
('AA017', 'p15', '0,533333333333333'),
('AA018', 'p9', '0,583333333333333'),
('AA019', 'p13', '2,83333333333333'),
('AA020', 'p10', '0,683333333333333'),
('AA021', 'p11', '1,66666666666667'),
('AA022', 'p7', '0,566666666666667'),
('AA019', 'p21', '2,4'),
('AA024', 'p2', '1,66666666666667'),
('AA025', 'p21', '2,83333333333333'),
('AA026', 'p12', '2,45'),
('AA027', 'p22', '2,36666666666667'),
('AA028', 'p17', '1,76666666666667'),
('AA029', 'p1', '0,8'),
('AA030', 'p6', '1,81666666666667'),
('AA001', 'p3', '0,983333333333333'),
('AA002', 'p1', '1,66666666666667'),
('AA003', 'p13', '1,83333333333333'),
('AA019', 'p9', '0,55'),
('AA005', 'p5', '1,91666666666667'),
('AA006', 'p18', '0,666666666666667'),
('AA007', 'p12', '2,98333333333333'),
('AA008', 'p17', '2,58333333333333'),
('AA009', 'p5', '1,95'),
('AA010', 'p11', '2,88333333333333'),
('AA011', 'p18', '0,95'),
('AA012', 'p17', '2,76666666666667'),
('AA013', 'p17', '2,81666666666667'),
('AA014', 'p8', '0,766666666666667'),
('AA015', 'p16', '2,05'),
('AA016', 'p18', '0,683333333333333'),
('AA017', 'p18', '0,65'),
('AA018', 'p4', '1,96666666666667'),
('AA019', 'p17', '2,21666666666667'),
('AA020', 'p5', '2,55'),
('AA021', 'p21', '2,16666666666667'),
('AA022', 'p21', '2,56666666666667'),
('AA019', 'p9', '0,95'),
('AA024', 'p12', '1,98333333333333'),
('AA025', 'p13', '2,21666666666667'),
('AA026', 'p17', '2,13333333333333'),
('AA027', 'p22', '1,88333333333333'),
('AA028', 'p9', '0,883333333333333'),
('AA029', 'p10', '0,7'),
('AA030', 'p1', '0,8');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
