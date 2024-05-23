-- displays average temperature by city
SELECT temperatures.city, AVG(temperatures.value) AS avg_temp FROM temperatures GROUP BY temperatures.city ORDER BY avg_temp DESC;
