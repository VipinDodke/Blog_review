from django.shortcuts import render
from .models import Blog_out, Feedback

def index(request):
    page_blog= Blog_out.objects.all()
    n = len(page_blog)
    params = {'range': range(n), 't_blog': page_blog}
    return render(request, 'review/index.html', params)

def view(request,myid):
    Blogid = Blog_out.objects.filter(id=myid)
    fb = Feedback.objects.all()

    return render(request,'review/review.html',{'pi':Blogid[0],'fb':fb})

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('Name', '')
        Textarea = request.POST.get('Textarea1', '')
        b_id = request.POST.get('blog', '')
        file = request.POST.get('File01','')
        print(name,Textarea,b_id)
        fb = Feedback(Name=name, Textarea=Textarea, Blog_id=b_id,FileTy=file)
        fb.save()
        Blogid = Blog_out.objects.filter(id=b_id)
    fb = Feedback.objects.all()
    return render(request, 'review/review.html', {'pi': Blogid[0],'fb':fb})