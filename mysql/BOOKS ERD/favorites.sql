insert into favorites (user_id,book_id) values (1,1),(1,2);
insert into favorites (user_id,book_id) values (2,1),(2,2),(2,3);
insert into favorites (user_id,book_id) values (3,1),(3,2),(3,3),(3,4);
insert into favorites (user_id,book_id) values (4,1),(4,2),(4,3),(4,4),(4,5);
select * from users join favorites on users.id = favorites.user_id where favorites.book_id = 3 ;
delete from favorites order by book_id = 3 desc limit 1;
insert into favorites (user_id,book_id) values (5,2);
select * from books join favorites on books.id = favorites.book_id where favorites.user_id = 3;
select * from users join favorites on users.id = favorites.user_id where favorites.book_id = 5 ;


