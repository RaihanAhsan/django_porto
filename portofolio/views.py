# portofolio/views.py
from django.shortcuts import render

def home(request):
    context = {
        'nama': 'Andi Prasetyo',
        'bio': 'Saya adalah seorang pengembang web Python yang antusias membangun solusi digital.',
    }
    return render(request, 'portofolio/home.html', context)

def about(request):
    return render(request, 'portofolio/about.html')

def blog(request):
    # Data dummy untuk artikel blog
    posts = [
        {
            'judul': 'Mengenal Django Framework',
            'tanggal': '15 Juli 2026',
            'kategori': 'Python',
            'isi': 'Django adalah framework web Python yang sangat powerful. Dalam artikel ini kita akan membahas dasar-dasar Django dan bagaimana memulainya dengan cepat.'
        },
        {
            'judul': 'Tips Belajar Pemrograman untuk Pemula',
            'tanggal': '10 Juli 2026',
            'kategori': 'Karir',
            'isi': 'Belajar pemrograman bisa terasa sulit di awal. Berikut beberapa tips yang bisa membantu Anda melewati masa-masa sulit tersebut.'
        },
        {
            'judul': 'Mengapa Memilih Bootstrap untuk Frontend?',
            'tanggal': '5 Juli 2026',
            'kategori': 'Frontend',
            'isi': 'Bootstrap adalah framework CSS yang paling populer. Mari kita bahas kelebihan dan kekurangannya untuk proyek web modern.'
        },
    ]
    context = {
        'posts': posts
    }
    return render(request, 'portofolio/blog.html', context)