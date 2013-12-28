create table movies (
   movieid serial8 primary key,
   title text,
   genre text,
   release_year int
);

insert into movies (title, genre, release_year)
 values ('The Hobbit: The Desolation of Smaug','Adventure,Fantasy', 2013);
insert into movies (title, genre, release_year)
 values ('Anchorman 2: The Legend Continues', 'Comedy', 2013);
insert into movies (title, genre, release_year)
 values ('Frozen', 'Animation,Adventure,Comedy', 2013);
insert into movies (title, genre, release_year)
 values ('American Hustle', 'Crime,Drama', 2013);
insert into movies (title, genre, release_year)
 values ('Saving Mr. Banks', 'Biography,Comedy,Drama', 2013);
insert into movies (title, genre, release_year)
 values ('The Wolf of Wall Street', 'Biography,Comedy,Crime',2013);
insert into movies (title, genre, release_year)
 values ('The Secret Life of Walter Mitty', 'Adventure,Comedy,Drama', 2013);
insert into movies (title, genre, release_year)
 values ('Lone Survivor', 'Action,Biography,Drama',2013);
insert into movies (title, genre, release_year)
 values ('The Hobbit: An Unexpected Journey', 'Adventure,Fantasy', 2012);
insert into movies (title, genre, release_year)
 values ('The Hunger Games', 'Adventure,Sci-Fi,Thriller', 2012);
insert into movies (title, genre, release_year)
 values ('Cloud Atlas', 'Adventure,Sci-Fi,Drama', 2012);
insert into movies (title, genre, release_year)
 values ('Pitch Perfect', 'Comedy,Music,Romance',2012);
