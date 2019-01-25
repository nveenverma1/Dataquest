## 1. Introducing Joins ##

SELECT * FROM facts 
INNER JOIN cities ON cities.facts_id = facts.id
LIMIT 10;

## 2. Understanding Inner Joins ##

SELECT c.*, f.name 'country_name' FROM facts 'f'
INNER JOIN cities 'c' ON f.id = c.facts_id
LIMIT 5;

## 3. Practicing Inner Joins ##

SELECT f.name 'country', c.name 'capital_city' FROM facts 'f' 
INNER JOIN cities 'c'
ON c.facts_id = f.id
WHERE c.capital = 1;

## 4. Left Joins ##

SELECT f.name 'country', f.population FROM facts 'f'
LEFT JOIN cities 'c'
ON c.facts_id = f.id
WHERE c.name is NULL;

## 6. Finding the Most Populous Capital Cities ##

SELECT C.name 'capital_city', f.name 'country', c.population 
FROM  cities 'c'
LEFT JOIN facts 'f'
ON f.id = c.facts_id
WHERE c.capital = 1
ORDER BY 3 DESC LIMIT 10;

## 7. Combining Joins with Subqueries ##

SELECT c.name 'capital_city', f.name 'country', c.population 
FROM facts 'f' 
INNER JOIN (SELECT * FROM cities where capital = 1) 'c'
ON c.facts_id = f.id
WHERE c.population > 10000000
ORDER BY 3 DESC;

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT country, urban_pop, total_pop, CAST(urban_pop as FLOAT)/CAST(total_pop as FLOAT) 'urban_pct' 
from (SELECT f.name 'country',  sum(c.population) 'urban_pop' , f.population 
      'total_pop' from cities 'c' INNER join facts 'f'
      on c.facts_id = f.id
      GROUP by f.id)
WHERE urban_pct > 0.5
ORDER BY urban_pct;