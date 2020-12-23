""" TM112 20J TMA02 Q5
01/10/2019 - ng264 
Updated 16/10/2019 PP
Updated 20/04/2020 MS
"""

from tma02_stats import median
from tma02_stats import mean
from tma02_stats import corr_coef

""" You can use one of two approaches:
1)  add suitable code below and then run this file
2)  run this file first then do the calculation in the 
    Python interactive shell.
"""


# Billions of hours given in volunteering 2005 - 2014 (ONS)

volunteeringHours = [2.28,2.28,2.27,2.19,2.11,2.05,2.05,2.12,2.09,1.97]


# Median age of population 2005 - 2014 (ONS)

populationAge = [38.7,38.9,39.0,39.1,39.3,39.5,39.6,39.7,39.9,40.0]

#Find median of volunteering hours in billions and round to 2.d.p
volunteering_median = round(median(volunteeringHours),2)
print(volunteering_median, 'billion hours')

#find the mean volunteering hours in billions rounded to 2.d.p
volunteering_mean = round(mean(volunteeringHours),2)
print(volunteering_mean,'billion hours')

#find the correlation coefficient between volunteeringHours and populationAge
correlation_co = round(corr_coef(volunteeringHours,populationAge),2)

print(correlation_co)
