from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post


def home(request):
    questions = Post.objects.filter(content_type='Q')
    return render(request, 'forum/home.html', {'questions': questions})


@login_required
def post_answer(request, question_id):
    if request.method == 'POST':
        answer_content = request.POST.get('answer')
        if answer_content:
            Post.objects.create(
                content_type='A',
                user=request.user,
                content=answer_content,
                parent_post_id=question_id
            )
    return redirect('home')

