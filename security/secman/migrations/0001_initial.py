# Generated by Django 5.0.7 on 2024-09-30 06:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeJoining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('contact_number', models.CharField(max_length=15)),
                ('emergency_contact1', models.CharField(max_length=15)),
                ('emergency_contact_relation1', models.CharField(max_length=20)),
                ('emergency_contact_relation1_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('current_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('security_guard_training', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('job_experience', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('pancard', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('aadhar', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('voter', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('preferred_work_arrangements', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=50)),
                ('account_holder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=30, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=15, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_address', models.TextField(blank=True, null=True)),
                ('qualification', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=20)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='employee_pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Quotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('guard_basic_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_special_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_total_a', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_conveyance_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_education_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_travelling_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_house_duty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_total_b', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_washing_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_hra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_sub_total_c', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_pf', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_gratuity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_leave_with_wages', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_esic', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_paid_holiday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_uniform', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_total_c', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_service_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guard_grand_total_per_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_basic_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_special_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_total_a', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_conveyance_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_education_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_travelling_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_house_duty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_total_b', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_washing_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_hra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_sub_total_c', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_pf', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_gratuity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_leave_with_wages', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_esic', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_paid_holiday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_uniform', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_total_c', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_service_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_grand_total_per_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='quotations/')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intime', models.TimeField()),
                ('outtime', models.TimeField()),
                ('description', models.CharField(max_length=255)),
                ('shift_total_time', models.FloatField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('check_in_time', models.TimeField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave'), ('H', 'Holiday')], default='A', max_length=1)),
                ('shift', models.CharField(max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='secman.employeejoining')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField()),
                ('special_allowance', models.IntegerField()),
                ('total', models.IntegerField()),
                ('conveyance_allowance', models.IntegerField()),
                ('education_allowance', models.IntegerField()),
                ('travelling_allowance', models.IntegerField()),
                ('hours_daily_duty', models.IntegerField()),
                ('total_b', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('pf', models.IntegerField()),
                ('gratuity', models.IntegerField()),
                ('leave_with_wages', models.IntegerField()),
                ('esic', models.IntegerField()),
                ('paid_holiday', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('uniform', models.IntegerField()),
                ('total_c', models.IntegerField()),
                ('food_allowance', models.IntegerField()),
                ('price_partial_uniform', models.IntegerField()),
                ('actual_salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('replicated_basic_salary', models.IntegerField()),
                ('replicated_special_allowance', models.IntegerField()),
                ('replicated_conveyance_allowance', models.IntegerField()),
                ('replicated_education_allowance', models.IntegerField()),
                ('replicated_travelling_allowance', models.IntegerField()),
                ('replicated_hours_daily_duty', models.IntegerField()),
                ('replicated_food_allowance', models.IntegerField()),
                ('replicated_total', models.IntegerField()),
                ('replicated_total_b', models.IntegerField()),
                ('replicated_hra', models.IntegerField()),
                ('replicated_pf', models.IntegerField()),
                ('replicated_gratuity', models.IntegerField()),
                ('replicated_leave_with_wages', models.IntegerField()),
                ('replicated_esic', models.IntegerField()),
                ('replicated_paid_holiday', models.IntegerField()),
                ('replicated_bonus', models.IntegerField()),
                ('replicated_total_c', models.IntegerField()),
                ('replicated_actual_salary', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secman.employeejoining')),
            ],
        ),
        migrations.CreateModel(
            name='AdvancePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=100)),
                ('advance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('request_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('approval_pdf', models.FileField(blank=True, null=True, upload_to='advance_pdfs/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secman.employeejoining')),
                ('salary_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secman.salarydetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('hod', 'HOD'), ('fo', 'Field Officer'), ('company', 'Company')], default='fo', max_length=20)),
                ('contact', models.CharField(max_length=12)),
                ('gst_or_emergency', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaxInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=50)),
                ('po', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=15)),
                ('year', models.PositiveIntegerField()),
                ('guard_count', models.PositiveIntegerField()),
                ('amount_per_guard', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supervisor_count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_per_supervisor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cgst', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sgst', models.DecimalField(decimal_places=2, max_digits=12)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='invoices/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secman.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='quotations/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(limit_choices_to={'user_type': 'company'}, on_delete=django.db.models.deletion.CASCADE, to='secman.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='employeejoining',
            name='company',
            field=models.ForeignKey(limit_choices_to={'user_type': 'company'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='secman.userprofile'),
        ),
        migrations.CreateModel(
            name='BirthdayCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('birthday_date', models.DateField()),
                ('user_profile', models.ForeignKey(limit_choices_to={'user_type': 'company'}, on_delete=django.db.models.deletion.CASCADE, to='secman.userprofile')),
            ],
        ),
    ]
