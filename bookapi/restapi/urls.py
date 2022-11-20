from django.urls import path
from .views import BookDetail, BookInfo


urlpatterns =[

    path('book/', BookDetail.as_view(), name='book'),
    path("book/<int:book_id>/", BookInfo.as_view())
]