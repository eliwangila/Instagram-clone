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


def edit_profile(request, username):
    template = loader.get_template('insta/edit_profile.html')
    user = Profile.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            profile.biography = form.cleaned_data['biography']
            profile.profile_pic = form.cleaned_data['profile_pic']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.save()
            return redirect(reverse('home'))
    else:

        form = ProfileForm(initial={'username': username,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'phone_number': profile.phone_number,
                                    # 'profile_pic': profile.profile_pic.url,
                                    'biography': profile.biography})

    context = {'form': form, 'user': user, 'profile':profile}
    return HttpResponse(template.render(context, request))