-- lists all shows contained in hbtn_0d_tvshows
-- that have atleast one genre lined
SELECT DISTINCT hbtn_0d_tvshows.tv_shows.title, hbtn_0d_tvshows.tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genre
ON hbtn_0d_tvshows.tv_show.id = hbtn_0d_tvshows.tv_show_genre.show_id
ORDER BY hbtn_0d_tvshows.tv_shows.title, hbtn_0d_tvshows.tv_show_genres.genre_id;
