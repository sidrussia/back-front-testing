__all__ = ['controller_config']

from lib.app_lib.amqp_routes import CONTROLLER, CONTROLLER_EXCHANGE
from lib.app_lib.messages.message import RenameFileRequest

controller_messages = [
    RenameFileRequest
]

controller_config = {
    "name": CONTROLLER,
    "types": controller_messages,
    "exchange_name": CONTROLLER_EXCHANGE,
    "queue_name": CONTROLLER,
    "routing_name": CONTROLLER
}
