from django.shortcuts import render
from .models import Video
from .forms import VideoForm




def hi(request):
    return render(request, 'play/style.html')
def vid(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    lastvideo = Video.objects.all()

    count = Video.objects.all().count()

    # videofile1 = lastvideo.videofile



    context = {'videofile': lastvideo,
               'count': count
               }
    return render(request, 'play/vidsplayer.html', context)