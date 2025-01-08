# Write your MySQL query statement below

with cte as (
    select min(id) as min_id
    from Person
    group by email
)
delete from Person
where id not in (
    select min_id from cte
);