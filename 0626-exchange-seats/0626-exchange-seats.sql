# Write your MySQL query statement below

select
    case
        when s1.id % 2 != 0 and s2.id is not null then s2.id
        when s1.id % 2 = 0 then s1.id - 1
        else s1.id
    end as id,
    s1.student
from
    Seat s1
left join
    Seat s2 on s1.id = s2.id - 1
order by
    id asc;