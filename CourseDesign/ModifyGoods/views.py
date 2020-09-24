from django.shortcuts import render
from django.http import HttpResponseRedirect
from Model.models import Commodity
# Create your views here.
import oss2


def modifyGoods(requests):
    id = requests.GET.get('id')
    tmp = Commodity.objects.filter(id=id)[0]
    datas = {'ID': id, 'Name': tmp.name, 'Price': tmp.price, 'Description': tmp.description, 'image': "https://database-design.oss-cn-beijing.aliyuncs.com/" + str(id) + ".jpg"}
    return render(requests, 'ModifyGoods.html', {'datas': datas})


def modifyResult(requests):
    itemName = requests.POST.get('itemName')
    itemPrice = requests.POST.get('itemPrice')
    itemDescription = requests.POST.get('itemDescription')
    id = requests.GET.get('id')
    key = 'LTAI4FzSxsTG9WmSi4UhykiP'
    password = 'FPI6XHyeybIFahASoJzQ30YBzd6yjK'
    auth = oss2.Auth(key, password)
    endpoint = "http://oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, 'database-design')
    itemImage = requests.FILES.get("itemImage")
    try:
        print("id = ", id)
        item = Commodity.objects.filter(id=id).update(name=itemName, price=itemPrice, description=itemDescription)
        return HttpResponseRedirect('/studentinfo')
    except Exception as e:
        return render(requests, 'return.html',
                      {'message': "修改失败，请检查输入", 'href': "/studentinfo"})