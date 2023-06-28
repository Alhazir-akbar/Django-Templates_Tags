from django.shortcuts import render

def index(request):
    context = {
        'title':'Halaman Utama',
        'nav':[
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/artikel', 'Artikel'],
            ['/login', 'Login'],
        ]
    }
    return render(request, 'index.html', context)