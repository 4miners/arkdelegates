"""a URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from app.views.delegate import DelegateView
from app.views.home import health, Homepage
from app.views.api import Delegates
from app.views.edit import EditProposalView, EditContributionView, EditNodeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health, name='health'),

    # pages
    path('', Homepage.as_view(), name='homepage'),
    path('delegate/<slug:delegate_slug>/', DelegateView.as_view(), name='delegate'),

    # auth
    path('auth/', include('app.views.auth.urls')),

    # edit
    path('edit/proposal/', EditProposalView.as_view(), name='proposal'),
    path('edit/contribution/', EditContributionView.as_view(), name='contribution'),
    path('edit/node/', EditNodeView.as_view(), name='node'),

    # api
    path('api/delegates/', Delegates.as_view(), name='delegates'),
]
