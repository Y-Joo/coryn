# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.BigIntegerField()
    permission_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    group_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    permission_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Coin(models.Model):
    id = models.BigAutoField(primary_key=True)
    coin_name = models.CharField(max_length=100, blank=True, null=True)
    kr_name = models.CharField(max_length=100, blank=True, null=True)
    ticker = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coin'


class CoinNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    coin = models.ForeignKey(Coin, models.DO_NOTHING)
    link = models.CharField(max_length=255, blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coin_news'


class CoinPrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    coin = models.ForeignKey(Coin, models.DO_NOTHING)
    day_high = models.TextField(blank=True, null=True)
    day_low = models.TextField(blank=True, null=True)
    hour_high = models.TextField(blank=True, null=True)
    hour_low = models.TextField(blank=True, null=True)
    minute_high = models.TextField(blank=True, null=True)
    minute_low = models.TextField(blank=True, null=True)
    week_high = models.TextField(blank=True, null=True)
    week_low = models.TextField(blank=True, null=True)
    day_close = models.TextField(blank=True, null=True)
    day_open = models.TextField(blank=True, null=True)
    hour_close = models.TextField(blank=True, null=True)
    hour_open = models.TextField(blank=True, null=True)
    minute_close = models.TextField(blank=True, null=True)
    minute_open = models.TextField(blank=True, null=True)
    week_close = models.TextField(blank=True, null=True)
    week_open = models.TextField(blank=True, null=True)
    day_change = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coin_price'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.BigAutoField(primary_key=True)
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'
