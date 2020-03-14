
# Run Phoenix Queries


!tables


SELECT * FROM MM_SEASON LIMIT 10;
!describe mm_season


SELECT * FROM mm_teams LIMIT 10;
!describe mm_teams;


###############################################################################################################
#
#   Phoenix - Join + Calculations
#
###############################################################################################################


# Calculate the Top 15 Teams with the most Wins
SELECT WTEAM_NAME, COUNT(*) AS WINS 

    FROM 

    (
    SELECT mm_season.*, 
        teams2a.team_name AS WTEAM_NAME, 
        teams2b.team_name AS LTEAM_NAME
        FROM mm_season
        LEFT JOIN mm_teams teams2a ON (mm_season.wteam = teams2a.team_id)
        LEFT JOIN mm_teams teams2b ON (mm_season.lteam = teams2b.team_id) 
    ) 
    
    GROUP BY WTEAM_NAME 
    ORDER BY WINS DESC 
    LIMIT 15;



# Calculate the Top 15 Teams with the most Losses
SELECT LTEAM_NAME, COUNT(*) AS LOSSES 

    FROM 

    (
    SELECT mm_season.*, 
        teams2a.team_name AS WTEAM_NAME, 
        teams2b.team_name AS LTEAM_NAME
        FROM mm_season
        LEFT JOIN mm_teams teams2a ON (mm_season.wteam = teams2a.team_id)
        LEFT JOIN mm_teams teams2b ON (mm_season.lteam = teams2b.team_id) 
    ) 
    
    GROUP BY LTEAM_NAME 
    ORDER BY LOSSES DESC 
    LIMIT 15;




# Calculate the Top 15 Matchups with the biggest score difference
SELECT SEASON, WSCORE, LSCORE, WLOC, (WSCORE-LSCORE) AS SCORE_DIFF, WTEAM_NAME, LTEAM_NAME

    FROM 

    (
    SELECT mm_season.*, 
        teams2a.team_name AS WTEAM_NAME, 
        teams2b.team_name AS LTEAM_NAME
        FROM mm_season
        LEFT JOIN mm_teams teams2a ON (mm_season.wteam = teams2a.team_id)
        LEFT JOIN mm_teams teams2b ON (mm_season.lteam = teams2b.team_id) 
    ) 
    
    ORDER BY SCORE_DIFF DESC
    LIMIT 15;



#ZEND
