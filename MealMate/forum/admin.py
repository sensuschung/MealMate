from django.contrib import admin
from forum.models import Tag,Forum,Post,GroupPost,JoinRequest

admin.site.register(Tag)
admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(GroupPost)
admin.site.register(JoinRequest)