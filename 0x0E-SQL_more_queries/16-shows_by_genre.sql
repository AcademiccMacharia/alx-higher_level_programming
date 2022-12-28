-- Script to list all shows
-- Query to list shows and genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_genres.name;
