from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
	entry_title = models.CharField(max_length=50)
	entry_text = models.TextField()
	entry_date = models.DateTimeField(auto_now_add=True)
	entry_author = models.ForeignKey(User, on_delete=models.CASCADE)


	class Meta:
		# Change nodel name on admin side
		verbose_name_plural = 'entries'

	def __str__(self):
		# Set title for posts
		return f'{self.entry_title}'
