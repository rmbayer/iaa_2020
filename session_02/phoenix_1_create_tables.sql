
# Connect to Phoenix, before you run the following SQL commands.
# Use this syntax to connect to Phoenix:
# python /phoenix/bin/sqlline.py localhost:2181


# Create Tables in Phoenix Shell

CREATE TABLE IF NOT EXISTS mm_season
    (id VARCHAR, season VARCHAR, day VARCHAR, wteam VARCHAR, wscore INTEGER, lteam VARCHAR, lscore INTEGER, wloc VARCHAR, ot VARCHAR
    CONSTRAINT mypk PRIMARY KEY (id))
    SALT_BUCKETS = 1;

CREATE TABLE IF NOT EXISTS mm_teams
    (team_id VARCHAR, team_name VARCHAR
    CONSTRAINT mypk PRIMARY KEY (team_id))
    SALT_BUCKETS = 1;

