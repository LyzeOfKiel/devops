'''Test time endpoint'''
from contextlib import contextmanager
from datetime import datetime
from pytz import timezone
from flask import template_rendered
import pytest

MOSCOW_TZ = timezone("Europe/Moscow")


@contextmanager
def captured_templates(app):
    recorded = []
    def record(_sender, template, context):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@pytest.mark.parametrize(
    'local_dt',
    ['2021-05-22 17:23', '2021-11-14 21:21']
)
def test_get_time(app, freezer, local_dt):
    freezer.move_to(local_dt)
    with captured_templates(app) as templates:
        resp = app.test_client().get('/')
        assert resp.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'
        parsed_time = datetime.strptime(context['time'], '%H:%M:%S')
        assert isinstance(parsed_time, datetime)
