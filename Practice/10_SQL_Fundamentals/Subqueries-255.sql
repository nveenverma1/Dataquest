## 2. Subqueries ##

SELECT Major, Unemployment_rate from recent_grads
where  Unemployment_rate < (SELECT AVG(Unemployment_rate) from recent_grads)
order by Unemployment_rate

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(*) AS float) / (SELECT CAST (COUNT(*) AS float) FROM recent_grads) 'proportion_abv_avg'
FROM recent_grads 
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads)

## 4. Returning Multiple Results In Subqueries ##

SELECT Major, Major_category 
FROM recent_grads
WHERE Major_category IN (SELECT Major_category 
                         FROM recent_grads 
                         GROUP BY Major_category
                         ORDER BY SUM(Total) DESC
                         LIMIT 5)


## 5. Building Complex Subqueries ##

select AVG(cast(Sample_size AS float)/CAST(Total AS float)) 'avg_ratio'
FROM recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

select Major, Major_category, CAST(Sample_size AS float)/ CAST(Total AS float) 'ratio' 
FROM recent_grads
WHERE ratio > (select AVG(CAST(Sample_size AS float)/ CAST(Total AS float)) 'avg_ratio' FROM recent_grads)