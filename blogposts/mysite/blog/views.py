from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage,\
                                        PageNotAnInteger

from.forms import EmailPostForm   
from django.core.mail import send_mail                                     
# Create your views here.
def post_list(request):
        #posts = Post.published.all()
        
        object_list = Post.published.all()


        
        paginator = Paginator(object_list,3) # 3 posts in each page
        page = request.GET.get('page')#tryinh to know how many pages we have now
        try:
             posts = paginator.page(page)#here we put the objects in the  paginator so that can be in a page into a a given page
        except PageNotAnInteger:# this means that if the parameter of page is not an integer, then display the next page
        # If page is not an integer deliver the first page
             posts = paginator.page(1)
        except EmptyPage:
        # If page is out of range deliver last page of results
         posts = paginator.page(paginator.num_pages)
        


        return render(request, 'blog/post/list.html', {'posts':posts,'page':page})


# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                             status='published',
#                             publish__year=year,
#                             publish__month=month,
#                             publish__day=day)



#     return render(request,
#    'blog/post/detail.html',

#        {'post': post})



def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent=False
    if request.method == 'POST':
    # Form was submitted
       form = EmailPostForm(request.POST)# here its trying to create  an instance of the form that is summited.
       if form.is_valid():


        cd = form.cleaned_data

        post_url = request.build_absolute_uri(
        post.get_absolute_url())
        subject = f"{cd['name']} recommends you read " \
        f"{post.title}"
        message = f"Read {post.title} at {post_url}\n\n" \
        f"{cd['name']}\'s comments: {cd['comments']}"
        send_mail(subject, message, 'owner@reportly.com',
            [cd['to']])
        sent = True
    else:
      form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
            'form': form,
            'sent': sent})
# Form fields passed validation
         
# ... send email


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,#this is how we were able to retrieve the post detail view.we use the get method.
    publish__day=day)
    context ={post:post}
    print(context)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
    # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
        # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request,
           'blog/post/detail.html',
            {'post':post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form})
                