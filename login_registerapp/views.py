from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from login_registerapp.models import User, Article, ArticleComment


def login(request):
    return render(request,'login_registerapp/login.html')

def login_logic(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    user = User.objects.filter(username=username)  #查看该用户是否存在
    article = Article.objects.all()
    if user: #存在
        print('1')
        user = User.objects.get(username=username)
        if password == user.password:
            request.session['login'] = 'ok'
            request.session['nickname'] = user.nickname
            request.session['username'] = username
            return redirect('login_registerapp:main')
        else:
            return render(request,'login_registerapp/login.html',{'error':'请检查用户名或密码'})
    else:
        return render(request,'login_registerapp/login.html',{'error':'用户名不存在'})



def index(request):
    return render(request,'login_registerapp/index.html')


def register(request):
    return  render(request,'login_registerapp/register.html')

def register_logic(request):
    user_name = request.POST.get('username')
    pass_word_1 = request.POST.get('password_1')
    pass_word_2 = request.POST.get('password_2')
    nick_name = request.POST.get('nickname')
    email = request.POST.get('email')
    if pass_word_1 != pass_word_2:
        return render(request,'login_registerapp/register.html',{'error':'两次密码不一致'})
    elif User.objects.filter(username=user_name):
        return render(request,'login_registerapp/register.html',{'error':'该用户名已存在'})
    else:
        User.objects.create(username=user_name,password=pass_word_1,nickname=nick_name,email=email)
        return render(request,'login_registerapp/login.html')


def forget_password(request):
    return render(request,'login_registerapp/forget.html')


def change_pwd(request):
    return render(request,'login_registerapp/changepwd.html')

def changepwd_logic(request):
    rst = request.session.get('login')
    if rst:
        username = request.POST.get('username')
        email = request.POST.get('email')
        if User.objects.filter(username=username,email=email):
            request.session['username'] = username
            return HttpResponse('1')
        else:
            return HttpResponse('2')  # 用户名与邮箱不一致
    else:
        return HttpResponse('不要乱点呀')


def reset(request):
    rst = request.session.get('login')
    if rst == 'ok':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(password1,password2)
        user_name = request.session['username']
        user = User.objects.get(username = user_name)
        if password1 == password2:
            user.password = password1
            user.save()
            print('修改好了')
            return HttpResponse('2')  #修改成功，跳转到登录页面
        else:
            return HttpResponse('1')  # 两次密码不一致
    else:
        return HttpResponse('不要乱点呀')

def main(request):
    rst = request.session.get('login')
    if rst:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        article = Article.objects.all()
        return render(request,'login_registerapp/blog.html',{'article':article,'users':user},{'user':username})
    else:
        article = Article.objects.all()
        return render(request,'login_registerapp/blog.html',{'article':article})



def contact(request):
    #要留言就需要先登录
    rst = request.session.get('login')
    if rst:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        num = len(ArticleComment.objects.all())
        comment = ArticleComment.objects.all()
        return render(request,'login_registerapp/contact.html',{'user':user,"num":num,"comment":comment})
    else:
        return redirect('login_registerapp:login')


def contact_logic(request):
    rst = request.session.get('login')
    body = request.POST.get('contact_con')
    if rst:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        nickname = user.nickname
        ArticleComment.objects.create(username=username,body=body,userimg='1',nickname=nickname)
        return redirect('login_registerapp:contact')
    else:
        return redirect('login_registerapp:login')


def log_out(request):
    request.session.clear()
    return render(request,'login_registerapp/index.html')




#tyy  tyy152207
