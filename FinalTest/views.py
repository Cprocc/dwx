from django.shortcuts import render
from FinalTest.utils import mysqlhelper
# Create your views here.


# def index(request):
#     return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def commerce(request):
    return render(request, 'e_commerce.html')


def projects(request):
    return render(request, 'projects.html')


def Apple(request):
    return render(request, 'APPLE.html')


def Huawei(request):
    return render(request, 'HUAWEI.html')


def XiaoMi(request):
    return render(request, 'XIAOMI.html')


def query_mobile(request):
    # 定义一个字典存储查询的条件
    res = {'name': ""}
    # 判断是HTTP请求的什么方法？
    if request.method == "GET":  # 访问首页，获取所有天气信息
        # 去数据库中把所有城市今天天气取出来
        sql = """
                Select PName, Price,Argument, Month_Sale,Image,Detail_Url
            from tmall """
    else:
        # 正在响应查询的请求--POST
        # 接收前端传递过来的数据
        res = request.POST  # res['city']
        # 拼接SQL语句
        sql = """
                       Select PName, Price,Argument, Month_Sale,Image,Detail_Url
                   from tmall where Mobile_Name Like '%s'
                   """ % ("%" + res['name'] + '%')
    # sql = """
    #     Select Mobile_Name, Price,Argument, Month_Sale,Image,Detail_Url
    #     from tmall """
    # 运行获取结果
    response = mysqlhelper.get_db_data(sql)
    # 携带数据加载HTML
    return render(request, 'tables_dynamic.html', {'mobiles': response['data']})


def Volg(request):
    return render(request, 'vlog.html')

