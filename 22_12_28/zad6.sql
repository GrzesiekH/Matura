select count(*) from dane_ankiet where imie like '%a';
select count(*) from dane_ankiet;
select Srod_lok, count(*) from lok join dane_ankiet using(Id) where Pora_roku = "lato" and Wojewodztwo = "Mazowieckie" group by Srod_lok;
select * from (select Wojewodztwo ,count(*) as c from dane_ankiet group by Wojewodztwo) as t where c > 20;
select Imie, Nazwisko, Wojewodztwo from dane_ankiet where Id not in (select distinct Id from zain where Zainteresowania = "gry komputerowe" or Zainteresowania = "informatyka") and Wyksztalcenie != "podstawowe" and Wiek > 50 order by Nazwisko;
select sum(dochod), count(*) from dane_ankiet where Id in (select distinct Id  from lok where Srod_lok = "rower") and imie like "%a" and Wojewodztwo = "Zachodniopomorskie"