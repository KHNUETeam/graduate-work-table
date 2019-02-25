import re
import pandas
from graduate_table.settings import BASE_DIR
from datetime import datetime
import os
from .models import Faculty, Department, Form, Specialty, Base, Place, Cause, Degree, Leader, Student
from datetime import datetime
import math
import numpy as np



class ViewController:

    def __init__(self):
        self.__name = None

    def handle_file(self, file):
        if os.path.exists('{}'.format(os.path.join(BASE_DIR, 'tmp'))):
            return self.__upload(file)
        else:
            os.mkdir('{}'.format(os.path.join(BASE_DIR, 'tmp')))
            return self.__upload(file)

    def __upload(self, file):
        try:
            self.__name = 'report-{}'.format(datetime.timestamp(datetime.now().replace(microsecond=0)))
            with open('{}.xlsx'.format(os.path.join(BASE_DIR, 'tmp', self.__name)), mode='wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return True
        except:
            return False

    def get(self):
        dataframe = pandas.read_excel('{}.xlsx'.format(os.path.join(BASE_DIR, 'tmp', self.__name)),
                                    header=None,
                                    encoding='utf-8'
        )
        
        #dataframe.replace(np.nan, None)
        #print(dataframe[9])
        dataframe_list = dataframe.iloc[1:, :].values.tolist()
        
        for row in dataframe_list:
            faculty = None
            department = None
            form = None
            specialty = None
            base = None
            place = None
            cause = None
            degree = None
            leader = None
            student = None
            
            if str(row[13]) != 'nan':
                if str(row[5]) != 'nan':
                    if str.lower(str(row[5])) == 'о':
                        row[5] = 'очна'
                    elif str.lower(str(row[5])) == 'з':
                        row[5] = 'заочна'
                    else:
                        row[5] = None
                        
                if str(row[6]) != 'nan':
                    if str.lower(str(row[6])) == 'к':
                        row[6] = 'контракт'
                    elif str.lower(str(row[6])) == 'б':
                        row[6] = 'бюджет'
                    else:
                        row[6] = None

                if str(row[2]) != 'nan':
                    if not Faculty.objects.filter(name=row[2]):
                        faculty = Faculty(
                            name=row[2],
                            deleted=0
                        )
                        faculty.save()
                    else:
                        faculty = Faculty.objects.filter(name=row[2])[0]
                if str(row[3]) != 'nan':
                    if not Department.objects.filter(name=row[3]):
                        department = Department(
                            name=row[3],
                            deleted=0
                        )
                        department.save()
                    else:
                        department = Department.objects.filter(name=row[3])[0]
                if row[5]:
                    if not Form.objects.filter(name=row[5]):
                        form = Form(
                            name=row[5],
                            deleted=0
                        )
                        form.save()
                    else:
                        form = Form.objects.filter(name=row[5])[0]
                        
                if str(row[7]) != 'nan':
                    if not Specialty.objects.filter(code=row[7]):
                        specialty = Specialty(
                            code=row[7],
                            deleted=0
                        )
                        specialty.save()
                    else:
                        specialty = Specialty.objects.filter(code=row[7])[0]
                        
                if row[6]:
                    if not Base.objects.filter(name=row[6]):
                        base = Base(
                            name=row[6],
                            deleted=0
                        )
                        base.save()
                    else:
                        base = Base.objects.filter(name=row[6])[0]
                        
                if str(row[12]) != 'nan':
                    if not Place.objects.filter(name=row[12]):
                        place = Place(
                            name=row[12],
                            deleted=0
                        )
                        place.save()
                    else:
                        place = Place.objects.filter(name=row[12])[0]

                if str(row[1]) != 'nan':
                    if not Cause.objects.filter(text=row[1]):
                        cause = Cause(
                            text=row[1],
                            deleted=0
                        )
                        cause.save()
                    else:
                        cause = Cause.objects.filter(text=row[1])[0]

                if str(row[9]) != 'nan':
                    if not Degree.objects.filter(name=row[9]):
                        print(row[9])

                        degree = Degree(
                            name=row[9],
                            deleted=0
                        )
                        degree.save()

                    else:
                        degree = Degree.objects.filter(name=row[9])[0]

                if str(row[10]) != 'nan':
                    if not Leader.objects.filter(fullname=row[10]):
                        leader = Leader(
                            fullname=row[10],
                            deleted=0
                        )
                        leader.save()
                    else:
                        leader = Leader.objects.filter(fullname=row[10])[0]

                if str(row[4]) != 'nan':
                    fullname = str(row[4]).split(' ')
                    try:
                        surname = fullname[0]
                    except:
                        surname = None
                        
                    try:
                        name = fullname[1]
                    except:
                        name = None
                        
                    try:
                        patronymic = fullname[2]
                    except:
                        patronymic = None
                        
                    
                        
                    protection_date = None
                    date_release = None

                    try:
                        if str(row[11]) != 'nan':
                            protection_date = row[11]
                    except:
                        protection_date = None

                    if str(row[0]) != 'nan':
                        try:
                            date_release = row[0]
                        except:
                            date_release = None
                            
                    if surname and name:
                        if not Student.objects.filter(
                            surname=surname,
                            name=name,
                            theme=row[13]
                        ):
                            student = Student(
                                surname=surname,
                                name=name,
                                patronymic=patronymic,
                                specialty=specialty,
                                form=form,
                                base=base,
                                theme=row[13],
                                degree=degree,
                                leader=leader,
                                protection_date=protection_date,
                                protection_place=place,
                                deducated_cause=cause,
                                date_release=date_release,
                                deleted=0
                            )
                            student.save()

