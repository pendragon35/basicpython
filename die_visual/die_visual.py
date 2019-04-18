import pygal

from die import die

die_1=die()
die_2=die(10)
results=[]

for roll_num in range(100):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()

hist.title="results of rolling two die 100 times."
hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="result"
hist.y_title="frequency of result"

hist.add('2d6',frequencies)
hist.render_to_file('die_visual.svg')

