# Write your MySQL query statement below
select 
     machine_id,
     round(avg(end_time - start_time), 3) as processing_time
from(
    select
         machine_id,
         process_id,
         max(case when activity_type = 'start' then timestamp end) as start_time,
         max(case when activity_type = 'end' then timestamp end) as end_time
    from Activity
    group by machine_id, process_id
) sub
group by machine_id