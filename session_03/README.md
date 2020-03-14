## Apache Spark - Data Processing & Machine Learning
1. Clone (or Download) Repo
```
git clone https://github.com/zaratsian/IAA_Sessions.git
cd IAA_Sessions/docker/
```

2. Build Container
<br>Mac/Linux:  ```./spark_build.sh```
<br>Windows:    Double-click on ```spark_build.bat```

3. Run Container
<br>```./spark_run.sh```

4. Open up Zeppelin Notebook (use the UI to submit code)
```
http://localhost:18080
```
5. Work through the following Labs:
<br>(1) Getting Started - Python
<br>(2) Flight Predictor - Python 
<br>(3) Movie Text Analytics - Python

Optional: Connect to the Docker container (submit code via cli)
```
docker exec -it spark bash
```
Within the Container - Connect to PySpark
```
/spark/bin/pyspark --deploy-mode client --master local[*] --name spark_lab
```
