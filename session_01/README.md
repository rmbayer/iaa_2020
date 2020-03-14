## IAA Module - Session 1 - Platform Overview

[Google Slides](https://docs.google.com/presentation/d/1CC03MXct8pW9DblZ4i7sICcYlbXg81xgyB1DLtDh_ig/edit?usp=sharing)

## Demo: Hortonworks Data Platform

For this demo, I am using [Cloudbreak](https://docs.hortonworks.com/HDPDocuments/Cloudbreak/Cloudbreak-2.7.2/index.html) to provision and deploy [Hortonworks HDP](https://docs.hortonworks.com) (Apache tech stack) across a set of [Google Cloud](https://cloud.google.com/) servers.

For single-machine, quick prototyping, you could also use the [Hortonworks Sandbox](https://hortonworks.com/products/sandbox/), which is available as VMWare, VirtualBox, or a Docker container.

Login to Cloudbreak (based on external IP of Cloudbreak VM instance):
user_email: ```admin@cloudbreak.com```
password: ```cloudbreak123```

## Demo: Google Cloud Dataproc

The second demo will demonstrate how to quickly deploy a Hadoop cluster using Google Cloud (specifically Google Dataproc). The cluster should spin up in ~2 minutes, and includes serives such as HDFS, Hive, Spark, and others.

To Launch a Google Cloud Dataproc cluster, execute these commands:
```
git clone https://github.com/zaratsian/IAA_Sessions.git
cd IAA_Sessions/session_01/
```
Create the 3+ node cluster (with parameters as specified in the bash script)
```
./dataproc_1_create_cluster.sh
```
To run a test PySpark script, run:
```
./dataproc_2_spark_submit.sh
```
Demo flow once Dataproc has launched:
```
# PySpark Shell - Connected as client to the  Yarn master
/usr/lib/spark/bin/pyspark --deploy-mode client --master yarn --name spark_example
```
```
# Step through ./spark_test_script.py within the PySpark shell

# Optional: For testing purposes, you can also create a Spark DF from python lists:
df = spark.createDataFrame([(1,'nc'),(2,'ca'),(3,'ny')], ['id','state'])
```
```
# Save sim DF as table
sim.write.mode("overwrite").saveAsTable('sim_table')
sim.write.mode("overwrite").format('orc').saveAsTable('sim_table_orc')
```
```
# Execute queries in Hive
/usr/lib/hive/bin/beeline -u jdbc:hive2://localhost:10000/default
# It's recommended to use the JDBC connection, but you can also directly connect to hive via:
#/usr/lib/hive/bin/hive

show tables;
describe formatted sim_table;
```
