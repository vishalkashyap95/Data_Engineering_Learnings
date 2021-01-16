import os
from imbox import Imbox ## https://pypi.org/project/imbox/
from cryptography.fernet import Fernet # https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/#:~:text=Install%20Cryptography%20Library%20and%20Create%20Key&text=The%20first%20thing%20we're,then%20we'll%20use%20it.
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,date
from airflow import DAG

def download_csv_from_email():
	# this key is generated using 'Fernet.generate_key()'
	key = b'ODlkJOf-JaDMKdeI3IKZ4Gaa62d46mYA07s95hPUyPU='
	# encrypted_password = Fernet(key).encrypt(b'enter actual gmail password here for encryption')
	# print(encrypted_password)
	encrypted_password = b'gAAAAABf24neoGPP2VNo8EQlIo52UO9em5XQlU4SIDh1HRnmlS37K0D1GYSG182JvcjYP2nYAu4t4Etmo46otcE6H1pUE9brDA=='
	host = "imap.gmail.com"
	username = "uhjihujni@gmail.com"
	password = Fernet(key).decrypt(encrypted_password)
	# print(password)
	destination_folder = "D:\DataEngineering_Learnings\Week_3_Task\destination_folder"

	# if not os.path.isdir(destination_folder):
	#     os.makedirs(destination_folder,exist_ok=True)

	mail = Imbox(host, username = username,password = password.decode("utf-8"), ssl = True, ssl_context = None, starttls = False)
	all_inbox_messages = mail.messages(folder='Inbox', sent_from ='vkashyap569@gmail.com',unread=True,raw='has:attachment')

	if len(all_inbox_messages)>0:
		for (uid,message) in all_inbox_messages:
			print("Subject of the email :---> ",message.subject)
			if message.subject.lower().__contains__("data engineering learning"):
				# mail.mark_seen(uid)
				for attachment in message.attachments:
					try:
						if attachment.get('filename').endswith('.csv'):
							print('Attachments :--->',attachment.get('filename'))
							full_file_path = "{0}\\{1}".format(destination_folder,attachment.get('filename'))
							print("full file path :----> ",full_file_path)
							with open(full_file_path,'wb') as fw:
								fw.write(attachment.get('content').read()) 
					except Exception as e:
						print("Exception caught while downloading the attachment :--> ",e)
					finally:
						print("Inside finally block..Code executed.")

			mail.mark_seen(uid)
	else:
		print("No new unread message in Inbox, from 'vkashyap569@gmail.com' which has attachments.")


default_args = {
	'owner':'Vishal Kashyap',
	'start_date': date.today().strftime("%Y-%m-%d")
}

dag = DAG(dag_id='Download_csv_from_email',
		default_args=default_args,
		schedule_interval= '* * * * *'
	)

task_to_download_csv_from_email = PythonOperator(task_id='task_to_download_csv_from_email',python_callable=download_csv_from_email,dag=dag)
