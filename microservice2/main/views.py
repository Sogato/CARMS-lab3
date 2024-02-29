import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def get_message(request):
    if request.method == "GET":
        message = "Привет! Это ВТОРОЙ микросервис!"
        logger.info(f"Сообщение отправлено: {message}")
        return HttpResponse(message)
