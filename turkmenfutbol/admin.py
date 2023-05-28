from tkinter.tix import BALLOON
from django.contrib import admin
from .models import*

# admin {NEWS} parol {NEWS}

class PropertyImageInline(admin.StackedInline):
    model = topar_surat_tkm

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=tkm_league
admin.site.register(tkm_league,PropertyAdmin)
# ----------------------------------------------------
class PropertyImageInline(admin.StackedInline):
    model = topar_surat_apl

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=apl
admin.site.register(apl,PropertyAdmin)
# ----------------------------------------------------
class PropertyImageInline(admin.StackedInline):
    model = topar_surat_laliga

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=laliga
admin.site.register(laliga,PropertyAdmin)
# --------------------------------------------------
class PropertyImageInline(admin.StackedInline):
    model = topar_surat_seria_a

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=seria_a
admin.site.register(seria_a,PropertyAdmin)
# ------------------------------------------------
class PropertyImageInline(admin.StackedInline):
    model = topar_surat_bundes_liga

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=bundes_liga
admin.site.register(bundes_liga,PropertyAdmin)
# --------------------------------------------------
class PropertyImageInline(admin.StackedInline):
    model = topar_surat_league1

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline ]

    class Meta:
        model=league1
admin.site.register(league1,PropertyAdmin)
# ----------------------------------------------
class PropertyGroup(admin.StackedInline):
    model=CL_club
    extra=4

class PropertyAdmin(admin.ModelAdmin):
    inlines=[PropertyGroup]

    class Meta:
        model=Each_CL_Group

admin.site.register(Each_CL_Group,PropertyAdmin)
# -------------------------------------------------
class PropertyGroup(admin.StackedInline):
    model=EL_club
    extra=4

class PropertyAdmin(admin.ModelAdmin):
    inlines=[PropertyGroup]

    class Meta:
        model=Each_EL_Group

admin.site.register(Each_EL_Group,PropertyAdmin)
# -------------------------------------------------
class PropertyGroup(admin.StackedInline):
    model=ConferLiga_club
    extra=4

class PropertyAdmin(admin.ModelAdmin):
    inlines=[PropertyGroup]

    class Meta:
        model=Each_ConferLiga_Group

admin.site.register(Each_ConferLiga_Group,PropertyAdmin)
# -------------------------------------------------
admin.site.register(importand_slide)
admin.site.register(football_news_continue)
admin.site.register(video)
admin.site.register(about_dashky)
admin.site.register(habarlashmak)
admin.site.register(league_logos)
admin.site.register(last5)
admin.site.register(subcategory)
admin.site.register(bolumler)