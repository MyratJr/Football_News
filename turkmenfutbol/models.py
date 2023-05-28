from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

class bolumler(models.Model):
    habar_lig=models.CharField(max_length=10,default=1)

    def __str__(self):
        return self.habar_lig


class subcategory(models.Model):
    wiwi=models.CharField(max_length=5)
    def __str__(self):
        return self.wiwi

class tkm_league(models.Model):
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='tkm_league_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='a')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='s')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='d')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='f')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='g')

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']
class topar_surat_tkm(models.Model):
    property=models.ForeignKey(tkm_league,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='tkm_league_pictures')



class importand_slide(models.Model):
    news_pics=models.ImageField(upload_to='news_pictures')
    title=models.CharField(max_length=1000)
    desc=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def shorten(self):
        return self.desc[:170]

    def __str__(self):
        return self.title

class football_news_continue(models.Model):
    bolum_sayla=models.ForeignKey(bolumler,on_delete=models.CASCADE,default=1)
    news_pics=models.ImageField(upload_to='news_pictures')
    title=models.CharField(max_length=1000)
    desc=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    saylanan=models.BooleanField(default=False)
    when=models.IntegerField(default=1)
    months=models.CharField(max_length=20,default=1)

    def shorten(self):
        return self.desc[:170]

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date']

class video(models.Model):
    at=models.CharField(default='asas',max_length=100)
    video=models.FileField(upload_to='videos')
    image=models.ImageField(upload_to='Images_of_videos')
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-date']


class about_dashky(models.Model):
    about=models.TextField()
    place=models.CharField(max_length=75)
    phone=models.IntegerField()
    email=models.EmailField()

    def __int__(self):
        return self.phone

class habarlashmak(models.Model):
    at=models.CharField(max_length=25)
    email=models.EmailField()
    title=models.CharField(max_length=100)
    desc=models.TextField(default=None)

    def __str__(self):
        return self.at

class last5(models.Model):
    win=models.ImageField(upload_to='last5')

    def __str__(self):
        return str(self.id)

class Group_Name(models.Model):
    group_name=models.CharField(max_length=7)

    def __str__(self):
        return str(self.group_name)

class Each_CL_Group(models.Model):
    group_name=models.ForeignKey(Group_Name,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.group_name)

class CL_club(models.Model):
    related=models.ForeignKey(Each_CL_Group,on_delete=models.CASCADE)
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='CL_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='y')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='u')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='i')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='o')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='p')

    
    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']


class CL_Images(models.Model):
    picture=models.ImageField(upload_to='CL_pictures')

class Each_EL_Group(models.Model):
    group_name=models.ForeignKey(Group_Name,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.group_name)

class EL_club(models.Model):
    related=models.ForeignKey(Each_EL_Group,on_delete=models.CASCADE)
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='EL_logos')
    utuk=models.IntegerField()
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='mm')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='nn')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='bb')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='vv')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='cc')

    
    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']


class EL_Images(models.Model):
    picture=models.ImageField(upload_to='EL_pictures')

class Each_ConferLiga_Group(models.Model):
    group_name=models.ForeignKey(Group_Name,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.group_name)

class ConferLiga_club(models.Model):
    related=models.ForeignKey(Each_ConferLiga_Group,on_delete=models.CASCADE)
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='ConferLiga_logos')
    utuk=models.IntegerField()
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='xx')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='zz')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='ll')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='kk')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='jj')

    
    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']


class ConferLiga_Images(models.Model):
    picture=models.ImageField(upload_to='ConferLiga_pictures')

class apl(models.Model):
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='apl_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='q')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='w')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='e')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='r')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='t')

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']

class topar_surat_apl(models.Model):
    property=models.ForeignKey(apl,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='apl_pictures')


class laliga(models.Model):
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='laliga_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='h')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='j')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='k')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='l')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='z')

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']

class topar_surat_laliga(models.Model):
    property=models.ForeignKey(laliga,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='laliga_pictures')


class seria_a(models.Model):
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='seria_a_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='x')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='c')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='v')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='b')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='n')

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']

class topar_surat_seria_a(models.Model):
    property=models.ForeignKey(seria_a,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='seria_a_pictures')


class bundes_liga(models.Model):
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='bundes_liga_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='tt')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='yy')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='uu')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='ii')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='oo')

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']

class topar_surat_bundes_liga(models.Model):
    property=models.ForeignKey(bundes_liga,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='bundes_liga_pictures')

class league1(models.Model):
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='league1_logos')
    utuk=models.IntegerField(default=1)
    oyun_jem=models.IntegerField()
    utush=models.IntegerField()
    dene_den=models.IntegerField()
    utulush=models.IntegerField()
    salnan_gol=models.IntegerField()
    ozune_gol=models.IntegerField()
    aratapawut=models.IntegerField()
    maglumat1=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='m')
    maglumat2=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='qq')
    maglumat3=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='ww')
    maglumat4=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='ee')
    maglumat5=models.ForeignKey(subcategory,on_delete=models.DO_NOTHING,default=1,related_name='rr')

    def __str__(self):
        return self.at

    class Meta:
        ordering=['-utuk','-aratapawut','-salnan_gol','-utush']

class topar_surat_league1(models.Model):
    property=models.ForeignKey(league1,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='league1_pictures')




class league_logos(models.Model):
    gysga=models.CharField(max_length=20)
    at=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='league_logos')
    time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.at

