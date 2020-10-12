# Generated by Django 3.1.2 on 2020-10-10 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Snippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(blank=True, default="", max_length=100)),
                ("code", models.TextField(help_text="code model help text")),
                ("linenos", models.BooleanField(default=False)),
                (
                    "language",
                    models.CharField(
                        choices=[("cpp", "cpp"), ("js", "js"), ("python", "python")],
                        default="python",
                        max_length=100,
                    ),
                ),
                (
                    "style",
                    models.CharField(
                        choices=[
                            ("monokai", "monokai"),
                            ("solarized-dark", "solarized-dark"),
                            ("vim", "vim"),
                        ],
                        default="solarized-dark",
                        max_length=100,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="snippets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("created",),},
        ),
        migrations.CreateModel(
            name="SnippetViewer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "snippet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="viewers",
                        to="snippets.snippet",
                    ),
                ),
                (
                    "viewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="snippet_views",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
