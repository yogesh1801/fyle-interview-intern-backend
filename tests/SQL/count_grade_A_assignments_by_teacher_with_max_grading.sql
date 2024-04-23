select count(*) as no_a 
from assignments
where grade = 'A'
group by teacher_id
order by no_a desc limit 1;