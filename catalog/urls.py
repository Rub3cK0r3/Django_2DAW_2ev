from django.urls import path,include
from . import views

app_name = 'catalog' # En esta implementacion he añadido ya de antemano los namespaces para prever futuras implementaciones

urlpatterns = [
    path('', views.index, name='index'),

    path('books/',views.BookListView.as_view(),name='books'),
    path('authors/',views.AuthorListView.as_view(),name='authors'),
    path('book/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    path('author/<int:pk>/',views.AuthorDetailView.as_view(),name='author_detail'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew_book_librarian'),
]

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all_borrowed'),
]

urlpatterns += [
    path('registro/',views.register,name='registro_usuarios'),
]

urlpatterns += [
    path('permisos/nuevo/',views.registro_permisos,name='registro_permisos'),
]

# si no te digo nada se tiene que llamar como la pregunta
urlpatterns += [
    path('preg4/<int:pk>',views.asignar_permiso_usuario,name='asignacion_permisos_usuario'),
]

urlpatterns += [
    path('preg5/<int:pk>',views.PerfilDetailView.as_view(),name='perfil_detail'),
]

urlpatterns += [
    path('perfiles/',views.PerfilListView.as_view(),name='lista_perfiles'),
]