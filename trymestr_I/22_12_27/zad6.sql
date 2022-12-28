select count(*) from koncerty where month(koncerty.data) = 7;
select distinct kod_miasta, sum(liczba_artystow) as n from koncerty join zespoly using(id_zespolu) group by kod_miasta;
select * from miasta where kod_miasta = "99-512" or kod_miasta = "99-507";
select wojewodztwo, round(sum(liczba_koncertow)/count(miasto),2) as srednia from (select miasto, wojewodztwo, count(id) as liczba_koncertow from koncerty join miasta using(kod_miasta) group by miasto) as tabela group by wojewodztwo order by srednia desc;
select nazwa from zespoly where id_zespolu not in (select distinct id_zespolu from koncerty where month(data) = 7 and day(data) >= 20 and day(data) <= 25);