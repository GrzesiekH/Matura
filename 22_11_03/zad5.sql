-- select Rodzina, count(*) from jezyki group by Rodzina -- zad 1
-- select count(*) from  jezyki as j where jezyk not in (select jezyk from uzytkownicy where urzedowy = "tak" group by jezyk) -- zad 2
-- select jezyk, count(*) as c from (select distinct kontynent, Jezyk from uzytkownicy as u join panstwa as p using(panstwo)) as t group by jezyk -- zad 3
select jezyk, sum(Uzytkownicy) as suma from (select * from uzytkownicy join jezyki using(jezyk) where rodzina != "indoeuropejska") as t join panstwa using(panstwo) where Kontynent like "Ameryka%" group by jezyk order by suma desc limit 6
