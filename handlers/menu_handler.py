from aiogram import Router, F, types
from keyboards.settings_keyboard import start_set_keyboard
from keyboards.feedback_keybord import start_feed_keyboard
from keyboards.zay_keyboard import start_zay_keyboard
from keyboards.contacts_keyboards import start_contact_keyboard
router = Router()


@router.callback_query(F.data == 'settings')
async def setting_handler(callback: types.CallbackQuery):
    await callback.message.answer('''
⚙️Тут Вы сможете поменять Имя и Фамилию в Базе данных нашего бота или же можете поменять Ваш номер телефона, если
 Вы изначально вводили что-то неверно. Выберите, что хотите поменять или вернитесь назад в главное меню:    
    ''', reply_markup=start_set_keyboard)

@router.callback_query(F.data == 'zayavka')
async def za_handler(callback: types.CallbackQuery):
    await callback.message.answer('''
📛👇📛Выберите категорию, по которой Вы хотите оставить заявку в УК:    
    ''', reply_markup=start_zay_keyboard)

@router.callback_query(F.data == 'feedback')
async def feedback_handler(callback: types.CallbackQuery):
    await callback.message.answer('''
👇Выберите способ связи из нижеперечисленного списка:   
    ''', reply_markup=start_feed_keyboard)

@router.callback_query(F.data == 'contacts')
async def contacts_handler(callback: types.CallbackQuery):
    await callback.message.answer('''
Управляющая компания:
Диспетчерская служба  ООО «УЭР-ЮГ»
+7 4722 35-50-06
Инженеры ООО «УЭР-ЮГ»
+7 920 566-28-86
Бухгалтерия ООО «УЭР-ЮГ»
+7 4722 35-50-06
Белгород, Свято-Троицкий б-р, д. 15, подъезд No 1

Телефоны для открытия ворот и шлагбаума: 
Шлагбаум «Набережная»
+7 920 554-87-74
Ворота «Харьковские»
+7920 554-87-40
Ворота «Мост»
+7 920 554-64-06
Калитка 1 «Мост»
+7 920 554-42-10
Калитка 2 «Мост»
+7 920 554-89-04
Калитка 3 «Харьковская»
+7 920 554-87-39
Калитка 4 «Харьковская»
+7 920 554-89-02

Охрана
+7 915 57-91-457

Участковый
Куленцова Марина Владимировна
+7 999 421-53-72
        ''', reply_markup=start_contact_keyboard)


