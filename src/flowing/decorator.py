from functools import wraps
from .span import Span
from .tracer import get_current_span, set_current_span, record_span


def trace_agent(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        parent = get_current_span()
        parent_id = parent.span_id if parent else None

        span = Span(agent_name=func.__name__, parent_id=parent_id)
        span.input = {"args": args, "kwargs": kwargs}

        set_current_span(span)

        try:
            result = func(*args, **kwargs)
            span.output = result
            return result

        except Exception as e:
            span.error = str(e)
            raise

        finally:
            span.finish()
            record_span(span)

            if parent:
                set_current_span(parent)
            else:
                set_current_span(None)

    return wrapper
