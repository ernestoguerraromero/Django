from rest_framework import mixins, viewsets

from . import models
from . import serializers

from django.http import HttpResponse
from rest_framework import status, response
from rest_framework.decorators import api_view
from django.http import JsonResponse



class AccountViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
        API endpoint that allows accounts to be viewed.

        list:
        Return all the accounts available.

        create:
        Create an account.

        retrieve:
        Return a given account.
    """
    model = models.Account
    # serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()

    def get_serializer_class(self):
        serializer_class = serializers.AccountSerializer

        if self.action == 'update':
            serializer_class=serializers.AccountSerializer_Per_Update
            return serializer_class
        return serializer_class
    def update(self, request, pk):
        super().update(request, pk)
        account=self.get_object()
        serializers.AccountSerializer(account)
        return response.Response(data=serializers.AccountSerializer(account).data, status=status.HTTP_200_OK)

@api_view(["GET"])
def fizz_buzz(request):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    x=request.query_params.get('x',100)
    #l={"x": 100, "fizzbuzz": f(int(x))}
    l={"x": 100, "fizzbuzz": ''.join(str(e) for e in fizzbuzzSec(x))}
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    #return response.Response(data=l)
    return response.Response(data=l, status=status.HTTP_200_OK)

def fizzbuzzSec(x):
    return [fizzbuzzN(n) for n in range(1,x)]

def fizzbuzzN(n):
    r=n
    if(n%3==0 and n%5==0):
        r="FizzBuzz"
    else: 
        if(n%3==0):
            r="Fizz" 
        else: 
            if(n%5==0):
                r="Buzz"
    return r

def f(n):
    s = ''
    for i in range(1, n+1):
        if i % 15 == 0:
            s+= 'FizzBuzz'
        elif i % 3 == 0:
            s += 'Fizz'
        elif i % 5 == 0:
            s += 'Buzz'
        else:
            s += str(i)
    return s 


