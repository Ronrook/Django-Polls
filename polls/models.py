from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count




class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option_one_count = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
