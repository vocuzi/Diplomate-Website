from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
# Create your views here.

def home(request):
    from .models import Branch
    ds=Branch.objects.all().order_by('name')
    return render(request,"homepage.html",{'branches':ds})

# def subjects(request,branch,semester):
#     from .models import Branch, Subject, File
#     ds=Subject.objects.filter(branch=Branch.objects.get(abbreviation=branch)).filter(semester=semester).order_by('name')
#     data={'Applied Mathematics Volume 2':[2015,2016],'2':"Applied Mathematics Volume 2",'3':[2019]}
#     return render(request,"subjects.html",{"subjects":ds,"AM2":{2015,2016}})



def subjects(request,branch,semester):
    from .models import Branch, Subject, File
    ds=Subject.objects.filter(branch=Branch.objects.get(abbreviation=branch)).filter(semester=semester).order_by('name')
    nds=[]
    for item in ds:
        nds.append(File.objects.filter(subject=item))
    return render(request,"subjects.html",{"subjects":nds,"names":ds,"branch":Branch.objects.get(abbreviation=branch).name,"sem":semester})






def uploadHandle(f,filename):
    filename=filename+"."+f.name.split(".")[-1]
    with open('static/'+filename, 'wb+') as d:
        for chunk in f.chunks():
            d.write(chunk)
        return filename

def test(request):
    return HttpResponse(open("/home/vocuzi/newt-schamander/workspace/diplomate/home-page.html").read())
@csrf_protect
def upload(request):
    if request.method=='POST':
        import requests, time
        from .models import UploadLogs
        url="https://api.telegram.org/bot-id/"
        requests.get(url+"sendMessage?chat_id=xx&text=REVIEW : Someone Just Uploaded a Document on Diplomate with description \n\n "+request.POST['description'][0:100])
        filename=request.POST['branch']+"-"+request.POST['semester']+"-"+str(time.time())
        filename=uploadHandle(request.FILES['document'],filename)
        ds=UploadLogs(
            useragent=request.META['HTTP_USER_AGENT'],
            ip_address=request.META['HTTP_X_REAL_IP'],
            filename=filename,
            description=request.POST['description'],
        )
        ds.save()
        return redirect("https://diplomate.greybits.in/contribute/")
    return render(request, 'upload-file.html', {})

def contribute(request):
    return render(request,"contribute.html",{})
