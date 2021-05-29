# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
#create_table = “CREATE TABLE IF NOT EXISTS
#songs (song_title varchar, artist_name varchar, year
#int, album_name varchar, single Boolean);”

#users - users in the app
#user_id, first_name, last_name, gender, level


songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays\
                         (songplay_id int PRIMARY KEY NOT NULL,\
                          start_time TIME,\
                          user_id int Not NULL,\
                          level VARCHAR,\
                          song_id VARCHAR,\
                          artist_id VARCHAR ,\
                          session_id INT NOT NULL,\
                          location VARCHAR,\
                          user_agent VARCHAR) user_id;")

user_table_create = ("CREATE TABLE IF NOT EXISTS users\
                     (user_id VARCHAR PRIMARY KEY NOT NULL,\
                      first_name VARCHAR,\
                      last_name VARCHAR,\
                      gender VARCHAR,\
                      level VARCHAR);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs\
                    (song_id  VARCHAR,\
                     title VARCHAR,\
                     artist_id VARCHAR ,\
                     year int ,\
                     duration decimal );")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists(\
                       artist_id VARCHAR,\
                       name VARCHAR,\
                       location VARCHAR ,\
                       latitude VARCHAR,\
                       longitude VARCHAR);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time (\
                     start_Time text ,\
                     hour text ,\
                     day TEXT ,\
                     week_of_year TEXT,\
                     month text,\
                     year int,\
                     weekday text);")



#hour, day, week of year, month, year, and weekday'''
# INSERT RECORDS

songplay_table_insert =("INSERT INTO songplays\
                        (songplay_id,\
                        start_time, user_id,\
                        level ,\
                        song_id ,\
                        artist_id ,\
                        session_id,\
                        location ,\
                        user_agent)\
values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (songplay_id) DO NOTHING;")

user_table_insert = ("INSERT INTO  users(user_id, first_name,\
                     last_name, gender, level)\
                     values(%s,%s,%s,%s,%s)\
                     ON CONFLICT (user_id) DO NOTHING;")

song_table_insert =  ("INSERT INTO  songs\
                      (song_id,\
                       title,\
                       artist_id,\
                       year , \
                       duration  )\
                       values(%s,%s,%s,%s,%s);")

artist_table_insert =("INSERT INTO artists\
                      (artist_id,\
                       name , \
                       location  , \
                       latitude , \
                       longitude \
                                              )\
                       values(%s,%s,%s,%s,%s);")


time_table_insert = ("INSERT INTO time(\
                     start_Time ,\
                     hour ,\
                     day  ,\
                     week_of_year ,\
                     month ,\
                     year ,\
                     weekday)\
                     values(%s,%s,%s,%s,%s,%s,%s);")

# FIND SONGS

song_select =("SELECT * FROM songplays")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]