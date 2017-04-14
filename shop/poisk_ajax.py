# from shop.models import Tovar
# from django.shortcuts import render, get_object_or_404
#
#
#
# def Obrab(request):
#     global tovar
#     if 'search' in request.POST:
#         if request.POST['search'] == '':
#             tovar="Начните вводить запрос"
#         else:
#             tovar=Tovar.objects.filter(tovar_name__icontains=request.POST['search'])
#     return render(request, 'shop/resSearch.html', {
#         'tovar': tovar
#     })