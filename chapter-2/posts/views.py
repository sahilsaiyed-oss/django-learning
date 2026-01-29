from django.shortcuts import render  # <--- THIS LINE MUST BE AT THE VERY TOP

def posts_lists(request):
    return render(request, 'posts/posts_list.html')