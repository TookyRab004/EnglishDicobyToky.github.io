from re import template
from django.shortcuts import render, redirect
import requests
from django.shortcuts import render
import requests
from requests.exceptions import RequestException
 

def redirect_to_home(request):
    return redirect('home') 

def home(request):
    print("Fonction home access granted ")
    return render(request,template_name='home.html')

# Create your views here.



def search(request):
    try:
        if 'word' in request.GET:
            word = request.GET.get('word').strip()  # Supprimer les espaces blancs avec strip()
            if word:
                api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}/"
                response = requests.get(api_url)
                data = response.json()  # Appel à la méthode json()

                if isinstance(data, list) and len(data) > 0:
                    if 'meanings' in data[0] and data[0]['meanings']:
                        if 'definitions' in data[0]['meanings'][0] and data[0]['meanings'][0]['definitions']:
                            definition = data[0]['meanings'][0]['definitions'][0]['definition']
                            return render(request, 'res_search.html', {'word': word, 'definition': definition})
                error_message = "No match found"
                return render(request, 'res_search.html', {'word': word, 'error_message': error_message})
            else:
                error_message = "Please enter a word to search"
                return render(request, 'res_search.html', {'error_message': error_message})
    except RequestException as e:
        error_message = "No internet connection. Please check your connection and try again."
        return render(request, 'res_search.html', {'error_message': error_message})
    
    return render(request, template_name='home.html')




