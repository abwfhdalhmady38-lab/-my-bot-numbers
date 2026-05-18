import telebot
import requests

# التوكن الخاص ببوتك تم وضعه بنجاح 🚀
TOKEN = '8805818191:AAGF1p4Xw6RvV_qkz9mY-BfSgIuwdpJhfc8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك في بوت الأرقام الوهمية المجاني! 🚀\nاضغط على /get_number للحصول على رقم وهمي مؤقت.")

@bot.message_handler(commands=['get_number'])
def get_number(message):
    bot.reply_to(message, "جاري سحب رقم مجاني... انتظر لحظة 🔄")
    
    # البوت يتصل بموقع أرقام مجاني ويجيب منه الرقم
    try:
        # رابط لموقع أرقام مجانية عامة
        response = requests.get('https://smsreceivefree.com/api/v1/countries/usa/numbers') 
        if response.status_code == 200:
            data = response.json()
            # سحب أول رقم متاح من القائمة
            number = data[0].get('number', 'لا توجد أرقام متوفرة حالياً!')
            bot.reply_to(message, f"رقمك الوهمي الجاهز هو: \n`{number}`\n\n(ملاحظة: هذا رقم عام ومجاني لاستقبال الأكواد)")
        else:
            bot.reply_to(message, "الموقع المجاني مضغوط حالياً، جرب تطلب مرة ثانية!")
    except:
        bot.reply_to(message, "عذراً، حدث خطأ أثناء الاتصال بسيرفر الأرقام. جرب لاحقاً!")

bot.polling()

