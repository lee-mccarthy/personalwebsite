from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, help_text="Enter a project name.")
    subtitle = models.CharField(max_length=255, null=True, blank=True, help_text="Enter a brief description of the project.")
    description = models.TextField(null=True, blank=True, help_text="Enter a detailed description of the project.")
    image = models.ImageField(upload_to='portfolio/projects', null=True, blank=True, help_text="Upload an image for the project.")

    def __str__(self):
        return self.title


class Link(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return self.project.title + ' | ' + self.text


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    contact_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name + ' | ' + self.subject


class Spam(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    website = models.CharField(max_length=255)
    contact_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name + ' | ' + self.subject
