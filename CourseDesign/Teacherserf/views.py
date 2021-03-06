from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User, Transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
import oss2

def GoodInfo(request):
    good_list = Commodity.objects.filter(status=True)
    goods = []
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price, 'Description': good.description, 'Owner':good.owner,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.image)})
    trans_list2 = Transaction.objects.filter(status=2)
    trans2 = []
    for trans in trans_list2:
        trans2.append({'ID': trans.id, 'Buyer': trans.buyer, 'Seller': trans.seller, 'Comment': trans.comment})

    trans_list3 = Transaction.objects.filter(status=3)
    trans3 = []
    for trans in trans_list3:
        trans3.append({'ID': trans.id, 'Buyer': trans.buyer, 'Seller': trans.seller, 'Comment': trans.comment})
    return render(request, 'teachers.html', {
        'trans2': trans2,
        'trans3': trans3,
        'goods': goods,
    })
def Delete(request):
    id=request.GET.get('id')
    Commodity.objects.get(id=id).delete()
    return HttpResponseRedirect("/teachers")



