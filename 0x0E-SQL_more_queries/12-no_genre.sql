-- Script to get records from database
-- Query to get genres that are not linked
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title;
