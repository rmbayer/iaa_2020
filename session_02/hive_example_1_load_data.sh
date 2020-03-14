
su -c "hadoop fs -mkdir /demo" hdfs
su -c "hadoop fs -mkdir /demo/ncaa" hdfs
su -c "hadoop fs -mkdir /demo/ncaa/SeasonResults" hdfs
su -c "hadoop fs -mkdir /demo/ncaa/Teams" hdfs
su -c "hadoop fs -put /data/SeasonResults.csv /demo/ncaa/SeasonResults/." hdfs
su -c "hadoop fs -put /data/Teams.csv /demo/ncaa/Teams/." hdfs

# Display hdfs directory
su -c "hadoop fs -ls /demo/ncaa/" hdfs

#ZEND
