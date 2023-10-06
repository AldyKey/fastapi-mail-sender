import logging
from logging.handlers import RotatingFileHandler
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.concurrency import iterate_in_threadpool


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        log_file = "logs/info.log"
        file_handler = RotatingFileHandler(log_file, maxBytes=524288000, backupCount=10)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        user_ip = request.client.host
        username = "AnonymousUser"

        self.logger.info(f"Incoming Request: {user_ip} | {username} | {request.method} {request.url}")

        response = await call_next(request)

        if response.status_code != 200:
            try:
                response_body = [chunk async for chunk in response.body_iterator]
                response.body_iterator = iterate_in_threadpool(iter(response_body))
                body = response_body[0].decode()
            except Exception:
                body = "<not decodable>"
            self.logger.info(f"Outgoing Response: {response.status_code} | Body: {body}")
        else:
            self.logger.info(f"Outgoing Response: {response.status_code}")

        return response