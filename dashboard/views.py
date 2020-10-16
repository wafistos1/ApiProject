from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from accounts.models import ClientUser
from shop.models import Store, Product
from store.models import OrderProduct, Orders
# Create your views here.


class dashboroadView(TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_OrdersProduct"] = OrderProduct.objects.all().count()
        context["count_Orders"] = Orders.objects.all().count()
        context["count_cilent"] = ClientUser.objects.all().count()
        context["count_Product"] = Product.objects.all().count()
        context["qs"] = Orders.objects.all()
        # qs = Orders.objects.all()
        # Turnover  = 0
        # for order in qs:
        #     Turnover += order.get_total()
        # context["Turnover"] = Turnover
        
        return context

class dashView(APIView):
    
    authentication_classes = []
    permission_classes = []

    
    def get(self, request, format=None):
        
        qs_count = ClientUser.objects.all().count()
        print(qs_count)
        labels = ['Users', 'blue', 'Yellow', 'Green', 'Orange']
        defautl_items = [qs_count, 234, 342, 343, 323]
        context = {
            'counts': labels,
            'defaul': defautl_items,
            'users': 'Wafi',
            }
        return Response(context)
    