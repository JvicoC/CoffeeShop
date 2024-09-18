from django.urls import path
from .views import ProductFormView, ProductListView, ProductEditView


urlpatterns = [
    path('', ProductListView.as_view(), name="list_product"),
    path('agregar/', ProductFormView.as_view(), name="add_product"),
    path('editar/', ProductEditView.as_view(), name="edit_product"),
] 