from django.shortcuts import render

from django.core.mail import send_mail
from doorcard import models
from django.utils.six import BytesIO
import qrcode
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # 将数据保存到数据库
        models.Card.objects.create(card_id=username, password=password, card_Email=email)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.Card.objects.all()
    return render(request, 'index.html', {'data': user_list})


def send(request):
    # send_mail('hello','hello massage','14777232006m@sina.cn',['14777232006m@sina.cn'], fail_silently=False)
    send_mail(
        'Subject',
        'Message.',
        '14777232006m@sina.cn',
        ['14777232006m@sina.cn', '14777232006m@sina.cn'],
    )
    return render(request, 'send.html')



def home(request):
        return render(request,'indexqr.html')

def generate_Image(request):
        website = request.POST.get('website')
        if(len(website) != 0):
                img = qrcode.make(str(website))
                buf = BytesIO()
                img.save(buf)
                image_stream = buf.getvalue()
                response = HttpResponse(image_stream,content_type="image/png")
                return response
        return HttpResponse(u"网址不能为空！")