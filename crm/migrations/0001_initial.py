# Generated by Django 4.0 on 2021-12-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=1028)),
                ('country', models.CharField(max_length=1028)),
                ('client_tel_no', models.CharField(max_length=60)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_location', models.CharField(max_length=200)),
                ('client_postal_address', models.CharField(max_length=350)),
                ('client_status', models.CharField(choices=[('E', 'Existing'), ('P', 'Potential'), ('F', 'Former')], max_length=10)),
                ('facebook_account', models.URLField()),
                ('twitter_account', models.URLField()),
                ('instagram_account', models.URLField()),
                ('linkedin_account', models.URLField()),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('nature_of_assignment', models.CharField(blank=True, max_length=2000, null=True)),
                ('contract_period', models.CharField(blank=True, max_length=2000, null=True)),
                ('final_proposal_amounts', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=255)),
                ('personal_tel_no', models.CharField(max_length=255)),
                ('personal_email', models.EmailField(max_length=254)),
                ('personal_facebook_account', models.URLField()),
                ('personal_twitter_account', models.URLField()),
                ('personal_instagram_account', models.URLField()),
                ('personal_linkedin_account', models.URLField()),
                ('personal_status', models.CharField(choices=[('A', 'Active'), ('E', 'Exited')], max_length=10)),
                ('service_line', models.CharField(max_length=250)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.clientmanager')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('sms', models.CharField(blank=True, max_length=4096, null=True)),
                ('email_body', models.CharField(blank=True, max_length=7168, null=True)),
                ('email_subject', models.CharField(blank=True, max_length=1024, null=True)),
                ('account_sid', models.CharField(blank=True, max_length=1024, null=True)),
                ('api_version', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_sent', models.DateField(blank=True, null=True)),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('delete', models.CharField(blank=True, max_length=1200, null=True)),
                ('direction', models.CharField(blank=True, max_length=1200, null=True)),
                ('error_code', models.CharField(blank=True, max_length=1200, null=True)),
                ('error_message', models.CharField(blank=True, max_length=1200, null=True)),
                ('feedback', models.CharField(blank=True, max_length=1200, null=True)),
                ('fetch', models.CharField(blank=True, max_length=1200, null=True)),
                ('from_who', models.CharField(blank=True, max_length=1200, null=True)),
                ('media', models.CharField(blank=True, max_length=1200, null=True)),
                ('messaging_service_sid', models.CharField(blank=True, max_length=1200, null=True)),
                ('num_media', models.CharField(blank=True, max_length=1200, null=True)),
                ('num_segments', models.CharField(blank=True, max_length=1200, null=True)),
                ('price', models.CharField(blank=True, max_length=1200, null=True)),
                ('price_unit', models.CharField(blank=True, max_length=200, null=True)),
                ('sid', models.CharField(blank=True, max_length=1200, null=True)),
                ('status', models.CharField(blank=True, max_length=1200, null=True)),
                ('subresource_uris', models.CharField(blank=True, max_length=1200, null=True)),
                ('to', models.CharField(blank=True, max_length=1200, null=True)),
                ('update', models.CharField(blank=True, max_length=1200, null=True)),
                ('uri', models.CharField(blank=True, max_length=1200, null=True)),
                ('target_sms', models.CharField(blank=True, max_length=200, null=True)),
                ('target_emails', models.CharField(blank=True, max_length=200, null=True)),
                ('clients', models.ManyToManyField(blank=True, help_text='Press ctrl + click to add multiple users', to='crm.ClientManager')),
                ('contacts', models.ManyToManyField(blank=True, help_text='Press ctrl + click to add multiple users', to='crm.ContactManager')),
            ],
        ),
        migrations.CreateModel(
            name='FilterSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_parameter', models.CharField(blank=True, max_length=2048, null=True)),
                ('filtered_list', models.CharField(blank=True, max_length=2048, null=True)),
                ('user_filters', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
