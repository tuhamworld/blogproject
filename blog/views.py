from django.shortcuts import render, redirect
from .models import PostModel

# Create your views here.

def index(request):
	# query database to get all posts
	posts = PostModel.objects.all()

	# print("POSTS: ", posts)
	return render(request, 'blog/index.html', {'blogs':posts})

def create(request):
	if request.method == "POST":
		# grabbing hold of fields from the frontend
		title = request.POST['title']
		content = request.POST['content']
		# print("T: ", title)
		# print("C: ", content)

		# saving the info to the database
		PostModel.objects.create(
			title = title,
			content = content
			)
		return redirect('index')
	return render(request, 'blog/post_create.html', {})

def update(request, id):
	post = PostModel.objects.get(id=id)
	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['content']
		post.title = title
		post.content = content

		post.save()
		return redirect('index')

	return render(request, 'blog/update_post.html', {'post':post})

def delete(request, id):
	post = PostModel.objects.get(id=id)
	post.delete()

	return redirect("index")