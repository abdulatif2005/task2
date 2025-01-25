import pytest


def test_wsgi_import():
    # Проверяем, что WSGI-приложение импортируется без ошибок.

    try:
        from core.wsgi import application
        assert application is not None
    except Exception as e:
        pytest.fail(f"Импорт WSGI-приложения завершился с ошибкой: {e}")


def test_asgi_import():
    # Проверяем, что ASGI-приложение импортируется без ошибок.

    try:
        from core.asgi import application
        assert application is not None
    except Exception as e:
        pytest.fail(f"Импорт ASGI-приложения завершился с ошибкой: {e}")
