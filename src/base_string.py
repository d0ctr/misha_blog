class BaseString():
    __start_message = 'Этот бот использует основанную на ruGPT3Small модель, '\
        'дообученную на блоге "Хрустящие мысли". ~~Основная~~ Единcтвенная функция бота это генерирование текста.'\
        'Для использования просто введите имя бота ({bot_id}) и название поста в любом чате.'
    __help_message = 'Для использования бота напишите в любом чате {bot_id} и название поста, '\
        'для которого хотите сгенерировать текст.'
    
    @classmethod
    def start_message(cls, context):
        return cls.__start_message.format(bot_id=context.bot)

    @classmethod
    def help_message(cls, context):
        return cls.__help_message.format(bot_id=context.bot)
