# Write your MySQL query statement below

with DailyTotals as (
  select 
    visited_on, 
    sum(amount) as daily_total
  from 
    Customer
  group by 
    visited_on
),
MovingAverage as (
  select 
    visited_on,
    sum(daily_total) over (
      order by visited_on 
      rows between 6 preceding and current row
    ) as total_amount,
    round(avg(daily_total) over (
      order by visited_on 
      rows between 6 preceding and current row
    ), 2) as average_amount
  from 
    DailyTotals
)
select 
  visited_on, 
  total_amount as amount, 
  average_amount
from 
  MovingAverage
where 
  datediff(visited_on, (select min(visited_on) from Customer)) >= 6
order by 
  visited_on;

