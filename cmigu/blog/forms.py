'''
forms一个很好的特性就是它既能从头定义一个表单，也能创建一个ModelForm来
将表单结果保存为一个模型。 
而这正是我们想要的功能，我们可以创建一个ModelForm来将表
单转换为一个Post模型。
'''

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)