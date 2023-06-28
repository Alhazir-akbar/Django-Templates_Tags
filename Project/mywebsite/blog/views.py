from django.shortcuts import render

def blog(request):
    context = {
        'title':'Halaman Blog',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/login', 'Login'],
        ]
    }
    return render(request, 'index.html', context)
