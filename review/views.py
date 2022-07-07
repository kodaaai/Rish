from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
)
from . import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model as user_model
from .forms import ReviewCreateForm, ClassCreateForm, TeacherCreateForm, TagCreateForm

# カスタムユーザーを使用する場合はこの記述は必須
User = user_model()


class ReviewListView(ListView):
    model = models.report
    template_name = "review/home.html"
    context_object_name = 'reviews'
    ordering = ['-id']
    paginate_by = 5


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.report
    form_class = ReviewCreateForm
    success_url = reverse_lazy('review:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = models.class_info
    form_class = ClassCreateForm
    template_name = "review/class_info_create.html"
    success_url = reverse_lazy('review:review-create')


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = models.teacher
    form_class = TeacherCreateForm
    template_name = "review/teacher_create.html"
    success_url = reverse_lazy('review:review-create')


class TagCreateView(LoginRequiredMixin, CreateView):
    model = models.Tag
    form_class = TagCreateForm
    template_name = "review/tag_create.html"
    success_url = reverse_lazy('review:review-create')
