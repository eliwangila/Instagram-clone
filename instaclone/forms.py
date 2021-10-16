from django import forms
from django.forms import ModelForm
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls.base import reverse

from .models import Post, Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'location', 'caption']
class ProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    profile_pic = forms.ImageField(required=False)
    username = forms.CharField(max_length=500,required=True)
    first_name = forms.CharField(max_length=500, required=False)
    last_name = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    biography = forms.CharField(required=False, widget=forms.Textarea())


def add_post(request):
    template = loader.get_template('insta/post.html')
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = profile
            fs.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()
        pass

    context = {'form': form ,'profile':profile}
    return HttpResponse(template.render(context, request))