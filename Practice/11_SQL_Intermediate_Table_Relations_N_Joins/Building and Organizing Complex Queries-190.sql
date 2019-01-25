## 3. The With Clause ##

WITH playlist_info AS
    (
    SELECT
        p.playlist_id 'playlist_id',
        p.name 'playlist_name',
        t.name 'track_name',
        (t.milliseconds/1000) 'length_seconds'
    FROM playlist p
    LEFT JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
    LEFT JOIN track t ON t.track_id = pt.track_id
    )
    
SELECT 
    playlist_id,    
    playlist_name, 
    COUNT(track_name) 'number_of_tracks',
    SUM(length_seconds) 'length_seconds'
FROM playlist_info
GROUP BY playlist_id
ORDER BY playlist_id;

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT 
        c.* FROM chinook.customer c
    INNER JOIN chinook.invoice i on c.customer_id = i.customer_id
    GROUP BY c.customer_id
    HAVING SUM(i.total) > 90;
    
SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * from chinook.customer_usa
UNION 
SELECT * from chinook.customer_gt_90_dollars;

## 6. Combining Rows Using Intersect and Except ##

WITH common AS
(
    SELECT * from customer_usa
    INTERSECT
    SELECT * FROM customer_gt_90_dollars
)

SELECT 
    e.first_name || " " || e.last_name 'employee_name',
    COUNT(common.customer_id) 'customers_usa_gt_90'
FROM employee e
LEFT JOIN common on common.support_rep_id = e.employee_id
WHERE e.title = "Sales Support Agent"
GROUP BY 1 ORDER BY 1;

## 7. Multiple Named Subqueries ##

WITH
    customers_india AS
        (
            SELECT * FROM customer
            WHERE country = "India"
        ),
    total AS
        (
            SELECT customer_id, SUM(total) 'total_purchases' FROM invoice
            GROUP BY customer_id
        )
        
SELECT 
    c.first_name || " " || c.last_name 'customer_name',
    total.total_purchases
FROM customers_india c
LEFT JOIN total ON c.customer_id = total.customer_id
ORDER BY customer_name;

## 8. Challenge: Each Country's Best Customer ##

WITH 
    ind_spend AS
        (
        SELECT 
            i.customer_id,
            SUM(i.total) 'ind_spending',
            c.country
        FROM invoice i 
        INNER JOIN customer c on c.customer_id = i.customer_id
        GROUP BY 1, 3
        ),
    max_spend AS
        (
        SELECT 
            country,
            MAX(ind_spending) 'max_spending'
        FROM ind_spend isp
        GROUP BY 1
        ),
    top_spend_per_country AS
        (
        SELECT 
            msp.country,
            msp.max_spending,
            (
                SELECT isp.customer_id
                FROM ind_spend isp 
                WHERE isp.ind_spending = msp.max_spending 
                and isp.country = msp.country
            ) customer_id
        FROM max_spend msp
        )
    
SELECT 
    tsp.country, 
    c.first_name || " " || c.last_name 'customer_name',
    tsp.max_spending 'total_purchased'
FROM customer c
INNER JOIN top_spend_per_country tsp
ON tsp.customer_id = c.customer_id
ORDER BY 1
    
