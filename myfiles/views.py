from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from myfiles.models import Postlar, Sitelogo, Bolim


def index(malumot):
    post = Postlar.objects.all().order_by('-id')[0:3]
    logo = Sitelogo.objects.all().order_by('-id')[0:1]
    bolim = Bolim.objects.all().order_by('id')
    return render(malumot, 'index.html', {'post': post, 'logo':logo, 'bolim':bolim})
def post(malumot):
    if 'qidiruv' in malumot.POST:
        matn = malumot.POST.get('qidiruv')
        m = matn.strip()
        search = Q(nom__contains=matn)|Q(matn__contains=matn)|Q(ism__contains=matn)
        posts = Postlar.objects.filter(search)
        logo = Sitelogo.objects.all().order_by('-id')[0:1]
        bolim = Bolim.objects.all().order_by('id')
        return render(malumot, 'post.html', {'tan':posts, 'logo':logo,'bolim':bolim })
    posts = Postlar.objects.all().order_by('-id')
    logo = Sitelogo.objects.all().order_by('-id')[0:1]
    bolim = Bolim.objects.all().order_by('id')
    return render(malumot, 'post.html', {'tan':posts, 'logo':logo,'bolim':bolim })
def bolimlar(matn, id):
    tanaffus = Postlar.objects.all().order_by('-id')
    logo = Sitelogo.objects.all().order_by('-id')[0:1]
    filters = Postlar.objects.filter(bolimlar=id)
    bolim = Bolim.objects.all().order_by('id')
    return render(matn, 'bolimlar.html', {'tan':tanaffus, 'logo':logo, 'bolim':bolim, 'filtr':filters})

