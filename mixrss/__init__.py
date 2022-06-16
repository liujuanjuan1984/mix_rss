import datetime
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
logging.basicConfig(
    format="%(name)s %(asctime)s %(levelname)s %(message)s",
    filename=f"mixrss_{datetime.date.today()}.log",
    level=logging.DEBUG,
)
