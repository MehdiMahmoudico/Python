insert into friendships (user_id,friend_id) values (1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(3,2),(3,5),(4,3),(5,1),(5,6),(6,2),(6,3);

SELECT * FROM users 
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id;

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users 
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id;

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users 
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id where users.id = 1;

select count(*) from friendships;

select users.first_name,count(friend_id) from users join friendships ON friendships.user_id = users.id group by user_id order by count(friend_id) desc limit 1 ;

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users 
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id where users.id = 3 order by friend_first_name desc;
