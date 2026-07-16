# portofolio/views.py
from django.shortcuts import render

def home(request):
    # Data yang akan dikirim ke halaman HTML
    context = {
        'nama': 'Andi Prasetyo',  # Ganti dengan nama Anda
        'title': 'Portofolio Saya',
        'bio': 'Saya adalah seorang pengembang web Python yang antusias membangun solusi digital.',
        'projects': [
            {
                'nama': 'Aplikasi Cuaca',
                'deskripsi': 'Aplikasi real-time berbasis API untuk menampilkan cuaca terkini.',
                'gambar': 'weather.jpg'  # nanti kita pakai placeholder
            },
            {
                'nama': 'Sistem Blog Django',
                'deskripsi': 'Blog sederhana dengan fitur CRUD dan autentikasi pengguna.',
                'gambar': 'blog.jpg'
            },
            {
                'nama': 'Dashboard Analitik',
                'deskripsi': 'Dashboard interaktif untuk menampilkan data penjualan.',
                'gambar': 'dashboard.jpg'
            },
        ]
    }
    return render(request, 'portofolio/home.html', context)