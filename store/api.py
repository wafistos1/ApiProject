from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
# third party imports
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import authentication

# Logics
from .serializers import (
    OrdersSerializer,
    OrderProductSerializer,
    OrderProductUpdateSerializer,
    OrdersAdminSerializer,
    OrderProductAdminSerializer,
    )

from .models import Orders, OrderProduct
from accounts.models import ClientUser

# Logics
from shop.serializers import  ProductSerializer, StoreSerializer
from shop.models import Product, Store
from accounts.models import ClientUser


class ProductOrdersAdminView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request, format=None):
        qs = OrderProduct.objects.all()
        orders = OrderProductAdminSerializer(qs,  many=True)
        message = f'All OrderProducts'
        count = qs.count()
        context = {
            'Message': message,
            'Count': f'Count all orders: {count}',
            'item': orders.data,
        }
        return Response(context)


class OrdersAdminView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self, request, format=None):
       
        qs = Orders.objects.all()
        orders = OrdersAdminSerializer(qs,  many=True)
        count = qs.count()
        message = f'All Order'
        context = {
            'Message': message,
            'Count': f'Count all orders: {count}',
            'orders': orders.data
        }
        return Response(context)
    
    
class AddItemCartView(APIView):
    """ Post :Add item in cart
        Get  :List item in cart

    Args:
        APIView ([type]): [description]
    """
    serializer_class = OrderProductSerializer
    
    
    def post(self, request ):
        serializer = OrderProductSerializer(data=request.data)
        if serializer.is_valid():
            # name = serializer.data.get('name')
            client = get_list_or_404(ClientUser, user=request.user)
            kitten_kwargs = serializer.validated_data
            orderProduct = OrderProduct(**kitten_kwargs)
            orderProduct.client = client[0]
            orderProduct.save()
            item = f'Item: {orderProduct.item.name} By {orderProduct.client.user.username.upper()}'
            context = {
                'message': 'item add successfully ',
                'Add Item': item,
                'Status': 'status.HTTP_200',
                }
            return Response(context)
        else:
            context = {
                'Alert': 'item add error ',
                'message': serializer.errors,
                'Status': 'status.HTTP_400 Bad Request',
                }
            return Response(context)

    
    def get(self, request, format=None):
        client = get_list_or_404(ClientUser, user=request.user)
        qs = OrderProduct.objects.filter(client=client[0]) 
        products = OrderProductSerializer(qs, many=True)
        message = f'All  {client[0].user.username.upper()} OrdersProducts'
        context = {
            'Message': message,
            'items': products.data,
            'Status': 'status.HTTP_200 ',
        }
        return Response(context)
        

class updateDeleteItemCartView(APIView):
    """ Put: update item in cart
        Delete: delete item in cart

    Args:
        APIView ([type]): [description]
    """
    
    serializer_class = OrderProductSerializer
    def get_object(self, pk):
        try:
            return OrderProduct.objects.get(pk=pk)
        except OrderProduct.DoesNotExist:
            raise Http404
    
      
    def put(self, request, pk, format=None):
        client = get_list_or_404(ClientUser, user=request.user)
        update_OrderProduct = self.get_object(pk)
        serializer = OrderProductUpdateSerializer(update_OrderProduct, data=request.data)
        
        if serializer.is_valid():
            if update_OrderProduct.client == client[0]:
                kitten_kwargs = serializer.validated_data
                orderProduct = OrderProduct(**kitten_kwargs)
                orderProduct.client = client[0]
                orderProduct.save()
                item = f'Product: {orderProduct.item.name} as updated with quantity:{orderProduct.quatity}'
                context = {
                    'Message': 'item update successfully ',
                    'Item': item,
                    'Status': 'status.HTTP_200',
                }
                return Response(context)
            else:
                context = {
                    'Alert': 'Unauthorized',
                    'Status': 'status.HTTP_401',
                }
                return Response(context) 
        else:
            context = {
                    'Alert': 'Not valid fields',
                    'message': serializer.errors,
                    'Status': 'status.HTTP_412 Precondition Failed',
                }
            return Response(context)
    
    def delete(self, request, pk, format=None):
        client = get_list_or_404(ClientUser, user=request.user)
        delete_OrderProduct = self.get_object(pk)

        if delete_OrderProduct.client == client[0]:
            delete_OrderProduct.delete()
            context = {
                'Message': 'item Deleted successfully ',
                
                'Status': 'status.HTTP_204_NO_CONTENT',
                }
            return Response(context)
        else:
            context = {
                'Alert': 'Request Unauthorized ',
                'Status': 'status.HTTP_401 Unauthorized',
                }
            return Response(context)
 
 
class OrderCreateUserView(APIView):
    """Post: Create Order by user
       Get: Get All orders of user      
    Args:
        APIView ([type]): [description]
    """
    def get_client(self):
        try:
            return Orders.objects.get(user=self.request.user)
        except Orders.DoesNotExist:
            raise Http404
        
    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            kitten_kwargs = serializer.validated_data
            # if kitten_kwargs['shipping_address'] is None:
            #     kitten_kwargs['shipping_address'] = 
            order = Orders(**kitten_kwargs)
            client = get_list_or_404(ClientUser, user=request.user)
            order.client = client[0]
            items = OrderProduct.objects.filter(client=client[0], selected=False)
            print(items)
            order.save()
            for item in items:
                order.items.add(item)
                item.selected = True
                item.quatity -= 1
                item.save()
            message = f'Order: {order.pk} add By {order.client.user.username.upper()}'
            context = {
                'message': 'Order add successfully ',
                'Add Item': message,
                'Status': 'status.HTTP_200',
                }
            return Response(context)
        else:
            context = {
                'Alert': 'Order add error ',
                'message': serializer.errors,
                'Status': 'status.HTTP_400 Bad Request',
                }
            return Response(context)
            
            
    def get(self, request):
        client = get_list_or_404(ClientUser, user=request.user)
        qs = Orders.objects.filter(client=client[0]) 
        products = OrdersSerializer(qs, many=True)
        
        message = f'All  {client[0].user.username.upper()} Orders'
        
        context = {
            'Message': message,
            'Orders': products.data,
            'Status': 'status.HTTP_200 ',
        }
        return Response(context)


class UpdateOrderUserView(APIView):
    """PUT: update oders by user
       DELETE: delete order By User      
    Args:
        APIView ([type]): [description]
    """
    
    def get_object(self, id):
        try:
            return Orders.objects.get(id=id)
        except Orders.DoesNotExist:
            raise Http404
    
    def delete(self, request, id, format=None):
        client = get_list_or_404(ClientUser, user=request.user)
        delete_Order = self.get_object(id)

        if delete_Order.client == client[0]:
            delete_Order.delete()
            context = {
                'Message': 'item Deleted successfully ',
                
                'Status': 'status.HTTP_204_NO_CONTENT',
                }
            return Response(context)
        else:
            context = {
                'Alert': 'Request Unauthorized ',
                'Status': 'status.HTTP_401 Unauthorized',
                }
            return Response(context)


