from django.contrib.auth.models import User
from django.db import models

from classifications.models import Category, Tag


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, through='PostTags')
    content = models.TextField()
    cover_image = models.ImageField(upload_to='posts/cover_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, tags=None):
        is_new = self.pk is None
        super().save(force_insert, force_update, using, update_fields)

        if tags is not None:
            # Remove old tags and replace
            PostTags.objects.filter(post=self).delete()
            for tag in tags:
                if self.author:  # ensure added_by is never None
                    PostTags.objects.create(post=self, tag=tag, added_by=self.author)


class PostTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"
