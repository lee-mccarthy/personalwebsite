from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, help_text="Enter a project name.")
    subtitle = models.CharField(max_length=255, help_text="Enter a brief description of the project.")
    description = models.TextField(help_text="Enter a detailed description of the project.")
    image = models.ImageField(upload_to='portfolio/projects', help_text="Upload an image for the project.")

    def __str__(self):
        return self.title


class Link(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return self.project.title + ' | ' + self.text
