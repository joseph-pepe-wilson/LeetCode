# Write your MySQL query statement below

with firstlogin as (
    select
        player_id,
        min(event_date) as first_login_date
    from
        activity
    group by
        player_id
),
nextdaylogin as (
    select
        f.player_id,
        f.first_login_date,
        a.event_date as next_day_login_date
    from
        firstlogin f
    left join
        activity a
    on
        f.player_id = a.player_id
        and a.event_date = date_add(f.first_login_date, interval 1 day)
)
select
    round(
        sum(case when next_day_login_date is not null then 1 else 0 end) * 1.0 / count(distinct f.player_id), 2
    ) as fraction
from
    nextdaylogin f;
