from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contributions_count = models.IntegerField(default=0) 
    def __str__(self):
        return self.title

    @property
    def snippet(self):
        return self.content[:100] + '...'

    def add_line(self, line):
        self.content += f'\n{line}'
        self.contributions_count += 1 
        self.save()




