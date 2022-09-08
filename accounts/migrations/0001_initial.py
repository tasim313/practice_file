# Generated by Django 3.2.4 on 2021-11-14 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('nid_number', models.CharField(blank=True, max_length=255, null=True)),
                ('identifier', models.CharField(blank=True, max_length=255, null=True)),
                ('bhamniuuid', models.CharField(blank=True, max_length=255, null=True)),
                ('create_account', models.BooleanField(default=False)),
                ('account_created', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_laboratory', models.BooleanField(default=False)),
                ('is_pharmacy', models.BooleanField(default=False)),
                ('is_assistant', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientUuid', models.CharField(blank=True, max_length=255, null=True)),
                ('serviceUuid', models.CharField(blank=True, max_length=255, null=True)),
                ('assistant_serviceUuid', models.CharField(blank=True, max_length=255, null=True)),
                ('startDateTime', models.CharField(blank=True, max_length=255, null=True)),
                ('endDateTime', models.CharField(blank=True, max_length=255, null=True)),
                ('providers_uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('video_stream_id', models.CharField(blank=True, max_length=500, null=True)),
                ('patientIdentifier', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=255, null=True)),
                ('assistant_name', models.CharField(blank=True, default='default', max_length=255, null=True)),
                ('appointment_uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('doctor_fee', models.IntegerField(default=0)),
                ('speciality', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('local_appointment_start_date_time', models.DateTimeField(blank=True, null=True)),
                ('local_appointment_end_date_time', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceUuid', models.CharField(blank=True, max_length=255, null=True)),
                ('available_for_appointment', models.BooleanField(default=False)),
                ('booth_location', models.CharField(blank=True, max_length=255, null=True)),
                ('assistant', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(blank=True, max_length=255, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('trade_license_number', models.CharField(blank=True, max_length=255, null=True)),
                ('tin_number', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('lab', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Laborder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('is_forwarded', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('forwarded_at', models.DateTimeField(blank=True, null=True)),
                ('lab', models.ManyToManyField(to='accounts.Lab')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(blank=True, max_length=255, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('tin_number', models.CharField(blank=True, max_length=255, null=True)),
                ('trade_license_number', models.CharField(blank=True, max_length=255, null=True)),
                ('license_number', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('pharmacy', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('is_forwarded', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('forwarded_at', models.DateTimeField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pharmacy', models.ManyToManyField(to='accounts.Pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Radiologyorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('is_forwarded', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('forwarded_at', models.DateTimeField(blank=True, null=True)),
                ('lab', models.ManyToManyField(to='accounts.Lab')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streeming_key', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='RadiologyorderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('given_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('radiologyorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radiologyorders', to='accounts.radiologyorder')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('given_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='accounts.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_notification', models.BooleanField(blank=True, default=True, null=True)),
                ('phone_notification', models.BooleanField(blank=True, default=True, null=True)),
                ('both_notification', models.BooleanField(blank=True, default=False, null=True)),
                ('no_notification', models.BooleanField(blank=True, default=False, null=True)),
                ('payment_notification', models.BooleanField(blank=True, default=False, null=True)),
                ('appointment_notification', models.BooleanField(blank=True, default=True, null=True)),
                ('forward_notification', models.BooleanField(blank=True, default=False, null=True)),
                ('user_notification', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_holder_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_branch_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_swift_code', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LaborderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('given_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('laborder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laborders', to='accounts.laborder')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('specialist', models.CharField(blank=True, max_length=255, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('tin_number', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor_license_number', models.CharField(blank=True, max_length=255, null=True)),
                ('hospital', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('serviceUuid', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor_fee', models.IntegerField(default=0)),
                ('available_for_appointment', models.BooleanField(default=False)),
                ('assistant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.assistant')),
                ('doctor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='accounts.appointment')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_types', to='accounts.paymenttype')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.assistant'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
