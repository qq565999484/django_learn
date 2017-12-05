#coding=utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# @python_3_unicode_compatible
class Post(models.Model):
    
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
    # 作者
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # 标题
    title = models.CharField(max_length=200)
    # 正文
    text = models.TextField()
    # 标签
    # tags = models.ManyToManyField()
    # 分类目录
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # 点击量
    click = models.IntegerField(default=0)
    # 创建时间
    created_date = models.DateTimeField(default=timezone.now)
    # 发布时间
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        