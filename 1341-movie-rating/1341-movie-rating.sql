# Write your MySQL query statement below

(select name as results
from MovieRating
join Users
    using(user_id)
group by user_id
order by count(movie_id) desc, min(name) asc
limit 1)

union all

(select title as results
from MovieRating
join Movies
    using(movie_id)
where created_at >= '2020-02-01' and created_at  < '2020-03-01'
group by movie_id
order by avg(rating) desc, title
limit 1);

