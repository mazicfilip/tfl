from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render

from .models import Product


class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'qs': queryset
#     }
#     return render(request, "product/list.html", context)


# class ProductDetailView(DetailView):
#     template_name = "products/detail.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         return context
#
#     def get_object(self, *args, **kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         instance = Product.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Product doesn't exist!")
#         return instance

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = Product.objects.get_by_id(slug)
        #if instance is None:
        #    raise Http404("Product doesn't exist!")
        #return instance
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Product doesn't exist!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhh")
        return instance
