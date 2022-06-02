# Module 9: Surfs Up Challenge

## Overview and Purpose:

The purpose of this challenege is to parse Hawaiian weather data to determine if a surf shop/ice cream shop is a sustainable year-round venture.  In order to determine the viability of this business venture, summary statistics were ran on weather data for the months of [June](https://github.com/laurlen2112/surfs_up/blob/main/resources/june_query.png) and [December](https://github.com/laurlen2112/surfs_up/blob/main/resources/dec_query.png).  This analysis was completed using Jupyter notebook and combination of Pandas and SQLAlchemy to parse and filter the data.

## Results:

* The mean temperature for the month of [June](https://github.com/laurlen2112/surfs_up/blob/main/resources/june_stats.png) is about 75 degrees.  The mean temperature for the month of [December](https://github.com/laurlen2112/surfs_up/blob/main/resources/dec_stats.png) is about 71 degrees.  Although December averages about 4 degress lower than June, each month is above 70 degrees so it likely warm enough to prompt customers to purchase ice cream.  

* The min temperature for June is about 64 degrees, while the min temperature for December is about 56 degrees.  Since December's minimum temperature is about 12 degrees lower than June's, the data suggests that on the coldest December days customers would not patronize a surf/ice cream shop because cold weather does not generally coincide with surfing or ice cream consumption.

* The max temp for June is about 85 degrees, while the max temp for December is about 2 degrees lower at 83.  These temperatures suggest that customers would engage in surfing and ice cream consumption.

## Summary:

The data indicates that a sufr shop/ice cream shop would be a viable year round business in Hawaii since the average December temperature is only about 4 degrees lower than the average June temperature.  While there is a 12 degree spread between the minimum temperatures for each month.  It is reasonable to infer that most consumers may not engage in beach activities when the temperature is in the 60s, so colder June days and colder December days are not likely to be profitable.  Finally, the maximun temperature for both months is in the 80s, a temperature range that encourages outdoor activities and comsumption of ice cream

This data provides a good starting point.  However, W.Avey may want to drill down on some of the statisics to better understand the data.  For example, it would be a good idea to count the number of days where the temperature was at the minimun temperature.  For example, data showing that 20 out of 31 December days is historically at minimun temperature, may indicate that this is not a year round business.  A similar query should be run for the max temperature as well because the number of days at max temp might coorrealate with higher sales.  Additionally, summary statistics should be captured on other weather conditions such as cloudiness, rain, and wind chill factor since these conditions may influence consumers' behavior.  Finally, W.Avey shoud consider doing this analysis on other months to provide a general picture of what to expect in regards to weather.  
