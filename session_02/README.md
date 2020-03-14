## Apache Hive 

1. Build Container
<br>```cd ./IAA_Sessions/docker```
<br>Mac/Linux:  ```./hive_build.sh```
<br>Windows:    Double-click on ```hive_build.bat```

2. Run Container
<br>```./hive_run.sh```

3. Connect to Container
<br>```docker exec -it hadoop-master bash```

4. Within the Container - Load into HDFS
<br>```./hive_example_1_load_data.sh```

5. Within the Container - Connect to Hive via JDBC
<br>```./connect_to_hive.sh```

6. Execute Hive SQL, found here:
<br>https://github.com/zaratsian/IAA_Sessions/blob/master/docker/containers/hive/assets/hive_example_2_query.sql

More scripts and examples found here:
<br>https://github.com/zaratsian/Apache_Hive
<br>https://github.com/zaratsian/HDP_Tuning_Unofficial

## Apache Phoenix (HBase)

1. Build Container
<br>```cd ./IAA_Sessions/docker```
<br>Mac/Linux:  ```./phoenix_build.sh```
<br>Windows:    Double-click on ```phoenix_build.bat```

2. Run Container
<br>```./phoenix_run.sh```

3. Connect to Container
<br>```docker exec -it phoenix bash```

4. Start Services (Apache HBase and PHoenix Query Server)
<br>```./start_services.sh```

5. Within the Container - Connect to Phoenix
<br>```./connect_to_phoenix.sh```

6. Within the Container, run Phoenix commands to create empty tables. Syntax shown here:
<br>https://github.com/zaratsian/IAA_Sessions/blob/master/docker/containers/phoenix/assets/phoenix_1_create_tables.sql.sql

7. Within the Container, exit the phoenix shell and load CSV into the tables (from the bash shell):
<br>```./phoenix_2_load_csvs.sh```

8. Within the Container - Connect to Phoenix (again)
<br>```./connect_to_phoenix.sh```

9. Within Container - Execute Phoenix Queries. Syntax shown here:
<br>https://github.com/zaratsian/IAA_Sessions/blob/master/docker/containers/phoenix/assets/phoenix_3_queries.sql

## Apache Spark

1. Build Container
<br>```cd ./IAA_Sessions/docker```
<br>Mac/Linux:  ```./spark_build.sh```
<br>Windows:    Double-click on ```spark_build.bat```

2. Run Container
<br>```./spark_run.sh```

3. Connect to Container
<br>```docker exec -it spark bash```

4. Within the Container - Connect to PySpark
<br>```/spark/bin/pyspark --deploy-mode client --master local[*] --name sparksql```

5. Within the Container - Execute SparkSQL Commands. Syntax shown here:
<br>https://github.com/zaratsian/IAA_Sessions/blob/master/session_02/spark_sql_example.py

