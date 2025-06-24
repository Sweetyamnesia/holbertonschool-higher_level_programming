-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title AS title, tv_genres.name AS name FROM tv_shows, tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
