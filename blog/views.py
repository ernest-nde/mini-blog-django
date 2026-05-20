from django.utils.functional import empty
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Comment
from django.core.paginator import Paginator

# Posts views
# List all posts
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'page_obj': page_obj})

# Detail of a post
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

# Create a post
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            post = Post.objects.create(title=title, content=content)
            # return redirect('detail', post.id)
            return render(request, 'posts/detail.html', {'post': post, 'success': 'Nouveau post ajouté avec succès!'})
        else:
            return render(request, 'posts/manage_post.html', {'error': 'Le titre et le contenu sont requis'})
    return render(request, 'posts/manage_post.html')

# Update a post
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return render(request, 'posts/detail.html', {'post': post, 'success': 'Le post : ' + post.title + ' a été modifié!'})
    return render(request, 'posts/manage_post.html', {'post': post})

# Delete a post
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('index')     

# Comments views
# List all comments
def list_comments(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()
    return render(request, 'posts/detail.html', {'comments': comments})

# Add a comment
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id) 
    
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            Comment.objects.create(
                post=post,
                author=author,
                content=content
            )
            return render(request, 'posts/detail.html', {'post': post, 'success': 'Nouveau commentaire ajouté!'}) 
        else:
            return render(request, 'posts/detail.html', {'post': post, 'error': 'L\'auteur et le contenu sont requis'})
    return render(request, 'posts/detail.html', {
        'post': post,
        'comments': post.comments.all()
    }) 
    
# Update a comment
def update_comment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comments.get(id=comment_id)
    if request.method == 'POST':
        comment.content = request.POST['content']
        comment.save()
        return redirect('detail', post.id)
    return render(request, 'posts/detail.html', {'post': post})

# Delete a comment
def delete_comment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comments.get(id=comment_id)
    comment.delete()
    return redirect('detail', post.id)    

                                                                                                                                                                                                                                                              
