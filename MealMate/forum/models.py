from django.db import models
from django.contrib.auth.models import User
import uuid

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Forum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    description = models.TextField(null=True,blank=True)
    notice = models.TextField(null=True,blank=True)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)
    creator = models.ForeignKey(User, related_name='created_forums',on_delete=models.SET_NULL,null=True)
    administrators = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # restaurant = models.ForeignKey(to_be_determined,on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    imaged = models.JSONField(null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    click = models.IntegerField(default=0,db_index=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class GroupPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    target_time = models.DateTimeField(db_index=True)
    sponser = models.ForeignKey(User, related_name='sponsered_posts', on_delete=models.CASCADE)
    address = models.CharField(max_length=40,default="默认")
    participants = models.ManyToManyField(User)
    max_participants = models.IntegerField(default=2)
    min_participants = models.IntegerField(default=2)
    # restaurant = models.ForeignKey(to_be_determined,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

class JoinRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,related_name='request_user',on_delete=models.CASCADE)
    target_post = models.ForeignKey(GroupPost,related_name='join_group_request',on_delete=models.CASCADE)
    is_comfirmed = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

