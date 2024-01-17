-- Display the average temperature (Fahrenheit) by city, ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
