--  a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows AS tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_shows.id IN (SELECT DISTINCT tv_show_id FROM tv_show_genres)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
