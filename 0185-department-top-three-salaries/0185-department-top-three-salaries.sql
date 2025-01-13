# Write your MySQL query statement below

with ranked_salaries as (
    select 
        e.id,
        e.name,
        e.salary,
        d.name as department,
        dense_rank() over (partition by e.departmentid order by e.salary desc) as ranks
    from Employee e
    join Department d on e.departmentid = d.id
)
select 
    department,
    name as employee,
    salary as salary
from ranked_salaries
where ranks <= 3;
