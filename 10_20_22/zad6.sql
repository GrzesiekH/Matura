select kraj, count(*) as liczba from gracze where year(data_dolaczenia) = 2018 group by kraj order by liczba desc limit 5;
select nazwa, sum(strzal) from jednostki inner join klasy using(nazwa) where nazwa like "%elf%" group by nazwa;
select id_gracza from gracze where id_gracza not in (select distinct id_gracza from jednostki where nazwa like "artylerzysta") order by id_gracza asc;
select nazwa, count(*) from jednostki inner join klasy using(nazwa) where abs(lok_x - 100) + abs(lok_y - 100) <= szybkosc group by nazwa;
select * from jednostki as j1 inner join jednostki as j2 using(lok_x, lok_y) where j1.id_gracza != j2.id_gracza group by lok_x, lok_y limit 100000; -- A)
select * from (select * from jednostki join gracze using(id_gracza)) as j1 join (select * from jednostki join gracze using(id_gracza)) as j2 using (lok_x, lok_y) where j1.id_gracza != j2.id_gracza and (j2.kraj like "Polska" or j1.kraj like "Polska") group by lok_x, lok_y limit 10000 -- B) 