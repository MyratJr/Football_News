from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from turkmenfutbol.forms import HabarlashmakForm
from django.contrib import messages
from .models import*
from django.utils import timezone
from django.db.models import Q


monthtkm={
    'January':'Ýanwar',
    'February':'Fewral',
    'March':'Mart',
    'April':'Aprel',
    'May':'Maý',
    'June':'Iýun',
    'July':'Iýul',
    'August':'Awgust',
    'September':'Sentýabr',
    'October':'Oktýabr',
    'November':'Noýabr',
    'December':'Dekabr'}

def Home(request):
    x1=tkm_league.objects.get(id=1)
    x2=apl.objects.get(id=1)
    x3=laliga.objects.get(id=1)
    x4=seria_a.objects.get(id=1)
    x5=bundes_liga.objects.get(id=1)
    x6=league1.objects.get(id=1)
    first=[x1,x2,x3,x4,x5,x6]
    a8=timezone.now()
    a88=football_news_continue.objects.all()
    for t in a88:
        t.when=a8.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    a1=league_logos.objects.all()
    a2=topar_surat_tkm.objects.all()
    a3=football_news_continue.objects.all()[:5]
    a4=importand_slide.objects.all()
    a5=video.objects.all()[:20]
    a6=football_news_continue.objects.all()[:30]
    a7=about_dashky.objects.all()
    context={
        'a1':a1,
        'a2':a2,
        'a3':a3,
        'a4':a4,
        'a5':a5,
        'a6':a6,
        'a7':a7,
        'a8':a8,
        'first':first
        # 'x1':x1,
        # 'x2':x2,
        # 'x3':x3,
        # 'x4':x4,
        # 'x5':x5,
        # 'x6':x6,
        # 'x7':x7,
    }
    return render(request,'index.html',context)

def About(request):
    a81=timezone.now()
    a88=football_news_continue.objects.all()
    for t in a88:
        t.when=a81.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    a6=football_news_continue.objects.all()[:20]
    a7=about_dashky.objects.all()
    context={
        'a6':a6,
        'a7':a7,
        'a81':a81
    }
    return render(request,'biz_hakda.html',context)

def Habarlashmak(request):
    a81=timezone.now()
    a88=football_news_continue.objects.all()
    for t in a88:
        t.when=a81.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    a6=football_news_continue.objects.all()[:20]
    a7=about_dashky.objects.all()
    a9=habarlashmak.objects.all()
    context={
        'a6':a6,
        'a7':a7,
        'a9':a9,
        'form':HabarlashmakForm,
        'a81':a81
    }
    return render(request,'habarlashmak.html',context)

def habarlash(request):
    form=HabarlashmakForm(request.POST)
    if form.is_valid():
            
        myregister=habarlashmak(at=form.cleaned_data['at'],
                                        email=form.cleaned_data['email'],
                                        title=form.cleaned_data['title'],
                                        desc=form.cleaned_data['desc']
                                        )
        myregister.save()
        messages.success(request,'Üstünlikli iberildi!!!')
        return redirect('/')
    messages.warning(request,'Iberilmedi ýalnyş girizdiňiz!!!')
    return redirect('Habarlashmak')

def eachnews(request, news_id):
    a8=timezone.now()
    a6=football_news_continue.objects.filter(~Q(id=news_id))[:10]
    a66=football_news_continue.objects.filter(~Q(id=news_id))[:20]
    for t in a6:
        t.when=a8.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    a7=about_dashky.objects.all()
    a10=football_news_continue.objects.get(id=news_id)
    a10.when=a8.day-a10.date.day
    a10.months=(monthtkm[a10.date.strftime('%B')])
    a10.save()
    a10.when=a8.day-a10.date.day
    a10.save()

    context={
        'a7':a7,
        'a6':a6,
        'a10':a10,
        'a8':a8,
        'a66':a66
    }
    return render(request,'her_news.html',context)

def table(request, liga_name):
    a8=timezone.now()
    a88=football_news_continue.objects.all()
    for t in a88:
        t.when=a8.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    a=0
    s=0
    a6=football_news_continue.objects.all()[:20]
    a7=about_dashky.objects.all()
    g2=last5.objects.filter(id=1)
    g1=last5.objects.filter(id=2)
    g3=last5.objects.filter(id=3)
    g4=last5.objects.filter(id=4)
    for q in g1:
        p1=q.win
    for q in g2:
        p3=q.win
    for q in g3:
        p2=q.win
    for q in g4:
        p4=q.win
    context={
        'a7':a7,
        'a6':a6,
        'p2':p2,
        'p1':p1,
        'p3':p3,
        'p4':p4,
        'a8':a8
    }
    if liga_name=='Bundes-liga':
        z1=league_logos.objects.get(at=liga_name)
        b1=bundes_liga.objects.all()
        b11=topar_surat_bundes_liga.objects.all()
        for j in b1:
            a+=1
            j.id=a
            j.save
    if liga_name=='Seria-a':
        z1=league_logos.objects.get(at=liga_name)
        b1=seria_a.objects.all()
        b11=topar_surat_seria_a.objects.all()
        for j in b1:
            a+=1
            j.id=a
            j.save        
    if liga_name=='La-liga':
        z1=league_logos.objects.get(at=liga_name)
        b1=laliga.objects.all()
        b11=topar_surat_laliga.objects.all()
        for j in b1:
            a+=1
            j.id=a
            j.save        
    if liga_name=='APL':
        z1=league_logos.objects.get(at=liga_name)
        b1=apl.objects.all()
        b11=topar_surat_apl.objects.all() 
        for j in b1:
            a+=1
            j.id=a
            j.save    
    if liga_name=='Türkmenistanyň ýokary ligasy':
        z1=league_logos.objects.get(at=liga_name)
        b1=tkm_league.objects.all()
        b11=topar_surat_tkm.objects.all()
        for j in b1:
            a+=1
            j.id=a
            j.save    
    if liga_name=='Çempionlar ligasy':
        b11=CL_Images.objects.all()
        z1=league_logos.objects.get(at=liga_name)
        b1=CL_club.objects.filter(related_id=1)
        b2=CL_club.objects.filter(related_id=2)
        b3=CL_club.objects.filter(related_id=3)
        b4=CL_club.objects.filter(related_id=4)
        b5=CL_club.objects.filter(related_id=5)
        b6=CL_club.objects.filter(related_id=6)
        b7=CL_club.objects.filter(related_id=7)
        b8=CL_club.objects.filter(related_id=8)
        listbirlik=[b1,b2,b3,b4,b5,b6,b7,b8]
        for j in listbirlik:
            for k in j:
                s+=1
                a+=1
                k.id=a
                k.save
                if s==4:
                    a=0
                    s=0  
        context['listbirlik']=listbirlik

    if liga_name=='Ýewropa ligasy':
        b11=EL_Images.objects.all()
        z1=league_logos.objects.get(at=liga_name)
        b1=EL_club.objects.filter(related_id=1)
        b2=EL_club.objects.filter(related_id=2)
        b3=EL_club.objects.filter(related_id=3)
        b4=EL_club.objects.filter(related_id=4)
        b5=EL_club.objects.filter(related_id=5)
        b6=EL_club.objects.filter(related_id=6)
        b7=EL_club.objects.filter(related_id=7)
        b8=EL_club.objects.filter(related_id=8)
        listbirlik=[b1,b2,b3,b4,b5,b6,b7,b8]
        for j in listbirlik:
            for k in j:
                s+=1
                a+=1
                k.id=a
                k.save
                if s==4:
                    a=0
                    s=0  
        context['listbirlik']=listbirlik

    if liga_name=='Konferensiýa ligasy':
        b11=ConferLiga_Images.objects.all()
        z1=league_logos.objects.get(at=liga_name)
        b1=ConferLiga_club.objects.filter(related_id=1)
        b2=ConferLiga_club.objects.filter(related_id=2)
        b3=ConferLiga_club.objects.filter(related_id=3)
        b4=ConferLiga_club.objects.filter(related_id=4)
        b5=ConferLiga_club.objects.filter(related_id=5)
        b6=ConferLiga_club.objects.filter(related_id=6)
        b7=ConferLiga_club.objects.filter(related_id=7)
        b8=ConferLiga_club.objects.filter(related_id=8)
        listbirlik=[b1,b2,b3,b4,b5,b6,b7,b8]
        for j in listbirlik:
            for k in j:
                s+=1
                a+=1
                k.id=a
                k.save
                if s==4:
                    a=0
                    s=0  
        context['listbirlik']=listbirlik              
                           
    if liga_name=='Liga-1':
        z1=league_logos.objects.get(at=liga_name)
        b1=league1.objects.all()
        b11=topar_surat_league1.objects.all()
        for j in b1:
            a+=1
            j.id=a
            j.save
    context['b1']=b1
    context['b11']=b11
    context['z1']=z1
    context['time_0']=z1.time.year-1     
    return render(request,'liga.html',context)

def eachvideo(request, video_id):
    a8=timezone.now()
    a88=football_news_continue.objects.all()
    for t in a88:
        t.when=a8.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    a6=football_news_continue.objects.all()[:20]
    a7=about_dashky.objects.all()
    a10=video.objects.get(id=video_id)
    a5=video.objects.filter(~Q(id=video_id))[:20]
    context={
        'a7':a7,
        'a6':a6,
        'a10':a10,
        'a5':a5,
        'a8':a8
    }
    return render(request,'her_video.html',context)

def All_News(request):
    a8=timezone.now()
    a88=football_news_continue.objects.all()
    for t in a88:
        t.when=a8.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    m1=football_news_continue.objects.all()
    a7=about_dashky.objects.all()
    context={
        'm1':m1,
        'a7':a7,
        'a8':a8
    }
    return render(request,'All_News.html',context)

def All_video(request):
    a1=video.objects.all()
    a7=about_dashky.objects.all()
    context={
        'a5':a1,
        'a7':a7,
    }
    return render(request,'All_videos.html',context)
cate={
    'tkm':1,
    'apl':2,
    'laliga':3,
    'seria_a':4,
    'bundes':5,
    'liga_1':6,
    'cl':7,
    'el':8,
    'conf_l':9
}
def liga_news(request,gysga):
    a7=about_dashky.objects.all()
    a8=timezone.now()
    a88=football_news_continue.objects.filter(bolum_sayla=cate[gysga])
    for t in a88:
        t.when=a8.day-t.date.day
        t.months=(monthtkm[t.date.strftime('%B')])
        t.save()
    context={
        'a7':a7,
        'a8':a8,
        'a88':a88,
    }
    return render(request,'Liga_news.html',context)
