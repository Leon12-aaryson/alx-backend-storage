-- a database script to sum the origins and name them nb_fans

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
