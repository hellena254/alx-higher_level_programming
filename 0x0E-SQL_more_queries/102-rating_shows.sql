-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- USE hbtn_0d_tvshows_rate;
SELECT title,
       SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
