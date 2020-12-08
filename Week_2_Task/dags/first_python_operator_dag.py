# There are 5 steps to create DAG 
# Step 1 - import the packages
# Step 2 - set default_args
# Step 3 - Initialize DAG
# Step 4 - Define tasks
# Step 5 - define dependecies



# Step 1 - importing packages
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.bash_operator import BashOperator
import datetime as dt

# Step 2 - create default args
default_args = {
	"owner" : "Vishal Kashyap",
	"depends_on_past":False,
	"start_date":dt.datetime(2020,12,2),
	"retries":0,
}

# Step 3 - Create a DAG object
dag = DAG(dag_id="First_python_operator_dag",
	default_args=default_args,
	catchup=False,
	schedule_interval="* * * * *")

# Step 4 - Create tasks
def test_method():
	print("This is the python method called from dags.")

python_task_1 = PythonOperator(task_id='id_python_task_1',
	python_callable = test_method,dag=dag)

dummy_task_2 = DummyOperator(task_id='id_dummy_task_2',dag=dag)

# t3 = BashOperator(task_id="task 3",bash_command='echo task 3',dag=dag)

# Step 5 - Defining dependencies
python_task_1 >> dummy_task_2

