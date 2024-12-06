# Write your MySQL query statement below
select e1.name
from Employee e1
join (
    select managerId, count(*) as direct_reports
    from Employee
    where managerId is not null
    group by managerId
    having COUNT(*) >= 5
) e2 on e1.id = e2.managerId;
