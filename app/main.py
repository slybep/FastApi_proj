import asyncio
import logging
from time import perf_counter

from app.api.routers.book import router as book_router
from fastapi import FastAPI, Request, Response

app = FastAPI()
app.include_router(router=book_router)
logger = logging.getLogger("app.middleware")


@app.middleware("http")
async def log_requests(request: Request, call_next) -> Response:
    started_at = perf_counter()
    try:
        response: Response = await call_next(request)
    except Exception:
        duration_ms = (perf_counter() - started_at) * 1000
        logger.exception(
            "Request failed: %s %s completed_in=%.2fms",
            request.method,
            request.url.path,
            duration_ms,
        )
        raise

    duration_ms = (perf_counter() - started_at) * 1000
    logger.info(
        "%s %s -> %s (%.2f ms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


_request_counter = 0
_lock = asyncio.Lock()


@app.middleware("http")
async def count_request(request: Request, call_next) -> Response:
    try:
        response: Response = await call_next(request)  # Работа самого эндпоинта
    except Exception:
        logger.exception(
            "Unhandled exception in request %s %s", request.method, request.url.path
        )
        raise
    global _request_counter
    async with _lock:
        _request_counter += 1
    response.headers["X-request-number"] = str(_request_counter)

    return response
