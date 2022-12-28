select count(*) from mecze where Sety_wygrane + Sety_przegrane = 5;
select miasto, count(*) as c from mecze join kluby using(Id_klubu) group by miasto order by c desc;
select imie, nazwisko from sedziowie where Id_sedziego not in (select distinct Id_sedziego from mecze join kluby using(Id_klubu) where year(Data) = 2019 and (month(Data) = 11 or (month(Data) = 10 and Day(Data) >= 15) or (month(Data) = 12 and Day(Data) <= 15)) and (miasto = "Licowo" or miasto = "Szymbark"));
select count(*) from mecze;
select count(*) from sedziowie;
select 20.25 as srednia;
select imie, nazwisko from (select imie, nazwisko, count(*) as c from mecze join sedziowie using(Id_sedziego) group by Id_sedziego) as t where c > 20.25;
select nazwa, miasto, c_wyg, c_przeg from (select * from (select Id_klubu, count(*) as c_wyg from mecze where Sety_wygrane > Sety_przegrane group by Id_klubu) as wyg join (select Id_klubu, count(*) as c_przeg from mecze where Sety_wygrane < Sety_przegrane group by Id_klubu) as przeg using(Id_klubu) where c_wyg >= c_przeg) as t join kluby using(Id_klubu)
