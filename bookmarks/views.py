from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Tag,Collection,Bookmark
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookmarkForm,CollectionForm,TagForm,ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
@login_required
def dashboard_view(request):
    
    bookmark_count=request.user.bookmark_set.count()
    collection_count=request.user.collection_set.count()
    tag_count=request.user.tag_set.count()
    recent_bookmarks=request.user.bookmark_set.order_by("-created_at")[:5]
    return render(request,"bookmarks/dashboard.html",{
        "bookmark_count":bookmark_count,
        "collection_count":collection_count,
        "tag_count":tag_count,
        "recent_bookmarks":recent_bookmarks,
    })

class BookmarkPageView(LoginRequiredMixin,ListView):
    model=Bookmark
    paginate_by=10
    template_name="bookmarks/bookmarks.html"
    context_object_name="bookmarks"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["collections"]=self.request.user.collection_set.all()
        context["tags"]=self.request.user.tag_set.all()
        return context
    
    def get_queryset(self):
        query=Bookmark.objects.filter(owner=self.request.user)
        q=self.request.GET.get("q")
        v=self.request.GET.get("visibility")
        c=self.request.GET.get("collection")
        t=self.request.GET.get("tag")
        s=self.request.GET.get("sort")
        if q:
            query=query.filter(title__icontains=q)
        if v:
            query=query.filter(visibility=v)
        if c:
            query=query.filter(collections__id=c)
        if t:
            query=query.filter(tags__id=t)
        if s:
            if s=="newest":
                query=query.order_by("-created_at")
            elif s=="oldest":
                query=query.order_by("created_at")
            elif s=="alphabetical":
                query=query.order_by("title")
            else:
                query=query.order_by("-created_at")
        else:
            query=query.order_by("-created_at")
        return query
class AddBookmarkView(LoginRequiredMixin,CreateView):
    model=Bookmark
    template_name="bookmarks/bookmarkadd.html"
    form_class=BookmarkForm
    
    success_url=reverse_lazy("bookmarks")
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"]=self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner=self.request.user
        messages.success(self.request,"Bookmark added successfully!!")
        return super().form_valid(form)
    
class BookmarkDetailView(LoginRequiredMixin,DetailView):
    model=Bookmark
    template_name="bookmarks/bookmarkdetail.html"
    context_object_name="bookmark"
    def get_queryset(self):
        query_set=Bookmark.objects.filter(owner=self.request.user)
        return query_set
    
class BookmarkUpdateView(LoginRequiredMixin,UpdateView):
    model=Bookmark
    template_name="bookmarks/bookmarkupdate.html"
    form_class=BookmarkForm
    def get_success_url(self):
        l=reverse_lazy("bookmarkdetail",kwargs={
            "pk":self.object.pk,
        })
        return l
    def get_queryset(self):
        query_set=Bookmark.objects.filter(owner=self.request.user)
        return query_set
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"]=self.request.user
        return kwargs
    def form_valid(self, form):
        form.instance.owner=self.request.user
        messages.success(self.request,"Bookmark updated successfully!!")
        return super().form_valid(form)
    
class DeleteBookmarkView(LoginRequiredMixin,DeleteView):
    model=Bookmark
    template_name="bookmarks/deletionconfirm.html"
    success_url=reverse_lazy("bookmarks")
    def get_queryset(self):
        query_set=Bookmark.objects.filter(owner=self.request.user)
        return query_set
    def form_valid(self, form):
        messages.success(self.request,"Bookmark Deleted successfully!!")
        return super().form_valid(form)
    
class CollectionPageView(LoginRequiredMixin,ListView):
    model=Collection
    template_name="bookmarks/collections.html"
    context_object_name="collections"
    paginate_by=10
    def get_queryset(self):
        query_set=Collection.objects.filter(owner=self.request.user).order_by("-created_at")
        srch=self.request.GET.get("q")
        sort=self.request.GET.get("sort")
        if srch:
            query_set=query_set.filter(name__icontains=srch)
        if sort == "newest":
            query_set=query_set.order_by("-created_at")
        if sort == "oldest":
            query_set=query_set.order_by("created_at")
        if sort == "alphabetical":
            query_set=query_set.order_by("name")
        return query_set
    
class CollectionAddView(LoginRequiredMixin,CreateView):
    model=Collection
    template_name="bookmarks/collectionadd.html"
    form_class=CollectionForm
    success_url=reverse_lazy("collections")
    def form_valid(self, form):
        form.instance.owner=self.request.user
        messages.success(self.request,"Collection added successfully!!")
        return super().form_valid(form)
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs["user"]=self.request.user
            return kwargs

class CollectionUpdateView(LoginRequiredMixin,UpdateView):
    model=Collection
    form_class=CollectionForm
    template_name="bookmarks/collectionupdate.html"
    success_url=reverse_lazy("collections")
    def get_queryset(self):
        query_set=Collection.objects.filter(owner=self.request.user)
        return query_set
    def get_form_kwargs(self):
        kwargs= super().get_form_kwargs()
        kwargs["user"]=self.request.user
        return kwargs
    def form_valid(self, form):
        messages.success(self.request,"Collection successfully updated!!")
        return super().form_valid(form)

class CollectionDeleteView(LoginRequiredMixin,DeleteView):
    model=Collection
    template_name="bookmarks/collectiondelete.html"
    success_url=reverse_lazy("collections")
    def form_valid(self, form):
        messages.success(self.request,"Successfully deleted collection!")
        return super().form_valid(form)
    
    def get_queryset(self):
        query_set=Collection.objects.filter(owner=self.request.user)
        return query_set

class TagPageView(LoginRequiredMixin,ListView):
    model=Tag
    template_name="bookmarks/tags.html"
    context_object_name="tags"
    paginate_by=10
    def get_queryset(self):
        query_Set=Tag.objects.filter(owner=self.request.user).order_by("-created_at")
        q=self.request.GET.get("q")
        s=self.request.GET.get("sort")
        if q:
            query_Set=query_Set.filter(name__icontains=q)
        if s == "oldest":
            query_Set=query_Set.order_by("created_at")
        elif s=="alphabetical":
            query_Set=query_Set.order_by("name")
        return query_Set

class AddTagView(LoginRequiredMixin,CreateView):
    model=Tag
    template_name="bookmarks/tagadd.html"
    form_class=TagForm
    success_url=reverse_lazy("tags")
    def form_valid(self, form):
        form.instance.owner=self.request.user
        messages.success(self.request,"Tag created successfully !!")
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs= super().get_form_kwargs()
        kwargs["user"]=self.request.user
        return kwargs

class UpdateTagView(LoginRequiredMixin,UpdateView):
    model=Tag
    template_name="bookmarks/tagedit.html"
    success_url=reverse_lazy("tags")
    form_class=TagForm
    def get_queryset(self):
        query_set=Tag.objects.filter(owner=self.request.user)
        return query_set
    
    def form_valid(self, form):
        messages.success(self.request,"Tag updated successfully!!")
        return super().form_valid(form)
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs["user"]=self.request.user
            return kwargs

class DeleteTagView(LoginRequiredMixin,DeleteView):
    model=Tag
    template_name="bookmarks/tagdelete.html"
    success_url=reverse_lazy("tags")
    def form_valid(self, form):
        messages.success(self.request,"Tag deleted successfully!!")
        return super().form_valid(form)
    def get_queryset(self):
        query_set=Tag.objects.filter(owner=self.request.user)
        return query_set
@login_required
def ProfileDetailView(request):
    user=request.user
    bookmarks=Bookmark.objects.filter(owner=request.user).count()
    collections=Collection.objects.filter(owner=request.user).count()
    tags=Tag.objects.filter(owner=request.user).count()
    return render(request,"bookmarks/profile.html",{
        "user":user,
        "bookmarks":bookmarks,
        "collections":collections,
        "tags":tags,
    })

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model=User
    form_class=ProfileForm
    template_name="bookmarks/profileupdate.html"
    success_url=reverse_lazy("profile")
    def form_valid(self, form):
        messages.success(self.request,"profile updated successfully!!")
        return super().form_valid(form)
    
    def get_queryset(self):
        query_set=User.objects.filter(pk=self.request.user.id)
        return query_set

@login_required
def delete_user(request):
    if request.method=='GET':
        return render(request,"bookmarks/accountdelete.html")
    if request.method=='POST':
        request.user.delete()
        logout(request)
        messages.success(request,"Account deleted successfully")
        return redirect("register_page")

