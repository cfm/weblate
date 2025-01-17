# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2.6 on 2021-09-23 08:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0139_alter_component_repoweb"),
        ("checks", "0005_alter_check_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="check",
            old_name="check",
            new_name="name",
        ),
        migrations.AlterUniqueTogether(
            name="check",
            unique_together={("unit", "name")},
        ),
    ]
