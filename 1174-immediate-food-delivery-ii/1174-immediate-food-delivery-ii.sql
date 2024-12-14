# Write your MySQL query statement below

with FirstOrder as (
    select
         customer_id,
         min(order_date) as first_order_date
    from
        Delivery
    group by
        customer_id
),

ImmediateFirstOrder as (
    select
         d.customer_id,
         d.order_date,
         d.customer_pref_delivery_date,
         case
             when d.order_date = d.customer_pref_delivery_date then 'immediate'
             else 'scheduled'
        end as order_type
    from 
        Delivery d
    join
        FirstOrder f
    on
        d.customer_id = f.customer_id
        and d.order_date = f.first_order_date
)

select
    round (
        sum(case when order_type = 'immediate' then 1 else 0 end) * 100 / count(*), 2
    ) as immediate_percentage
from
    ImmediateFirstOrder;
