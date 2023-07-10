-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 30 Haz 2021, 21:55:48
-- Sunucu sürümü: 10.4.18-MariaDB
-- PHP Sürümü: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `gorsel2`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktor`
--

CREATE TABLE `doktor` (
  `id` int(11) NOT NULL,
  `ad` varchar(40) COLLATE utf8_turkish_ci NOT NULL,
  `soyad` varchar(40) COLLATE utf8_turkish_ci NOT NULL,
  `mail` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `password` varchar(16) COLLATE utf8_turkish_ci NOT NULL,
  `alanı` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `tc_kimlik` varchar(11) COLLATE utf8_turkish_ci NOT NULL,
  `search_name` varchar(50) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `doktor`
--

INSERT INTO `doktor` (`id`, `ad`, `soyad`, `mail`, `password`, `alanı`, `tc_kimlik`, `search_name`) VALUES
(1, 'Emirhan', 'acar', 'emrhn_16@hotmail.com', 'acaremir', 'Çocuk_Sağlığı_ve_Hastalıkları', '10003941075', 'emirhan_acar'),
(2, 'Abdurrahman', 'Yılmaz', 'furkan@gmail.com', '258369', 'Enfeksiyon_astalıkları', '23210313187', 'abdurrahman_yılmaz'),
(3, 'Hulya', 'Sali', 'salihulya15@gmail.com', '147258', 'Fiziksel_Tıp_ve_Rehabilitasyon', '38117112032', 'Hulya_sali'),
(4, 'Fatih', 'Yıldırım', 'fatih@gmail.com', 'fatih55', 'Çocuk_Sağlığı_ve_Hastalıkları', '25417854725', 'fatih_yıldırım'),
(5, 'Efe', 'Kalkan', 'kalkan@gmail.com', 'kalkan54', 'Genel_Cerrahi', '12485964587', 'efe_kalkan'),
(6, 'Pelin', 'Korkmaz', 'korkmaz@gmail.com', 'korkmaz15', 'Göz_Hastalıkları', '47517468514', 'pelin_korkmaz'),
(7, 'Fikri', 'Fazlı', 'fazlı@gmail.com', 'fikri25', 'Psikiyatri', '12479547852', 'fikri_fazlı'),
(8, 'Emre', 'Keskin', 'keskin@gmail.com', 'emre754', 'Kulak_Burun_Boğaz_Hastalıkları', '54712457896', 'emre_keskin'),
(9, 'İsmail', 'Mutlu', 'ismail@gmail.com', 'ismail16', 'Kardiyoloji', '25415974875', 'ismail_mutlu'),
(10, 'Yasin', 'Yurt', 'yasin@gmail.com', 'yasin25', 'Anesteziyoloji_ve_Reanimasyon', '65796452874', 'yasin_yurt'),
(11, 'Yunus', 'Mert', 'yunus@gmail.com', 'yunus65', 'Deri_ve_zührevi_Hastalıkları', '54769721436', 'yunus_mert'),
(12, 'Cansu', 'Ersoy', 'cansu@gmail.com', 'cansuersoy12', 'Göğüs_Hastalıkları', '74567124862', 'cansu_ersoy'),
(13, 'Ceyda', 'Yazar', 'ceyda@gmail.com', 'ceyda3613', 'İç_Hastalıklar', '34679852476', 'ceyda_yazar'),
(14, 'Eda', 'Terzi', 'eda@gmail.com', 'eda44', 'Kadın_Hastalıkları_ve_Doğum', '74584125476', 'eda_terzi'),
(15, 'Mehmet', 'Dursun', 'mehmet@gmail.com', 'mehmet3341', 'Üroloji', '64157954821', 'mehmet_dursun'),
(16, 'Enes', 'Yontar', 'enes@gmail.com', 'enes2286', 'Ortopedi_ve_Travmaloji', '2175463521', 'enes_yontar');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hasta`
--

CREATE TABLE `hasta` (
  `id` int(11) NOT NULL,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `tckimlik` varchar(11) NOT NULL,
  `cinsiyet` enum('Erkek','Kadın','Diğer') NOT NULL,
  `kan` varchar(30) NOT NULL,
  `dogumyeri` varchar(50) NOT NULL,
  `dogumtarihi` date NOT NULL,
  `baba_adı` varchar(50) NOT NULL,
  `anne_adı` varchar(50) NOT NULL,
  `numara` varchar(11) NOT NULL,
  `eposta` varchar(50) NOT NULL,
  `sifre` varchar(20) NOT NULL,
  `adres` varchar(250) NOT NULL,
  `recete` varchar(50) NOT NULL,
  `tanı` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `hasta`
--

INSERT INTO `hasta` (`id`, `ad`, `soyad`, `tckimlik`, `cinsiyet`, `kan`, `dogumyeri`, `dogumtarihi`, `baba_adı`, `anne_adı`, `numara`, `eposta`, `sifre`, `adres`, `recete`, `tanı`) VALUES
(12, 'Duygu', 'Mutlu', '45621736915', 'Kadın', 'AB_Rh_negatif', 'İzmir', '1993-02-16', 'Nazım', 'Senay', '05348743215', 'duygu@gmail.com', 'duyguduygu', 'Bursa/Osmangazi', '', ''),
(15, 'Mertcan', 'göz', '65478925834', 'Erkek', 'A_Rh_pozitif', 'İstanbul', '2000-10-13', 'Faith', 'Edanur', '05481545', 'mertcan@gmail.com', 'mert', 'Bursa/Gemlik', '', ''),
(47, 'Kadir', 'Barbaros', '54721576354', 'Erkek', 'A_Rh_negatif', 'Erzurum', '2000-07-11', 'Safa', 'Didem', '05492674851', 'kadir@gmail.com', 'kadir012', 'Bursa/Yıldırım', '', ''),
(48, 'Remzi', 'Bilgi', '10003457815', 'Erkek', '0_RH_Pozitif', 'Antalya', '1964-11-23', 'Altan', 'Ayseren', '05482493674', 'remzi@gmail.com', 'remzi1964', 'Bursa/Orhangazi', '', ''),
(49, 'Sena', 'Candan', '64257315724', 'Kadın', 'B_Rh_pozitif', 'Balıkesir', '1995-05-17', 'Aydın', 'Elvan', '05342486472', 'sena@gmail.com', 'sena1616', 'Bursa/Kestel', '', '');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanıcı1`
--

CREATE TABLE `kullanıcı1` (
  `id` int(11) NOT NULL,
  `ad` varchar(40) NOT NULL,
  `soyad` varchar(40) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `kullanıcı1`
--

INSERT INTO `kullanıcı1` (`id`, `ad`, `soyad`, `email`, `password`) VALUES
(1, 'Ayşe', 'Bilir', 't', 't'),
(3, 'Ece', 'Derya', 'ece@gmail.com', 'ece548'),
(4, 'Ziya', 'Devrim', 'ziya@gmail.com', 'ziya6679');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanıcı2`
--

CREATE TABLE `kullanıcı2` (
  `id` int(11) NOT NULL,
  `ad` varchar(40) NOT NULL,
  `soyad` varchar(40) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(16) NOT NULL,
  `search_name` varchar(50) NOT NULL,
  `tckimlik` varchar(11) NOT NULL,
  `yas` int(3) NOT NULL,
  `cinsiyet` enum('Erkek','Kadın','Diğer') NOT NULL,
  `numara` varchar(11) NOT NULL,
  `recete` varchar(200) NOT NULL,
  `teshis` varchar(50) NOT NULL,
  `hekim` varchar(50) NOT NULL,
  `Klinik` enum('Anesteziyoloji ve Reanimasyon','Çocuk Sağlığı ve Hastalıkları','Deri ve Zührevi Hastalıkları','Diş Hekimliği','Enfeksiyon Hastalıkları','Fiziksel Tıp ve Rehabilitasyon','Genel Cerrahi','Göğüs Hastalıkları','Göz Hastalıkları','İç Hastalıklar','Kadın Hastalıkları ve Doğum','Kardiyoloji','Kulak Burun Boğaz Hastalıkları','Nöroloji','Ortopedi ve Travmaloj','Psikiyatri','Sağlık Kurulu','Üroloji') NOT NULL,
  `teshis_tarihi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `kullanıcı2`
--

INSERT INTO `kullanıcı2` (`id`, `ad`, `soyad`, `email`, `password`, `search_name`, `tckimlik`, `yas`, `cinsiyet`, `numara`, `recete`, `teshis`, `hekim`, `Klinik`, `teshis_tarihi`) VALUES
(1, 'Abdurrahman', 'Yılmaz', 'a@gmail.com', 'abdu', 'abdurrahman yılmaz', '12345678910', 23, 'Erkek', '05115485684', '0', '0', '', '', ''),
(2, 'murat', 'demir', 'mrtdmr@gmail.com', '1234', 'murat demir', '12234851756', 16, 'Erkek', '05279425486', '0', '0', '', '', ''),
(3, 'ayşe', 'demir', 'ays@gmail.com', '1234', 'ayşe demir', '45257889451', 18, 'Kadın', '05782845255', '0', '0', '', '', ''),
(4, 'mert', 'oz', 'mertoz@gmail.com', '1234', 'mert oz', '48245486945', 27, 'Erkek', '05147547511', '0', '0', '', '', ''),
(5, 'ilayda', 'burc', 'ilyada@gmail.com', '1234', 'ilayda burc', '54448764215', 52, 'Kadın', '05746742159', '0', '0', '', '', '');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `muayenetablosu`
--

CREATE TABLE `muayenetablosu` (
  `id` int(11) NOT NULL,
  `hasta_adı` varchar(50) NOT NULL,
  `hasta_soyadı` varchar(50) NOT NULL,
  `tc_kimlik` varchar(11) NOT NULL,
  `klinik` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `randevulist`
--

CREATE TABLE `randevulist` (
  `randevu_id` int(11) NOT NULL,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `tckimlik` varchar(11) NOT NULL,
  `klinik` varchar(50) NOT NULL,
  `doktorname` varchar(50) NOT NULL,
  `randevu_tarih` varchar(20) NOT NULL,
  `randevu_saat` varchar(8) NOT NULL,
  `hasta_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `randevulist`
--

INSERT INTO `randevulist` (`randevu_id`, `ad`, `soyad`, `tckimlik`, `klinik`, `doktorname`, `randevu_tarih`, `randevu_saat`, `hasta_id`) VALUES
(60, 'Duygu', 'Mutlu', '88888888', 'Çocuk_Sağlığı_ve_Hastalıkları', 'emirhan acar', '2021 - Şubat - 02', '10.00', 12),
(62, 'Duygu', 'Mutlu', '88888888', 'Çocuk_Sağlığı_ve_Hastalıkları', 'emirhan acar', '2021 - Haziran - 03', '14.00', 12),
(63, 'DuyguDuygu', 'MutluMutlu', '88888888888', 'Çocuk_Sağlığı_ve_Hastalıkları', 'emirhan acar', '2021 - Mart - 03', '15.00', 1212),
(65, 'DuyguDuygu', 'MutluMutlu', '88888888888', 'Çocuk_Sağlığı_ve_Hastalıkları', 'emirhan acar', '2021 - Mayıs - 04', '16.00', 1212),
(67, 'DuyguDuygu', 'MutluMutlu', '88888888888', 'Çocuk_Sağlığı_ve_Hastalıkları', 'emirhan acar', '2021 - Ocak - 04', '11.00', 1212),
(76, 'Duygu', 'Mutlu', '88888888', 'Çocuk_Sağlığı_ve_Hastalıkları', 'emirhan acar', '2021 - Nisan - 03', '12.00', 12);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tanıverecete`
--

CREATE TABLE `tanıverecete` (
  `id` int(11) NOT NULL,
  `hasta_adı` varchar(50) NOT NULL,
  `soyadı` varchar(50) NOT NULL,
  `tckimlik` varchar(11) NOT NULL,
  `tanı` text NOT NULL,
  `recete` text NOT NULL,
  `klinik` varchar(50) NOT NULL,
  `randevu_tarih` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `tanıverecete`
--

INSERT INTO `tanıverecete` (`id`, `hasta_adı`, `soyadı`, `tckimlik`, `tanı`, `recete`, `klinik`, `randevu_tarih`) VALUES
(14, 'emir', 'adada', '1234512345', 'kalk kalk\n', 'bişeyi yok bunun\n', '{Çocuk_Sağlığı_ve_Hastalıkları}', ''),
(15, '', '', '13123', 'ekmdkedmke\n', 'amsd masd asd\n', '', ''),
(16, 'emir', 'adada', '1234512345', 'asjdnalksmdaşksdmaşskda\n', '\n', '{Çocuk_Sağlığı_ve_Hastalıkları}', ''),
(17, 'fjgfhfghdgf', 'fgjfdx', '12345123451', 'dddddddd\n', 'ffffffffffff\n', 'Çocuk_Sağlığı_ve_Hastalıkları', ''),
(27, 'Duygu', 'Mutlu', '33333333', 'errrrrrrrrrr\n', 'tettttttttt\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{{2020 - Temmuz - 05}}'),
(28, 'Duygu', 'Mutlu', '33333333', 'bu salak\n', 'dua edin düzelsin\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Temmuz - 05}'),
(29, 'Duygu', 'Mutlu', '33333333', 'ggggggggg\n', 'mmmmmmmmmmmm\n', '', ''),
(30, 'Duygu', 'Mutlu', '88888888', 'sorun yok\n', 'bos\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Temmuz - 05}'),
(31, 'Duygu', 'Mutlu', '88888888', 'yaşamaz\n', 'parol,gaviscon(öylesine)\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Temmuz - 05}'),
(32, 'Duygu', 'Mutlu', '88888888', 'dsfsdfsdf	\n', 'sdfsfsdf\n', '', ''),
(33, 'Duygu', 'Mutlu', '88888888', 'afasasd	\n', 'sssdsd\n', '', ''),
(34, 'abdü', 'yılmaz', '147258', 'vertigo\n', 'geçimiş olsun, yaşamaz bu\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2021 - Temmuz - 08}'),
(35, 'Duygu', 'Mutlu', '88888888', 'aodkfasofd\n', 'aospdkjaosd\n', '', ''),
(36, 'Mertcan', 'dem', '3', 'rthgytredgh\n', 'frhfgh\n', '', ''),
(37, '', '', '13579', 'dsfgfdg\n', 'fsdgdfg\n', '', ''),
(38, 'Duygu', 'Mutlu', '88888888', 'fcxvbgxscfvcx\n', 'dfgvdsxfvdxs\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}'),
(39, 'Duygu', 'Mutlu', '88888888', 'asdfasdsa\n', 'asdad\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}'),
(40, 'Duygu', 'Mutlu', '88888888', 'asdsa\n', 'asdasdas\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}'),
(41, 'Duygu', 'Mutlu', '88888888', '\n', '\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}{2020 - Nis'),
(42, 'Duygu', 'Mutlu', '88888888', '\n', '\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}'),
(43, 'Duygu', 'Mutlu', '88888888', 'asdasd\n', 'asdas\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}{2020 - Nis'),
(44, 'Duygu', 'Mutlu', '88888888', 'saqedsad\n', 'asdasd\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2020 - Nisan - 03}'),
(45, 'Duygu', 'Mutlu', '88888888', 'asdasd	sada\n', 'dasdavavc\n', '', ''),
(46, 'Duygu', 'Mutlu', '88888888', 'adjfikadf	\n', 'jdfkadfmasd\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2021 - Şubat - 02}'),
(47, 'Duygu', 'Mutlu', '88888888', 'aklsndklasdlksandklas\n', 'klasnsadlasd\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2021 - Şubat - 02}{2021 - Şub'),
(48, 'Duygu', 'Mutlu', '88888888', 'adasdas\n', 'asdasdas\n', 'Çocuk_Sağlığı_ve_Hastalıkları', '{2021 - Şubat - 02}'),
(49, 'Duygu', 'Mutlu', '45621736915', 'ıpdğsajhsıdpgv\n', 'dafdsoıgfhndsaıpf\n', 'Fiziksel_Tıp_ve_Rehabilitasyon', '{2021 - Mart - 04}');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `doktor`
--
ALTER TABLE `doktor`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `hasta`
--
ALTER TABLE `hasta`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kullanıcı1`
--
ALTER TABLE `kullanıcı1`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kullanıcı2`
--
ALTER TABLE `kullanıcı2`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `muayenetablosu`
--
ALTER TABLE `muayenetablosu`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `randevulist`
--
ALTER TABLE `randevulist`
  ADD PRIMARY KEY (`randevu_id`);

--
-- Tablo için indeksler `tanıverecete`
--
ALTER TABLE `tanıverecete`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `doktor`
--
ALTER TABLE `doktor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Tablo için AUTO_INCREMENT değeri `hasta`
--
ALTER TABLE `hasta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- Tablo için AUTO_INCREMENT değeri `kullanıcı1`
--
ALTER TABLE `kullanıcı1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `kullanıcı2`
--
ALTER TABLE `kullanıcı2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `muayenetablosu`
--
ALTER TABLE `muayenetablosu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Tablo için AUTO_INCREMENT değeri `randevulist`
--
ALTER TABLE `randevulist`
  MODIFY `randevu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- Tablo için AUTO_INCREMENT değeri `tanıverecete`
--
ALTER TABLE `tanıverecete`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
