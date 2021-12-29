from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    PUBLISHED = 'published'
    DRAFT = 'draft'
    STATUS_OF_CHOICES = [(DRAFT, 'Draft'),
                         (PUBLISHED, 'Published')]
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_OF_CHOICES, default=DRAFT)
    objects = models.Manager()
    published = PublishManager()

    def get_absolute_url(self):
        return reverse('blog:post_one',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug
                             ])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title + ' - ' + str(self.author)
