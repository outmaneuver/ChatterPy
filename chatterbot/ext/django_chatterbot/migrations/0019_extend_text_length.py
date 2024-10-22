from django.db import migrations, models


class Migration(migrations.Migration):
    """
    This migration updates the column length for 'text' and 'search_text'
    in the 'statement' table to 1000 characters.
    """

    dependencies = [
        ('django_chatterbot', '0018_text_max_length'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                "ALTER TABLE statement ALTER COLUMN text TYPE varchar(1000);",
                "ALTER TABLE statement ALTER COLUMN search_text TYPE varchar(1000);"
            ],
            reverse_sql=[
                "ALTER TABLE statement ALTER COLUMN text TYPE varchar(255);",
                "ALTER TABLE statement ALTER COLUMN search_text TYPE varchar(255);"
            ]
        ),
    ]
