-- lists all the TV shows contained in hbtn_0d_tvshows that has at least one genre linked
-- lists all the rows of a database that have one column in common
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
