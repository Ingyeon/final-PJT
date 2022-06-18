from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),  # 기본 영화 리스트
    path('genre/<int:genre_id>/',views.genre_movie), # 장르별 영화
    path('detail/<int:movie_id>/', views.movie_detail), # 영화 세부 정보 페이지 용
    path('<int:movie_id>/like/', views.like_movie), # 영화 좋아요 기능 
    path('similar/<int:movie_id>/',views.similar_movie), # 비슷한 영화
    path('similar/detail/<int:movie_id>/',views.similar_detail), # 비슷한 영화
    path('search/<title>/', views.search_movie), # 영화 서치
]