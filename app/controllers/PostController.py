from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request


class PostController(Controller):
    def show(self, view: View):
        post = Post.all()
        return view.render("posts", {'posts':post})

    def single(self, view: View, request: Request):
        post = Post.find(request.param("id"))
        return view.render("single", {'post':post})
    
    def makeUpdate(self, view: View, request: Request):
        post = Post.find(request.param("id"))
        return view.render("update", {"post":post})
    
    def storeUpdate(self, request: Request, view: View):
        post = Post.find(request.param("id"))
        post.title = request.input("title")
        post.body = request.input("body") 
        post.save()
        return view.render("update", {"post":"Post updated successfully"})
    
    def delete(self, request: Request, view: View):
        post = Post.find(request.param('id'))
        post.delete()
        return view.render("posts", {"delPost":"Post updated successfully"})
        return 'post deleted'