from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, PostbackEvent
from module import func
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '店家資訊':
                        func.information(event)

                    elif mtext == '地址查詢':
                        func.address(event)

                    elif mtext == '美味菜單':
                        func.menu(event)

                    elif mtext == '其他美味餐點':
                        func.menu(event)

                    elif mtext == '茶飲':
                        func.tea(event)

                    elif mtext == '咖啡':
                        func.coffee(event)

                    elif mtext == '多多/氣泡飲':
                        func.bubble(event)

                    elif mtext == '炸物':
                        func.fry(event)

                    elif mtext == '點心':
                        func.dessert(event)

                    elif mtext == '舒芙蕾':
                        func.souffle(event)

                    elif mtext == '厚片吐司':
                        func.thick_cut_toast(event)

                    elif mtext == '千層麵':
                        func.lasagna(event)

                    elif mtext == '義大利麵':
                        func.pasta(event)

                    elif mtext == '洋甘菊菩提茶':
                        func.order(event)

                    elif mtext == '玫瑰紅棗茶':
                        func.order(event)

                    elif mtext == '山竹甜菊茶':
                        func.order(event)

                    elif mtext == '薰衣草甜菊茶':
                        func.order(event)

                    elif mtext == '玫瑰洛神茶':
                        func.order(event)

                    elif mtext == '柚子蜜茶':
                        func.order(event)

                    elif mtext == '蜂蜜蘋果茶':
                        func.order(event)

                    elif mtext == '葡萄柚果茶':
                        func.order(event)

                    elif mtext == '熱帶水果茶':
                        func.order(event)

                    elif mtext == '補水果乾茶':
                        func.order(event)

                    elif mtext == '美顏果乾茶':
                        func.order(event)

                    elif mtext == '淨白果乾茶':
                        func.order(event)

                    elif mtext == '美式咖啡':
                        func.order(event)

                    elif mtext == '卡布奇諾':
                        func.order(event)

                    elif mtext == '原味拿鐵':
                        func.order(event)

                    elif mtext == '榛果拿鐵':
                        func.order(event)

                    elif mtext == '香草拿鐵':
                        func.order(event)

                    elif mtext == '抹茶拿鐵':
                        func.order(event)

                    elif mtext == '摩卡拿鐵':
                        func.order(event)

                    elif mtext == '焦糖瑪奇朵':
                        func.order(event)

                    elif mtext == '紅茶歐蕾':
                        func.order(event)

                    elif mtext == '黑糖歐蕾':
                        func.order(event)

                    elif mtext == '可可歐蕾':
                        func.order(event)

                    elif mtext == '抹茶歐蕾':
                        func.order(event)

                    elif mtext == '綠茶多多':
                        func.order(event)

                    elif mtext == '檸檬多多':
                        func.order(event)

                    elif mtext == '百香多多':
                        func.order(event)

                    elif mtext == '鮮奶多多':
                        func.order(event)

                    elif mtext == '黑莓泡泡':
                        func.order(event)

                    elif mtext == '百香泡泡':
                        func.order(event)

                    elif mtext == '蘋果泡泡':
                        func.order(event)

                    elif mtext == '黑醋栗泡泡':
                        func.order(event)

                    elif mtext == '葡萄柚泡泡':
                        func.order(event)

                    elif mtext == '薯條':
                        func.order(event)

                    elif mtext == '薯餅':
                        func.order(event)

                    elif mtext == '奶油玉米可樂餅':
                        func.order(event)

                    elif mtext == '乳酪棒':
                        func.order(event)

                    elif mtext == '熔岩巧克力':
                        func.order(event)

                    elif mtext == '閃電泡芙':
                        func.order(event)

                    elif mtext == '當日限量糕點':
                        func.order(event)

                    elif mtext == '原味香草':
                        func.order(event)

                    elif mtext == '巧克力可可':
                        func.order(event)

                    elif mtext == '抹茶紅豆':
                        func.order(event)

                    elif mtext == '水果優格':
                        func.order(event)

                    elif mtext == '綜合野莓':
                        func.order(event)

                    elif mtext == '抹茶麻糬':
                        func.order(event)

                    elif mtext == '花生起司':
                        func.order(event)

                    elif mtext == '牛奶黑糖麻糬':
                        func.order(event)

                    elif mtext == '巧克力焦糖杏仁':
                        func.order(event)

                    elif mtext == '雙醬菠菜千層麵':
                        func.order(event)

                    elif mtext == '塔香野菇千層麵':
                        func.order(event)

                    elif mtext == '奶油香草野菇義大利麵':
                        func.order(event)

                    elif mtext == '香濃起司鮮蔬義大利麵':
                        func.order(event)


            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得data資料
                if backdata.get('action') == 'yes':
                    func.yes_order(event, backdata)
                elif backdata.get('action') == 'no':
                    func.no_order(event, backdata)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
