
####################################################################################################
#
#   Spark Performance / Testing Script
#
#   This script will simulate data, execute basic commands (counts(), show(), ect.) and collect
#   cluster setting and runtime stats that can be used for Spark tuninig and configuration.
#
####################################################################################################

from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import datetime
import json
import sys

number_of_records = 1000

#conf  = SparkConf().setAppName('Spark Test Script').setMaster('yarn').set('deploy-mode','client')
conf  = SparkConf().setAppName('Spark Test Script').setMaster('local')
sc    = SparkContext(conf=conf)
spark = SparkSession \
    .builder \
    .config(conf=conf) \
    .getOrCreate()

start_time = datetime.datetime.now()
start_time_total = start_time

df = spark.range(0,number_of_records)

def sim_random():
    import random
    return random.random()

def sim_rate():
    import random
    return random.random() * random.triangular(100,1000,100)

def sim_bool1():
    import random
    return random.choice(['TRUE']*2 + ['FALSE']*8)

def sim_bool2():
    import random
    return int(random.choice([1]*2 + [0]*8))

def sim_gender():
    import random
    return random.choice(['MALE']*3 + ['FEMALE']*6)

def sim_age():
    import random
    return int(random.triangular(15,90,35))

def sim_rating():
    import random
    return int(random.triangular(1,10,6))

def sim_state():
    import random
    return ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'][int(random.triangular(0,49,2))]

def sim_name():
    import random
    return ['Frank','Dean','Dan','Sammy','James','Andrew','Scott','Steven','Kristen','Stephen','William','Craig','Stacy','Stuart','Christopher','Alan','Megan','Brian','Kevin','Kate','Molly','Derek','Martin','Thomas','Neil','Barry','Ian','Ashley','Iain','Gordon','Alexander','Graeme','Peter','Darren','Graham','George','Kenneth','Allan','Lauren','Douglas','Keith','Lee','Katy','Grant','Ross','Jonathan','Gavin','Nicholas','Joseph','Stewart'][int(random.triangular(0,49,2))]

def sim_date():
    import random
    return random.choice(['2015','2016','2017']) + '-' + str(random.choice(range(1,13))).zfill(2) + '-' + str(random.choice(range(1,30))).zfill(2)

udf_random  = udf(sim_random, FloatType())
udf_rate    = udf(sim_rate, FloatType())
udf_bool1   = udf(sim_bool1, StringType())
udf_bool2   = udf(sim_bool2, IntegerType())
udf_gender  = udf(sim_gender, StringType())
udf_age     = udf(sim_age, IntegerType())
udf_state   = udf(sim_state, StringType())
udf_name    = udf(sim_name, StringType())
udf_date    = udf(sim_date, StringType())
udf_rating  = udf(sim_rating, IntegerType())

sim = df.withColumn('date', udf_date() ) \
  .withColumn('name', udf_name() ) \
  .withColumn('age', udf_age() ) \
  .withColumn('gender', udf_gender() ) \
  .withColumn('state', udf_state() ) \
  .withColumn('flag1', udf_bool1() ) \
  .withColumn('flag2', udf_bool2() ) \
  .withColumn('metric1', udf_random() ) \
  .withColumn('metric1', udf_random() ) \
  .withColumn('metric1', udf_random() ) \
  .withColumn('rating', udf_rating() )


sim.show(20, False)


print('\n\n\n[ INFO ] Spark Test Successful!\n\n\n')


#ZEND
