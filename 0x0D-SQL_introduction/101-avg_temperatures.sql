-- displays the average temperature by city
-- ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM tempatures
GROUP BY city
ORDER BY avg_temp DESC;
