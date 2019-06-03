from django.forms import CheckboxSelectMultiple, ModelForm
from django.shortcuts import render
from django.urls import reverse

from .models import ProductforWeek
from core.models import Product, Supplier
# Create your views here.
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, DeleteView


def index(request):
    return render(request, 'supplier_base_template.html')


class SupplierView(CreateView):
    template_name = "supplier/supplier_form.html"
    model = ProductforWeek
    fields = ('products','date')
    def get_context_data(self, **kwargs):
        supplier = Supplier.objects.filter(user=self.request.user)
        data = super(SupplierView, self).get_context_data(**kwargs)
        print(supplier[0].id)
        data['products'] = Product.objects.filter(supplier=supplier[0].id)
        print(data['products'])
        return data


class SupplierUpdateView(UpdateView):
    template_name ="supplier/supplier_update_form.html"
    model = ProductforWeek
    fields = ('products',)

    def get_context_data(self, **kwargs):
        supplier = Supplier.objects.filter(user=self.request.user)
        data = super(SupplierUpdateView,self).get_context_data(**kwargs)
        data['supply'] = ProductforWeek.objects.filter(active=True)
        data['products'] = Product.objects.filter(supplier=supplier[0].id).filter(active=True)
        selected = ProductforWeek.objects.prefetch_related("products").filter(active=True)
        sp = []
        for p in selected[0].products.all():
            sp.append(p.id)
        data["sp"] = sp

        return data
    def get_absolute_url(self):
        return reverse('supplier')


class SupplierDetailView(TemplateView):
    template_name ="supplier/supplier_form_detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(SupplierDetailView, self).get_context_data(*args, **kwargs)
        data = ProductforWeek.objects.filter(active=True)
        context['data'] = data[0]
        print(data[0])
        return context

class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('supplier',)


class CreateProductView(CreateView):
    model = Product
    template_name = 'supplier/supplier_product_form.html'
    form_class = CreateProductForm
    success_url = '/supplier'

    def form_valid(self, form):
        supplier = Supplier.objects.filter(user=self.request.user)
        form.instance.supplier = supplier[0]
        form.instance.save()
        return super(CreateProductView, self).form_valid(form)

class UpdateProductView(UpdateView):
    model = Product
    form_class = CreateProductForm
    success_url = '/supplier'
    template_name = 'supplier/supplier_product_update_form.html'

