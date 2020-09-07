from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage, BaseSize, DatetimePickerTemplateAction, MessageImagemapAction, ImagemapArea, URIImagemapAction, ImagemapSendMessage, VideoSendMessage, AudioSendMessage, MessageAction, QuickReplyButton, QuickReply, LocationSendMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
import datetime

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def information(event):  #店家資訊
    try:
        message = [
            TextSendMessage(text='清澄甜點製造所隨時歡迎您的光臨！\n我們每天都提供不一樣的手作糕點，各位喜愛甜食的饕客們趕快來享受午茶時光吧🍰'),
            TextSendMessage(
                text = '☎️電話：03-4650020\n\n⏰營業時間：12:00-20:00（舒芙蕾鬆餅與餐點供應至19:00）\n\n❗低消為一個品項(100元以上)，免服務費\n\n❗尖峰時刻(客滿)用餐時間限2小時',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '地址查詢', text = '地址查詢')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def address(event):  #店家資訊
    try:
        message = [
            LocationSendMessage(
                title = '清澄甜點製造所',
                address = '中壢區大仁五街34號',
                latitude = 24.956782,
                longitude = 121.240285
            )   #LocationSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def menu(event):  #美味菜單
    try:
        message =[
            TemplateSendMessage(
                alt_text='轉盤樣板',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://i.ibb.co/Gv6YHkj/drink.jpg',
                            title='飲品',
                            text='請選擇：',
                            actions=[
                                MessageTemplateAction(
                                    label='茶飲',
                                    text='茶飲'
                                ),
                                MessageTemplateAction(
                                    label='咖啡',
                                    text='咖啡'
                                ),
                                MessageTemplateAction(
                                    label='多多/氣泡飲',
                                    text='多多/氣泡飲'
                                ),
                            ]   #actions
                        ),  #CarouselColumn
                        CarouselColumn(
                            thumbnail_image_url='https://i.ibb.co/1fQzGVX/dessert.jpg',
                            title='點心',
                            text='請選擇：',
                            actions=[
                                MessageTemplateAction(
                                    label='炸物',
                                    text='炸物'
                                ),
                                MessageTemplateAction(
                                    label='點心',
                                    text='點心'
                                ),
                                MessageTemplateAction(
                                    label='舒芙蕾',
                                    text='舒芙蕾'
                                ),
                            ]   #actions
                        ),   #CarouselColumn
                        CarouselColumn(
                            thumbnail_image_url='https://i.ibb.co/Pzr77Kb/Staple.jpg',
                            title='主食',
                            text='請選擇：',
                            actions=[
                                MessageTemplateAction(
                                    label='厚片吐司',
                                    text='厚片吐司'
                                ),
                                MessageTemplateAction(
                                    label='千層麵',
                                    text='千層麵'
                                ),
                                MessageTemplateAction(
                                    label='義大利麵',
                                    text='義大利麵'
                                ),
                            ]   #actions
                        ),   #CarouselColumn
                    ]   #columns
                )   #CarouselTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def tea(event): #茶飲
    try:
        message = [
            FlexSendMessage(
                alt_text="茶飲",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "TEA",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "花果茶飲",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          },
                          {
                            "type": "text",
                            "text": "hot",
                            "align": "end",
                            "color": "#005f6b",
                            "weight": "bold",
                            "size": "md"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "洋甘菊菩提茶",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "140",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "玫瑰紅棗茶",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "140",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "山竹甜菊茶",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "140",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "薰衣草甜菊茶",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "150",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "玫瑰洛神茶",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "150",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "果茶",
                                "size": "md",
                                "weight": "bold",
                                "color": "#005f6b"
                              },
                              {
                                "type": "text",
                                "text": "ice/hot",
                                "align": "end",
                                "color": "#005f6b",
                                "weight": "bold",
                                "size": "md"
                              }
                            ]
                          },
                          {
                            "type": "separator",
                            "margin": "sm"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "柚子蜜茶",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "120",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "蜂蜜蘋果茶",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "120",
                                    "size": "sm",
                                    "color": "#008c9e",
                                    "align": "end"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "葡萄柚果茶(ice)",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "130",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "熱帶水果茶",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "130",
                                    "color": "#008c9e",
                                    "size": "sm",
                                    "align": "end"
                                  }
                                ]
                              }
                            ],
                            "spacing": "sm",
                            "margin": "md"
                          }
                        ],
                        "margin": "xxl"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "果乾茶",
                                "color": "#005f6b",
                                "size": "md",
                                "weight": "bold"
                              }
                            ]
                          },
                          {
                            "type": "separator",
                            "margin": "sm"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "補水果乾茶",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "80",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "美顏果乾茶",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "80",
                                    "size": "sm",
                                    "color": "#008c9e",
                                    "align": "end"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "淨白果乾茶",
                                    "size": "sm",
                                    "color": "#008c9e"
                                  },
                                  {
                                    "type": "text",
                                    "text": "80",
                                    "align": "end",
                                    "size": "sm",
                                    "color": "#008c9e"
                                  }
                                ]
                              }
                            ],
                            "spacing": "sm",
                            "margin": "md"
                          }
                        ],
                        "margin": "xxl"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def coffee(event): #咖啡
    try:
        message = [
            FlexSendMessage(
                alt_text="咖啡",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "COFFEE",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "咖啡",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          },
                          {
                            "type": "text",
                            "text": "ice/hot",
                            "align": "end",
                            "color": "#005f6b",
                            "weight": "bold",
                            "size": "md"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "美式咖啡",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "90",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "卡布奇諾",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "130",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "原味拿鐵",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "130",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "榛果拿鐵",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "140",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "香草拿鐵",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "140",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "抹茶拿鐵",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "150",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "摩卡拿鐵",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "150",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "焦糖瑪奇朵",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "150",
                                "align": "end",
                                "color": "#008c9e",
                                "size": "sm"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "歐蕾",
                                "size": "md",
                                "weight": "bold",
                                "color": "#005f6b"
                              },
                              {
                                "type": "text",
                                "text": "ice/hot",
                                "align": "end",
                                "color": "#005f6b",
                                "weight": "bold",
                                "size": "md"
                              }
                            ]
                          },
                          {
                            "type": "separator",
                            "margin": "sm"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "紅茶歐蕾",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "130",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "黑糖歐蕾",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "130",
                                    "size": "sm",
                                    "color": "#008c9e",
                                    "align": "end"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "可可歐蕾",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "150",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "抹茶歐蕾",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "150",
                                    "color": "#008c9e",
                                    "size": "sm",
                                    "align": "end"
                                  }
                                ]
                              }
                            ],
                            "spacing": "sm",
                            "margin": "md"
                          }
                        ],
                        "margin": "xxl"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def bubble(event): #多多/氣泡飲
    try:
        message = [
            FlexSendMessage(
                alt_text="多多/氣泡飲",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "YAKULT/SPARKLING",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "多多",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          },
                          {
                            "type": "text",
                            "text": "ice",
                            "align": "end",
                            "color": "#005f6b",
                            "weight": "bold",
                            "size": "md"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "綠茶多多",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "110",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "檸檬多多",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "120",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "百香多多",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "120",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "鮮奶多多",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "120",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "氣泡飲",
                                "size": "md",
                                "weight": "bold",
                                "color": "#005f6b"
                              },
                              {
                                "type": "text",
                                "text": "ice",
                                "align": "end",
                                "color": "#005f6b",
                                "weight": "bold",
                                "size": "md"
                              }
                            ]
                          },
                          {
                            "type": "separator",
                            "margin": "sm"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "黑莓泡泡",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "160",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "百香泡泡",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "160",
                                    "size": "sm",
                                    "color": "#008c9e",
                                    "align": "end"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "蘋果泡泡",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "160",
                                    "align": "end",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "黑醋栗泡泡",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "160",
                                    "color": "#008c9e",
                                    "size": "sm",
                                    "align": "end"
                                  }
                                ]
                              },
                              {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "葡萄柚泡泡",
                                    "color": "#008c9e",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "text",
                                    "text": "160",
                                    "size": "sm",
                                    "color": "#008c9e",
                                    "align": "end"
                                  }
                                ]
                              }
                            ],
                            "spacing": "sm",
                            "margin": "md"
                          }
                        ],
                        "margin": "xxl"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def fry(event): #炸物
    try:
        message = [
            FlexSendMessage(
                alt_text="炸物",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "FRIED FOODS",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "炸物",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "薯條",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "薯餅",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "奶油玉米可樂餅",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "乳酪棒",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "100",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def dessert(event): #點心
    try:
        message = [
            FlexSendMessage(
                alt_text="點心",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "DESSERT",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "甜點",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "熔岩巧克力",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "140",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "閃電泡芙",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "text",
                                "text": "每日限量甜點請在蛋糕櫃挑選",
                                "size": "sm",
                                "color": "#008c9e"
                              }
                            ],
                            "margin": "xl"
                          }
                        ],
                        "margin": "md"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def souffle(event): #舒芙蕾
    try:
        message = [
            FlexSendMessage(
                alt_text="舒芙蕾",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "SOUFFLE",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "舒芙蕾",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "原味香草",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "190",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "巧克力可可",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "220",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "抹茶紅豆",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "230",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "水果優格",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "230",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "綜合野莓",
                                "color": "#008c9e",
                                "size": "sm"
                              },
                              {
                                "type": "text",
                                "text": "230",
                                "color": "#008c9e",
                                "size": "sm",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def thick_cut_toast(event): #厚片
    try:
        message = [
            FlexSendMessage(
                alt_text="厚片",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "THICK CUT TOAST",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "厚片吐司",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "抹茶麻糬",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "花生起司",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "牛奶黑糖麻糬",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "巧克力焦糖杏仁",
                                "size": "sm",
                                "color": "#008c9e"
                              },
                              {
                                "type": "text",
                                "text": "70",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def lasagna(event): #千層麵
    try:
        message = [
            FlexSendMessage(
                alt_text="千層麵",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "LASAGNA",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "千層麵",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "雙醬菠菜千層麵",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "230",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "塔香野菇千層麵",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "230",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def pasta(event): #義大利麵
    try:
        message = [
            FlexSendMessage(
                alt_text="義大利麵",
                contents=
                {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "RECEIPT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                      },
                      {
                        "type": "text",
                        "text": "PASTA",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "md",
                        "color": "#005f6b"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "義大利麵",
                            "color": "#005f6b",
                            "size": "md",
                            "weight": "bold",
                            "align": "start"
                          }
                        ],
                        "margin": "md"
                      },
                      {
                        "type": "separator",
                        "margin": "sm"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "奶油香草野菇義大利麵",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "230",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "香濃起司鮮蔬義大利麵",
                                "size": "sm",
                                "color": "#008c9e",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "240",
                                "size": "sm",
                                "color": "#008c9e",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "md"
                      }
                    ]
                  },
                  "styles": {
                    "footer": {
                      "separator": True
                    }
                  }
                }
            ),   #FlexSendMessage
            TextSendMessage(
                text = '想看看其他餐點嗎？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '其他美味餐點', text = '其他美味餐點')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def order(event): #確認點餐
    try:
        message = [
            TemplateSendMessage(
                alt_text='按鈕樣版',
                template=ConfirmTemplate(
                    text='您要購買此項產品嗎？',
                    actions=[
                        PostbackTemplateAction(
                            label='是',
                            data='action=yes'
                        ),   #MessageTemplateAction
                        PostbackTemplateAction(
                            label='否',
                            data='action=no'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ConfirmTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def yes_order(event,backdata): #點餐
    try:
        message = (
            TextSendMessage(text='感謝您的購買，我們將盡快製作您的餐點🙋')
        )   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def no_order(event,backdata): #不點餐
    try:
        message = (
            TextSendMessage(text='今天不想要吃他嗎？沒關係我們還有很多餐點供您選擇🙆')
        )   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
