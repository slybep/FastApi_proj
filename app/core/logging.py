import logging


def configure_logging():
    root_logger = logging.getLogger()  # получаем корневой логгер (самый верхний)
    if not root_logger.handlers:  # проверяем, есть ли у него уже обработчики
        logging.basicConfig(  # если нет – настраиваем
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )
    logging.getLogger("app").setLevel(logging.INFO)
