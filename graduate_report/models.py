from django.db import models


# Faculties table
class Faculty(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'faculty'

    def __str__(self):
        return self.name


# Departments table
class Department(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'department'

    def __str__(self):
        return self.name


# Forms table
class Form(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'form'

    def __str_(self):
        return self.name


# Specialties table
class Specialty(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=20, blank=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty')
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'specialty'

    def __str__(self):
        return self.code


# Learning base table
class Base(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True)
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'base'

    def __str__(self):
        return self.name


# Places table
class Place(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True)
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'place'

    def __str__(self):
        return self.name


# Leaders table
class Leader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    patronymic = models.CharField(max_length=255, blank=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty')
    deleted = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'leader'

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)


# Students table
class Student(models.Model):
    id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    patronymic = models.CharField(max_length=255, blank=True)
    specialty = models.ForeignKey('Specialty', models.DO_NOTHING, db_column='specialty', related_name='specialty')
    form = models.ForeignKey('Form', models.DO_NOTHING, db_column='form')
    base = models.ForeignKey('Base', models.DO_NOTHING, db_column='base')
    theme = models.TextField(blank=True)
    leader = models.ForeignKey('Leader', models.DO_NOTHING, blank=True)
    protection_date = models.BigIntegerField(blank=True)
    protection_place = models.ForeignKey('Place', models.DO_NOTHING, db_column='protection_place')
    protection_specialty = models.ForeignKey('Specialty', models.DO_NOTHING,
                                             db_column='protection_specialty',
                                             related_name='protection_specialty'
    )
    deducated_cause = models.TextField(blank=True)
    date_release = models.BigIntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'student'

    def __str__(self):
        return str.join(' ', (self.surname, self.name, self.patronymic))


