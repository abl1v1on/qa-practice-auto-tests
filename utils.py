import os
import httpx
from _pytest.main import Session
from dotenv import load_dotenv


load_dotenv()


def disable_proxy() -> None:
    os.system('proxy -d')


def enable_proxy() -> None:
    os.system('proxy -e')


class TelegramClient:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')

    def __init__(self) -> None:
        self.base_url = f'https://api.telegram.org/bot{self.BOT_TOKEN}'

    def send_message(self, session: Session) -> httpx.Response:
        with httpx.Client(base_url=self.base_url) as client:
            response = client.post('/sendMessage', data={
                'chat_id': self.CHAT_ID,
                'text': self.__get_message_text(session)
            })
            return response

    @staticmethod
    def __get_message_text(session: Session) -> str:
        total = session.testscollected
        failed = session.testsfailed
        status = "✅ Все тесты пройдены!" if failed == 0 else "⚠️ Есть проваленные тесты!"

        message = (
            '🎯 Результаты тестирования 🎯\n\n'
            f'📌 Всего тестов: {total}\n'
            f'💥 Провалено: {failed}\n\n'
            f'📊 Статус: {status}\n\n'
            f'📜 Отчет: [ссылка на детали]\n\n'
            '🚀 Продолжаем совершенствоваться! 🚀'
        )
        return message
