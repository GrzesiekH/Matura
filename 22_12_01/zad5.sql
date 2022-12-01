select * from wypożyczenia join filmy using(ID_FILMU);
select count(*) from filmy where ODCINKI = 1;
select count(*) from filmy;
select ID_OSOBY, count(*) from wypożyczenia join filmy using(ID_FILMU) where wypożyczenia.ODCINKI = filmy.ODCINKI and filmy.ODCINKI != 1 group by ID_OSOBY;
select * from osoby where ID_OSOBY = "k24";
select * from filmy where ID_FILMU not in (select ID_FILMU from wypożyczenia join filmy using(ID_FILMU) group by ID_FILMU);
-- select * from wypożyczenia join filmy using(ID_FILMU) where filmy.ODCINKI !=1 and filmy.ODCINKI != wypożyczenia.ODCINKI