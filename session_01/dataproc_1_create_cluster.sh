CLUSTER_NAME=iaa-gccluster
PYSPARK_SCRIPT=spark_test_script.py

# Spin up Dataproc Cluster on Google Cloud
gcloud dataproc clusters create $CLUSTER_NAME \
    --subnet default --zone us-east1-b \
    --master-machine-type n1-standard-2 --master-boot-disk-size 500 \
    --num-workers 4 --worker-machine-type n1-standard-2 --worker-boot-disk-size 500 \
    --num-preemptible-workers 3 \
    --image-version 1.3-deb9 \
    --project zproject201807

# Submit pyspark job
#gcloud dataproc jobs submit pyspark --cluster=$CLUSTER_NAME $PYSPARK_SCRIPT

# Cleanup / Remove Dataproc Cluster
#gcloud dataproc clusters delete $CLUSTER_NAME

#ZEND
