from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Article
from django.views.generic.edit import UpdateView , DeleteView , CreateView
from django.urls import reverse_lazy
from django.db import models




class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"
    def get_queryset(self):
        return Article.objects.all()

class  ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    def get_queryset(self):
        return Article.objects.all()
    
class ArticleUpdateView(UpdateView):
    modle = Article
    fields = ('title','body')
    template_name = "articles/article_edit.html"
    def get_queryset(self):
        return Article.objects.all()
    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')
    def get_queryset(self):
        return Article.objects.all()
    
class ArticlecreateView(CreateView):
    model = Article
    template_name = "articles/article.html"
    fields = ('title', 'body' , 'author')
    def get_queryset(self):
        return Article.objects.all()
    

