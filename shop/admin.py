from django.contrib import admin

# Register your models here.
from .models import Kategor,Tovar,Tovar_inphoto,Tovar_img






class  KategorAdmin(admin.ModelAdmin):
    list_display =['kategory_name', 'kategory_slug']
    prepopulated_fields = {'kategory_slug': ('kategory_name', )}

admin.site.register(Kategor, KategorAdmin)

class TovarAdmin(admin.ModelAdmin):
    list_display =['tovar_name','tovar_info','tovar_made','tovar_price',
                   'tovar_stock','tovar_available','tovar_created','tovar_updated']
    list_filter = ['tovar_available', 'tovar_created', 'tovar_updated','tovar_name']
    list_editable = ['tovar_price', 'tovar_stock', 'tovar_available']
    prepopulated_fields = {'tovar_slug': ('tovar_name',)}

admin.site.register(Tovar, TovarAdmin)

class  Tovar_inphotoAdmin(admin.ModelAdmin):
    list_display = ['tovarinphoto_slug','tovarinphoto_info','tovarinphoto_proizv','tovarinphoto_diagon','tovarinphoto_ram',
                    'tovarinphoto_akb','tovarinphoto_osnkamera','tovarinphoto_opsystem','tovarinphoto_color',
                    'tovarinphoto_cpu','tovarinphoto_razreshenie','tovarinphoto_frontkamera','tovarinphoto_scaner',
                    'tovarinphoto_3g','tovarinphoto_gps','tovarinphoto_matrix']

    list_filter = ['tovarinphoto_slug','tovarinphoto_info','tovarinphoto_proizv','tovarinphoto_diagon','tovarinphoto_ram',
                    'tovarinphoto_akb','tovarinphoto_osnkamera','tovarinphoto_opsystem','tovarinphoto_color',
                    'tovarinphoto_cpu','tovarinphoto_razreshenie','tovarinphoto_frontkamera','tovarinphoto_scaner',
                    'tovarinphoto_3g','tovarinphoto_gps','tovarinphoto_matrix']

admin.site.register(Tovar_inphoto, Tovar_inphotoAdmin )


class Tovar_imgAdmin(admin.ModelAdmin):
    list_display = ['tovar_name','tovar_image']





admin.site.register(Tovar_img, Tovar_imgAdmin)
#           Образец
#
#
#
# # Модель категории
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name', )}
# # Модель товара
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['price', 'stock', 'available']
#     prepopulated_fields = {'slug': ('name', )}
#
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
