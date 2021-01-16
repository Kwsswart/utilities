from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.bash_operator import BashOperator 

from datetime import datetime
from datetime import timedelta 


#default configuration that applies to the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@daily',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

def source1_to_s3():
    # Here we need two write the code that writes our data from source 1 to s3 

def source3_to_s3():
    # Here we need two write the code that writes our data from source 3 to s3

def source2_to_hdfs(config, ds, **kwargs):
    # code that writes our data from source 2 to hdfs
    # ds: the date of run of the given task.
    # kwargs: keyword arguments containing context parameters for the run.


# instantiate a DAG object:

dag = DAG(
    dag_id='my_dag',
    description='Simple DAG for learning',
    default_args=default_args)


# Creating four tasks in this DAG
# PythonOperator for the three tasks defined as Python functions and BashOperator for the Spark Job

config = get_hdfs_config()

src1_s3 = PythonOperator(
    task_id='source1_to_s3',
    python_callable=source_to_s3, # set to the name of predefined python functions
    dag=dag)

src2_hdfs = PythonOperator(
    task_id='source2_to_hdfs',
    python_callable=source2_to_hdfs, # set to the name of predefined python functions
    op_kwargs = {'config' : config},
    provide_context=True,
    dag=dag)

src3_s3 = PythonOperator(
    task_id='source3_to_s3',
    python_callable=source3_to_s3, # set to the name of predefined python functions
    dag=dag)

spark_job = BashOperator(
    task_id='spark_task_et1',
    bash_command='spark-submit --master spark://localhost:7077 spark_job.py',
    dag=dag)


# Setting dependancies we set these with the >> or << operators
src1_s3 >> spark_job
src2_hdfs >> spark_job
src3_s3 >> spark_job

"""
these set dependencies for different versions

# for Airflow <v1.7
spark_job.set_upstream(src1_s3)
spark_job.set_upstream(src2_hdfs)
# alternatively using set_downstream
src3_s3.set_downstream(spark_job)



When using a web server we  can start the web server and scheduler 

    > airflow webserver
    
    > airflow scheduler
"""