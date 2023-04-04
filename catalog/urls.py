from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base_generic.html'), name='draw_menu'),
    path('<str:menu_name>/', TemplateView.as_view(template_name='base_generic.html'), name='draw_menu')
]