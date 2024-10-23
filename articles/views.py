from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from articles.models import Articles
from django.core.paginator import Paginator

# Create your views here.


def navbar(request):
  return render(request, "navbar.html")


def accueil(request):
    articles_list = Articles.objects.all() 
    paginator = Paginator(articles_list, 3) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "accueil.html", {'page_obj': page_obj})


def useradmin(request):
   articles = Articles.objects.all()
   return render(request, "userAdmin.html",{'Articles': articles})

def detailsArticle(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, 'detailsArticle.html', {'article': article})




 
def new_article(request):
    if request.method == "POST":
        Author = request.user
        Title = request.POST['Title']
        Content = request.POST['Content']
        image = request.FILES['image']
        prix = request.POST['prix']
        if Title and Content and prix:
            article = Articles.objects.create(
                Author=Author,
                Title=Title,
                Content=Content,
                image=image,
                prix=prix
            )
            article.save()

            
            return redirect('accueil')  

        else:
            error_message = "Veuillez remplir tous les champs obligatoires."
            return render(request, "newArticle.html", {'error_message': error_message})
    return render(request, "newArticle.html")


def edit_article(request , id):
    article = get_object_or_404(Articles, id=id)
    if request.method == "POST":
        Title = request.POST['Title']
        Content = request.POST['Content']
        # image = request.FILES['image']
        prix = request.POST['prix']
        article_to_update = Articles.objects.filter(pk=article.id)
        article_to_update.update(
                Title=Title,
                Content=Content,
                # image=image,
                prix=prix
            )
        return redirect('useradmin')
    return render(request , "editArticle.html",{'article': article})

def delete_article(request , id):
    article = get_object_or_404(Articles, id=id)
    if request.method == "POST":
        article.delete()
        return redirect('useradmin')
    return render(request , "deleteArticle.html", {'article': article})


def contact(request):
  return render(request, "contact.html")

def propos(request):
  return render(request, "propos.html")