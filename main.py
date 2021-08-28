from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from Buttons import *
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler

admins = [881319779, 611003999]

state_main = 1
state_task_check = 2
state_task1 = 3
state_task2 = 4
state_task3 = 5
state_task4 = 6
state_photo = 7
state_photo_get = 8
state_phone = 9
state_mintaqa = 10


def start(update: Update, context: CallbackContext) -> None:
    users = get_users()
    update.message.reply_text(f'Assalomu alaykum  {update.effective_user.first_name}\n'
                              f'HOMEXPO mahsulot zakaz berish platformasiga xush kelibsiz!\nQuyidagi buyruqlardan birini tanlang👇👇',
                              reply_markup=main_buttons())
    all_users = []
    for i in users:
        all_users.append(i[0])
    if update.effective_user.id not in all_users:
        first_name = update.effective_user.first_name
        id = update.effective_user.id
        username = update.effective_user.username
        add_user(first_name, id, username)
        message = f'Foydalanuvchilar soni: {len(users)}\nIsmi: {first_name}\n' \
                  f'chat_id: {id}\n' \
                  f'username: {username}\n' \
                  f'Botga start berdi'
        context.bot.send_message(chat_id=881319779,
                                 text=message)
    return state_main


def back(update, context):
    update.message.reply_text('o\'zingiz uchun kerakli bo\'lgan buyruqlardan birini tanlang👇👇',
                              reply_markup=main_buttons())
    return state_main


def task(update, context):
    update.message.reply_text(
        "Assalomu alaykum\nushbu qismda siz uyingiz qurilishida ishlatiladigan mahsulotlarni buyurtma qilishingiz mumkin\nBiz Qisqa vaqt ichida sizga arzon va sifatli mahsulotlarni yetkazib beramiz🥳🥳\nSizga buyurtma qilmoqchi bo'layotgan mahsulotlar bo'yicha bir nechta savollar beriladi\nTayyormisiz?✅",
        reply_markup=task_button())
    return state_task_check


def command_task1(update, context):
    update.message.reply_text(
        "Yaxshi\n Qanday qurilish mollarini sotib olmoqchisiz?\n(Nomi, o'lchami, va sonini miqdorini kiriting)\nMasalan: 1.Reyka 6x4 - 100metr\n2. ...\n.\n.",
        reply_markup=ReplyKeyboardRemove())
    return state_task3


def command_task4(update, context):
    update.message.reply_text(
        "Siz bilan bog\'lanish uchun raqamingizni yuboring📲\nraqam yuborish tugmasini bosing!👇👇",
        reply_markup=phone_button())
    order = update.message.text
    id = order_create(order, update.effective_user.id)
    update_order_id(id, update.effective_user.id)
    return state_phone


def command_phone(update, context):
    contact = update.effective_message.contact
    phone = contact.phone_number
    user_id = update.effective_user.id
    update.message.reply_text(
        'Mahsulotlarni yetkazib berish manzilini aniqlash uchun telefoninggizning lokatsiyasini yoqqan holda Lokatsiya yuborish tugmasi bosing👇👇',
        reply_markup=location_button())
    order_update_phone(phone, user_id)
    return state_mintaqa


def command_mintaqa(update, context):
    update.message.reply_text('to\'lov', reply_markup=ReplyKeyboardRemove())
    update.message.reply_text(
        "Arizani yakunlash uchun to'lov turini tanlang👇👇",
        reply_markup=button_tulov_type())
    location = update.message.location
    latitude = location['latitude']
    longitude = location['longitude']
    user_id = update.effective_user.id
    order_update_location(latitude, longitude, user_id)

    return state_task2


def tulov_type(update, context):
    query = update.callback_query
    A = query.data
    query.message.delete()
    user_id = update.effective_user.id
    update_tulov_type(A, user_id)
    query.message.reply_html("Arizangiz muaffaqiyatli qabul qilindi\nTez orada siz bilan bog'lanamiz!",
                             reply_markup=main_buttons())
    order = get_order(user_id)
    user = get_user(user_id)
    xabar = f'NEW ORDER:\nFoydalanuvchi ismi: {user[1]}\n' \
            f'Foydalanuvchi username: @{user[6]}\n' \
            f'Foydalanuvchi id: {user[2]}\n' \
            f'Foydalanuvchi telefon raqami: {user[3]}\n' \
            f'Foydalanuvchi yashash manzili(latitude): {order[4]}\n' \
            f'Foydalanuvchi yashash manzili(longitude): {order[3]}\n' \
            f'to\'lov turi: {order[-1]}\n' \
            f'Orders: {order[1]}\n'
    for i in admins:
        try:
            context.bot.send_message(chat_id=i, text=xabar)
        except Exception as s:
            print(s)
    return state_main


def contact(update, context):
    user_id = update.effective_user.id
    update.message.reply_html(
        f'Aссалому алайкум\nБот юзасидан фикр ва таклифларингизни юборишингиз мумкин👇👇\n  @labbay_admin\n☎️📞 +998712007702',
        reply_markup=main_buttons())
    if user_id in admins:
        users = get_users()
        all_users = []
        for i in users:
            all_users.append(i[0])
        context.bot.send_message(chat_id=user_id, text=f"Foydalanuvchilar soni: {len(all_users)}")
    return state_main


conv_hand = ConversationHandler(
    entry_points=[MessageHandler(Filters.text, start)],
    states={
        state_main: [
            MessageHandler(Filters.regex('^(' + '📝Buyurma qilish' + ')$'), task),
            MessageHandler(Filters.regex('^(' + '☎️📞Biz bilan aloqa' + ')$'), contact),
        ],
        state_task_check: [
            MessageHandler(Filters.regex('^(' + 'Ha✅' + ')$'), command_task1),
            MessageHandler(Filters.regex('^(' + '⬅️Ortga' + ')$'), back),
        ],
        state_task3: [
            MessageHandler(Filters.text, command_task4)
        ],
        state_phone: [
            MessageHandler(Filters.contact, command_phone)
        ],
        state_mintaqa: [
            MessageHandler(Filters.location, command_mintaqa)
        ],
        state_task2: [
            CallbackQueryHandler(tulov_type)
        ]
    },
    fallbacks=[CommandHandler('start', start)]
)
updater = Updater('1930735104:AAGOgPFseJ6eOgpBcIgF5JFYRnq4zAZhebY')
updater.dispatcher.add_handler(conv_hand)

updater.start_polling()
updater.idle()
