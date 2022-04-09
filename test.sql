WITH
    ratings_subquery AS (
        SELECT
            ratings.username,
            COUNT(rating) AS ratings_quantity
        FROM
            ratings
        GROUP BY
            ratings.username
        HAVING
            COUNT(rating) > 50
        ),
    reviews_subquery AS (
        SELECT
            reviews.username,
            COUNT(text) AS reviews_quantity
        FROM
            reviews
        GROUP BY
            reviews.username
    )
SELECT
    AVG(reviews_quantity)
FROM
    ratings_subquery
    LEFT JOIN reviews_subquery ON reviews_subquery.username = ratings_subquery.username
