from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from review.models import report
from functools import reduce
from operator import and_


class SearchResultView(LoginRequiredMixin, ListView):
    template_name = 'search/search.html'
    context_object_name = 'review_list'
    model = report

    def get_queryset(self):
        object_list = report.objects.all()
        q_word = self.request.GET.get('query')

        if q_word:
            """ 除外リストを作成 """
            exclusion_list = set([' ', '　'])
            q_list = ''

            for i in q_word:

                if i in exclusion_list:
                    pass
                else:
                    q_list += i

            keyword = reduce(
                and_, [Q(class_info__name__icontains=q) |
                       Q(teacher__name__icontains=q) for q in q_list]
            )

            object_list = object_list.filter(keyword)

        return object_list
