# Module 9: Surfs Up Challenge

## Overview:

This analysis parses Hawaiian weather data to determine if a surf/ice cream shop is a sustainable year-round venture.  In order to determine the viability of this business venture, summary statistics were computed on weather data for the months of [June](https://github.com/laurlen2112/surfs_up/blob/main/resources/june_query.png) and [December](https://github.com/laurlen2112/surfs_up/blob/main/resources/dec_query.png).  

## Results:

* The mean temperature for the month of [June](https://github.com/laurlen2112/surfs_up/blob/main/resources/june_stats.png) is about 75 degrees.  The mean temperature for the month of [December](https://github.com/laurlen2112/surfs_up/blob/main/resources/dec_stats.png) is about 71 degrees.  Based on this datapoint, a year-round surf/ice cream shop might be viable because the average temperature for each month is above 70 degrees and warmer weather generally prompts consumers to engage in outdoor activities and consumer cold foods.

* The minimum temperature for June is about 64 degrees.  June's minimum temperature is high enough to predict that some consumers may engage in outdoor activities during the colder days of June.  By contrast, the minimum temperature for December is about 56 degrees and it seems less likely that consumers would patronize a surf/ice cream shop during December's colder days.  

* The maximum temp for June is about 85 degrees and the maximum temp for December is about 2 degrees lower at 83.  These temperatures suggest that customers would engage in surfing and ice cream consumption.

## Summary:

The data indicates that a surf shop/ice cream shop would be a viable year round business in Hawaii since the average temperatures in June and December temperature are in the 70s and the maximum temperature for both months reaches into the 80s.  Consumers are more likely to engage in outdoor activities and consumption of ice cream during these temperatures.  Finally, the minimum temperatures of June and December indicate that the business may be less active.  However, it should be noted that the minimum temperature will occur less frequently than the average and maximum temperatures combined and some less active periods do not make the business unviable.

This data provides a good starting point.  However, additional queries should be conducted to assist in the decision making process. For example, W. Avey could drill down on this data to find the number of days per month at the average, minimum, and maximum temperatures.  This information could be visualized as a histogram to show the historic temperature fluctuations throughout June and December.  Also, it may be helpful to re-run the same temperature statistics and coordinate them with longitude, latitude, and elevation since some beaches on the Oahu may generally cooler or warmer depending where they are situated.

Finally, summary statistics should be captured on other weather conditions such as cloudiness, humidity, and wind chill factor for June and December since these conditions may influence consumers' behavior.  These conditions can be cross-referenced with temperature to glean the how many days were at a specific temperature and cloudy or how many days were at specific temperature and humid.  It should be noted that a different data set would need to be incorporated since [this data set](https://github.com/laurlen2112/surfs_up/blob/main/resources/table_keys.png) does not have that information. 
