USE book_tracker;

CREATE PROCEDURE book_tracker.get_books()
select book_list.book_id,
	   book_list.title,
       author.name as author,
       genre.name as genre,
       book_list.pages,
       reading_level.level as reading_level,
       book_list.book_image,
       book_list.blurb
from book_list
JOIN author on book_list.author_id = author.author_id
JOIN genre on book_list.genre_id = genre.genre_id
JOIN reading_level on book_list.reading_level_id = reading_level.reading_level_id
order by Title;

CALL book_tracker.get_books(); -- Returns all books with data from foreign keys and titles in alphabetical order

DROP PROCEDURE IF EXISTS book_tracker.get_books;

