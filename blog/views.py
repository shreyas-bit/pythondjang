from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post,BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    context={'allPosts': allPosts}
    return render(request, 'blog/blogHome.html',context)
    # return HttpResponse('this is home')

def blogPost(request,slug): 
    post=Post.objects.filter(slug=slug).first() 
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for reply in replies:
      if reply.parent.sno not  in repDict.keys():#parent reply
        repDict[reply.parent.sno]=[reply] #current replies
      else:
        repDict[reply.parent.sno].append(reply)
    context= {'post':post,'comments':comments,'user':request.user,'repDict':repDict}
    return render(request, 'blog/blogPost.html',context)
    # return HttpResponse(f'this is blogPost:{slug}')

def postComment(request): 
    if request.method == 'POST':
        comment=request.POST.get('comment')
        user=request.user
        postSno=request.POST.get('postSno')
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get('parentSno')
        if parentSno== "":
          comment=BlogComment(comment=comment, user=user, post=post)
          comment.save()
          messages.success(request,"Successfully  Commented")   
        else:
          parent=BlogComment.objects.get(sno=parentSno)
          comment=BlogComment(comment=comment, user=user, post=post,parent=parent)   
          comment.save()
          messages.success(request,"Successfully Replied To Comment")   

        
    return redirect(f"/blog/{post.slug}")
   

    # return HttpResponse(f'this is blogPost:{slug}')