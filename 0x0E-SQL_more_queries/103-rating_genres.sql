-- lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT tv_genres.name,
       SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_genres.genre_id
GROUP BY title
ORDER BY rating DESC;
