from django.urls import path
# from .views import  polls_list, polls_detail

from .apiviews import PollList, PollDetail


# URL PATTERNS FOR DJANGO VIEWS
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]

# URL PATTERNS FOR DRF APIVIEW
urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]
