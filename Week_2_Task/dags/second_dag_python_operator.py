from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,date
from airflow import DAG
from random import random

default_args = {
	'owner':'Vishal Kashyap',
	'start_date': date.today().strftime("%Y-%m-%d")
}

dag = DAG(dag_id='Second_dag_python_operator_with_xcom',
	default_args=default_args,
	# schedule_interval = '*/5 * * * *'
	schedule_interval = None
	)

def print_ten_times_hello_world():
	for i in range(10):
		print("*****Hello World*****")

def push_random_value_to_xcom(**context):
	random_value = random()
	context['ti'].xcom_push(key='random_value',value=random_value)
	print("Random Value generated in python and pushed to xcom - {}".format(random_value))

def pull_random_value_from_xcom(**context):
	## 'ti' = task_instance
	received_random_value = context['ti'].xcom_pull(key='random_value')
	print("Random value received from xcom - {}".format(received_random_value))

python_task_1 = PythonOperator(task_id='python_task_1',python_callable=print_ten_times_hello_world,dag=dag)

bash_task_1 = BashOperator(task_id='bash_task_1', bash_command='echo -----Hello World-----',dag=dag)

python_task_push_random_value_to_xcom = PythonOperator(
				task_id='python_task_push_random_value_to_xcom',
				provide_context = True,
				python_callable=push_random_value_to_xcom,
				dag=dag)

python_task_pull_random_value_from_xcom = PythonOperator(
				task_id='python_task_pull_random_value_from_xcom',
				provide_context = True,
				python_callable=pull_random_value_from_xcom,
				dag=dag)

[python_task_1,bash_task_1] >> python_task_push_random_value_to_xcom >> python_task_pull_random_value_from_xcom
