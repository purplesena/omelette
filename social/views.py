from audioop import reverse
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import UserProfile
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        likers = profile.likers.all()
        liked = profile.liked.all()

        context = {
            'user': user,
            'profile': profile,
            'likers': likers,
            'liked': liked,
        }

        return render(request, 'social/profile.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['bio', 'physical_desc', 'birthdate', 'gender', 'sexuality', 'img1', 'img2', 'img3','img4']
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    
class People(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'social/people.html')