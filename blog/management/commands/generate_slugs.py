from django.core.management.base import BaseCommand
from django.utils.text import slugify
from blog.models import Post

class Command(BaseCommand):
    help = 'Genera slugs para posts que no tienen slug'

    def handle(self, *args, **kwargs):
        posts_without_slug = Post.objects.filter(slug__exact='')
        for post in posts_without_slug:
            post.slug = slugify(post.title)
            post.save()
        self.stdout.write(self.style.SUCCESS('Slugs generados para todos los posts sin slug'))