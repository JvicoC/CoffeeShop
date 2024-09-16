from django.urls import reverse_lazy
from django.views import generic
from products.models import Product
from .forms import ProductForm, ProductFormEdit


class ProductFormView(generic.FormView):
    template_name="products/add_product.html"
    form_class=ProductForm
    success_url=reverse_lazy('list_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class ProductListView(generic.ListView):
    model=Product
    template_name="products/list_product.html"
    context_object_name='products'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class ProductEditView(generic.FormView):
    model=Product
    template_name="products/edit_product.html"
    form_class=ProductFormEdit
    context_object_name='products'
    success_url=reverse_lazy('list_product')

    def form_valid(self, form):
        form.update(3)
        return super().form_valid(form)