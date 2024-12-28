# Write your MySQL query statement below
with CumulativeWeight as (
    select
         person_id,
         person_name,
         weight,
         turn,
         sum(weight) over (order by turn) as cum_weight
    from
        Queue
)
select
    person_name
from
    CumulativeWeight
where
    cum_weight <= 1000
order by
    turn desc
limit 1;