with cte as(
Select player_id,min(event_date) as f,
DATE_ADD(MIN(event_date),interval 1 day) as s
from Activity group by player_id
)

Select round(count(distinct a.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from cte c join Activity a on c.player_id=a.player_id and a.event_date =c.s;