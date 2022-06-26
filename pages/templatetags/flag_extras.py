from django import template

register = template.Library()

from datetime import datetime, tzinfo
import pytz
from dateutil import tz

# from django.utils import timezone


@register.simple_tag
def current_time(format_string):
    # now = datetime.fromtimestamp(timestamp, timezone.utc)
    fmt = "%d/%m/%Y %H:%M"
    dt_str = datetime.now().strftime(format_string)

    # Create datetime object in local timezone
    dt_utc = datetime.strptime(dt_str, format_string)
    dt_utc = dt_utc.replace(tzinfo=pytz.UTC)
    # Get local timezone
    local_zone = pytz.timezone("Australia/Brisbane")
    # Convert timezone of datetime from UTC to local
    dt_local = dt_utc.astimezone(local_zone)
    return dt_local.strftime(format_string)
