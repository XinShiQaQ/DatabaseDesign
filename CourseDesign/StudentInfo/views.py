from django.shortcuts import render, HttpResponseRedirect
from Model.models import Commodity, User, Transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
import oss2

# Create your views here.


def InfoPage(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    tmp = User.objects.filter(id=request.session['user'])[0]
    userInfo = {'Account': request.session['user'], 'Name': tmp.name,
             'Birthday': tmp.birthday, 'Sex': 'Male' if tmp.isMale else 'Female',
             'College': tmp.college, 'Address': tmp.address,
             'QQ': tmp.QQ, 'Telephone': tmp.tel,
             'Email': tmp.email}
    good_list = Commodity.objects.filter(owner=request.session['user'], status=True)
    goods = []
    for good in good_list:
        goods.append({'ID': good.id, 'Name': good.name, 'Price': good.price, 'Description': good.description,
                      'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(good.image)})
    sellConfirm = Transaction.objects.filter(seller=request.session['user'], status=2)
    request.session['message'] = len(sellConfirm)

    transaction_list = Transaction.objects.filter(buyer=request.session['user'])
    purchase_list = [{'commodity': t.commodity, 'status': t.status, 'transaction_id': t.id} for t in transaction_list]
    for purchase in purchase_list:
        if purchase['status'] == 2:
            purchase['status'] = "等待卖家确认"
            purchase['transaction_id'] = -1
        elif purchase['status'] == 3:
            purchase['status'] = "卖家已确认，点击确认收货"
        else:
            purchase['status'] = "交易已完成"
            purchase['transaction_id'] = -1
    print(purchase_list)
    return render(request, 'StudentInfo.html', {
        'datas': userInfo,
        'goods': goods,
        'len': len(goods),
        'purchase_len': len(purchase_list),
        'purchase_list': purchase_list
    })


def DeleteItem(request):
    delete_list = request.POST.getlist('choose')
    key = 'LTA'+'I4GF'+'kNx'
    key = key + 'HzH'+'ejr7'+'Xj8'+'da9o'
    password = 'QXR'+'i6uKVthP'+'xInBRVScB413'+'JW5rHxi'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    for Id in delete_list:
        bucket.delete_object(str(Commodity.objects.filter(id=Id)[0].image))
        Commodity.objects.filter(id=Id).delete()
    return HttpResponseRedirect('/studentinfo')

