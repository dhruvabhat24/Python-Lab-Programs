import shutil,os,zipfile
directory = 'c:\\Users\\Exam\\Program6'
archieved = shutil.make_archive('c:\\Users\\Exam\\Program6','zip','Program6')
if os.path.isfile('c:\\Users\\Exam\\Program6.zip'):
    print('Archieved', "Python.zip","created successfully")
else:
    print("Archieved","Python.zip","not created")