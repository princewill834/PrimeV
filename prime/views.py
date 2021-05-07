from django.shortcuts import render,get_object_or_404,redirect
from . models import Vendor, Post
from django.http import HttpResponse
import datetime
from account.models import Account
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context = {}
    return render(request,'prime/index.html', context)

def coupon(request):
    vendors = Vendor.objects.all()
    context = {'vendors':vendors}
    return render(request,'prime/coupon.html', context)

@login_required
def customer(request):
    posts = Post.objects.all()[:1]
    context = {'posts':posts}
    return render(request,'prime/customer.html', context)


def postDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post':post}
    return render(request,'prime/post_detail.html', context)


def withdraw(request):
    context = {}
    return render(request, 'prime/withdraw.html', context)

@login_required
def shareItem(request, slug):
    today = datetime.datetime.today()
    post = Post.objects.filter(slug=slug, date=today, sharer_id=request.user.id)
    for i in post:
        if i.shared is False:
            i.shared = True
            i.sharer = request.user
            i.save()
            credit = Account.objects.filter(email=request.user.email)
            for i in credit:
                if i.task_earned ==0:
                    i.task_earned=50
                    i.save()
                else:
                    prev_bal = i.task_earned
                    i.task_earned = prev_bal + 50
                    i.save()              
        else:
            return HttpResponse('You have already shared this post today')
    return redirect('post_detail', slug)

