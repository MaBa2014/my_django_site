from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

from .models import Lesson
from .forms import PostForm
def lessons_list(request):
    lessons = Lesson.objects.order_by('lesson_name')
    return render(request, 'my_app/lessons_list.html', {'lessons': lessons})


def lesson_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('lessons_list')
    else:
        form = PostForm()
        return render(request, 'my_app/post_edit.html',{'form': form})

