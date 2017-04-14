from django.shortcuts import render, get_object_or_404
from .models import Kategor, Tovar, Tovar_inphoto, Tovar_img
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render_to_response
from cart.forms import CartAddProductForm
from .forms import TovarForm
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError


def index(request):
    return render(request, 'shop/index.html', {})


def info(request):
    return render(request, 'shop/info_gl_str.html', {})


def log1(request):
    return render(request, 'shop/login_menu.html', {})


def login(request):
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("passwd")
    return render(request, 'shop/login.html', {'email': email, 'password': password})


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/log1/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "shop/login_menu.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.




class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = "shop/login.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


def ProductList(request, category_slug=None):
    category = None
    categories = Kategor.objects.all()
    products = Tovar.objects.filter(tovar_available=True)
    if category_slug:
        category = get_object_or_404(Kategor, kategory_slug=category_slug)
        products = products.filter(kategory_id=category)
    if 'phone_name' in request.GET:
        products = products.filter(tovar_name__icontains=request.GET['phone_name'])
    checki = request.GET.get('checki', False)
    check0 = request.GET.get('check0', False)
    check1 = request.GET.get('check1', False)
    check2 = request.GET.get('check2', False)
    check3 = request.GET.get('check3', False)
    check4 = request.GET.get('check4', False)
    check5 = request.GET.get('check5', False)
    check6 = request.GET.get('check6', False)
    check7 = request.GET.get('check7', False)
    check8 = request.GET.get('check8', False)
    check9 = request.GET.get('check9', False)
    check10 = request.GET.get('check10', False)
    check11 = request.GET.get('check11', False)
    check12 = request.GET.get('check12', False)
    check13 = request.GET.get('check13', False)
    check14 = request.GET.get('check14', False)
    check15 = request.GET.get('check15', False)
    check16 = request.GET.get('check16', False)
    check17 = request.GET.get('check17', False)
    check18 = request.GET.get('check18', False)
    check19 = request.GET.get('check19', False)
    check20 = request.GET.get('check20', False)
    check21 = request.GET.get('check21', False)
    check22 = request.GET.get('check22', False)
    check23 = request.GET.get('check23', False)
    check24 = request.GET.get('check24', False)

    if checki:
        try:
            z = [check0, check1, check2, check3, check4, check5, check6, check7, check8, check9,
                 check10, check11, check12, check13, check14, check15, check16, check17,
                 check18, check19, check20, check21, check22, check23, check24]

            a0 = Tovar_inphoto.objects.filter(tovarinphoto_proizv__in=[z[0], z[1], z[2], z[6]])
            list_a0 = []
            for i in a0.values_list('tovarinphoto_proizv', flat=True).order_by('tovarinphoto_proizv'):
                list_a0.append(i)

            a1 = Tovar_inphoto.objects.filter(tovarinphoto_diagon__in=[z[3], z[4], z[5]])
            list_a1 = []
            for i in a1.values_list('tovarinphoto_proizv', flat=True).order_by('tovarinphoto_proizv'):
                list_a1.append(i)

            a2 = Tovar_inphoto.objects.filter(tovarinphoto_ram__in=[z[7], z[8], z[9], z[10]])
            list_a2 = []
            for i in a2.values_list('tovarinphoto_proizv', flat=True).order_by('tovarinphoto_proizv'):
                list_a2.append(i)

            a3 = Tovar_inphoto.objects.filter(
                tovarinphoto_osnkamera__in=[z[11], z[12], z[13], z[14], z[15], z[16], z[17]])
            list_a3 = []
            for i in a3.values_list('tovarinphoto_proizv', flat=True).order_by('tovarinphoto_proizv'):
                list_a3.append(i)

            a4 = Tovar_inphoto.objects.filter(tovarinphoto_opsystem__in=[z[18], z[19], z[20]])
            list_a4 = []
            for i in a4.values_list('tovarinphoto_proizv', flat=True).order_by('tovarinphoto_proizv'):
                list_a4.append(i)

            a5 = Tovar_inphoto.objects.filter(tovarinphoto_cpu__in=[z[21], z[22], z[23], z[24]])
            list_a5 = []
            for i in a5.values_list('tovarinphoto_proizv', flat=True).order_by('tovarinphoto_proizv'):
                list_a5.append(i)

            list_all_p = []
            list_all_proizv = [list_a0, list_a1, list_a2, list_a3, list_a4, list_a5]
            for i in list_all_proizv:
                if len(i) != 0:
                    list_all_p.append(set(i))
                else:
                    pass
            iter_a = list_all_p[0]
            for i in list_all_p:
                iter_a &= i
            iter_a = list(iter_a)
            list_tovar = []
            for i in Tovar_inphoto.objects.filter(tovarinphoto_proizv__in=iter_a):
                list_tovar.append(i.tovar_id.tovar_name)

            products = Tovar.objects.filter(tovar_name__in=list_tovar)
        except IndexError:
            pass

    return render(request, 'shop/smartfons.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Tovar.objects.filter(tovar_name__icontains=starts_with)
    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list


def suggest_category(request):
    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']

    cat_list = get_category_list(8, starts_with)

    return render(request, 'shop/category_list.html', {'cat_list': cat_list})




    # Страница товара


def ProductDetail(request, id, slug):
    product = get_object_or_404(Tovar, id=id, tovar_slug=slug, tovar_available=True)
    har = Tovar_inphoto.objects.get(id=id)
    fot = har.phototovar.all()[0]
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/harakteriskick.html', {'product': product, 'har': har,
                                                        'cart_product_form': cart_product_form,
                                                        'fot': fot})


# def ProductDetail(request, id, slug):
#     product = get_object_or_404(Tovar, id=id, tovar_slug=slug, tovar_available=True)
#     har = Tovar_inphoto.objects.get(id=id)
#     cart_product_form = CartAddProductForm()
#     if request.method == "GET":
#         form = TovarForm(request.GET.get("phone_name", None))
#         print(request.GET['phone_name'])
#         if form:
#             product = Tovar_inphoto.objects.filter(tovarinphoto_info__icontains=form)
#             return render(request, 'shop/harakteriskick.html', {'product': product, 'har': har,
#                                                                 'cart_product_form': cart_product_form,
#                                                                 'form': form})
#         else:
#             form = TovarForm()
#         return render(request, 'shop/harakteriskick.html', {'product': product, 'har': har,
#                                                             'cart_product_form': cart_product_form,
#                                                             'form': form})

# def ProductDetail(request, id, slug):
# product = get_object_or_404(Tovar, id=id, slug=slug, available=True)
# cart_product_form = CartAddProductForm()
# return render_to_response('shop/product/detail.html',
#   {'product': product,
#  'cart_product_form': cart_product_form})



# Функция формы обратной связи
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['leva2048@mail.ru']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'leva2048@mail.ru', recepients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact.html', {'form': form })


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})
