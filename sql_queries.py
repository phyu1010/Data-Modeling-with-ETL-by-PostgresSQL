# DROP TABLES

songplay_table_drop = "Drop Table if exists songplays"
user_table_drop = "Drop Table if exists users"
song_table_drop = "Drop Table if exists songs"
artist_table_drop = "Drop Table if exists artists"
time_table_drop = "Drop Table if exists time"

# CREATE TABLES

songplay_table_create = ("""Create Table If Not Exists songplays(
                            songplay_id SERIAL PRIMARY KEY, 
                            start_time timestamp,
                            user_id int NOT NULL,
                            level varchar,
                            artist_id varchar,
                            song_id varchar,
                            session_id int,
                            location text,
                            user_agent text)
""")

user_table_create = ("""Create Table If Not Exists users(
                         user_id int Not Null,
                         first_name varchar,
                         last_name varchar,
                         gender varchar,
                         level varchar,
                         PRIMARY KEY (user_id))
""")

song_table_create = ("""Create Table If Not Exists songs(
                        song_id varchar Not Null,
                        title varchar,
                        artist_id varchar,
                        year int,
                        duration float,
                        PRIMARY KEY (song_id))
""")

artist_table_create = ("""Create Table If Not Exists artists(
                          artist_id varchar,
                          name varchar,
                          location varchar,
                          latitude numeric,
                          longitude numeric,
                          PRIMARY KEY (artist_id))
""")

time_table_create = ("""Create Table If Not Exists time(
                        start_time timestamp NOT NULL,
                        hour int,
                        day int,
                        week int,
                        month int,
                        year int,
                        weekday varchar,
                        PRIMARY KEY (start_time))
""")

# INSERT RECORDS

songplay_table_insert = ("""Insert Into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                        Values(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""Insert Into users(user_id, first_name, last_name, gender, level)
                    Values(%s, %s, %s, %s, %s)
                    ON CONFLICT (user_id)
                    DO UPDATE SET level = excluded.level
""")

song_table_insert = ("""Insert Into songs(song_id, title, artist_id, year, duration)
                    Values(%s, %s, %s, %s, %s)
                    ON CONFLICT (song_id)
                    DO NOTHING
""")

artist_table_insert = ("""Insert Into artists(artist_id, name, location, latitude, longitude)
                      Values(%s, %s, %s, %s, %s)
                      ON CONFLICT (artist_id)
                      DO NOTHING
                      
""")


time_table_insert = ("""Insert Into time(start_time, hour, day, week, month, year, weekday)
                    Values(%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (start_time)
                    DO NOTHING
""")

# FIND SONGS

song_select = ("""Select s.song_id, a.artist_id from songs s join artists a
                    on s.artist_id=a.artist_id
                    where s.title=%s AND a.name=%s AND s.duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]