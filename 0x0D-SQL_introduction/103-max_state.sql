-- displays the max temperature of each state
SELECT temperatures.state, MAX(temperatures.value) AS max_temp FROM temperatures GROUP BY temperatures.state ORDER BY temperatures.state ASC;
