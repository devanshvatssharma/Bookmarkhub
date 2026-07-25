from django import forms
from .models import Bookmark,Collection,Tag
from django.contrib.auth.models import User
class BookmarkForm(forms.ModelForm):
    class Meta:
        model=Bookmark
        exclude=["owner","created_at","updated_at"]
    def __init__(self, *args,user=None, **kwargs):
        super(BookmarkForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields["collections"].queryset = Collection.objects.filter(owner=user)
            self.fields["tags"].queryset = Tag.objects.filter(owner=user)
        else:
            self.fields["collections"].queryset = Collection.objects.none()
            self.fields["tags"].queryset = Tag.objects.none()

class CollectionForm(forms.ModelForm):
    
    class Meta:
        model=Collection
        exclude=["owner","created_at","updated_at"]
    def __init__(self, *args,user=None, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.user=user
    def clean_name(self):
        name=self.cleaned_data["name"]
        query=Collection.objects.filter(owner=self.user,name=name)
        if(query.exists()):
            if(not query.filter(id=self.instance.id).exists()):
                raise forms.ValidationError("Name of collection should be unique")
        return name
 
class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        exclude=["owner","created_at","updated_at"]
    def __init__(self, *args,user=None, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.user=user
    def clean_name(self):
        name=self.cleaned_data["name"]
        query=Tag.objects.filter(owner=self.user,name=name)
        if(query.exists()):
            if(not query.filter(id=self.instance.id).exists()):
                raise forms.ValidationError("Name of tag should be unique")
        
        return name

class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email"]