from django.db import models
# Create your models here.
class Post(models.Model):
	header = models.CharField(max_length=255)
	content = models.TextField()
	when = models.DateTimeField()

 	
	def __unicode__(self):
		return u'{} at {}'.format(self.header,
			self.when)