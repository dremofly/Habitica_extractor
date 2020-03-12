from habitica import *

f = 'data/habitica-user-data.json'
begin = '2020-03-08 00:00:00'
end = '2020-03-15 00:00:00'
d = habitica(f, begin, end)
print(d.get_todos())
print(d.get_dailys())