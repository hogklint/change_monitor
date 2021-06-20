import gevent

from .gerrit import event_provider
from . import event_handler


host_configs = [
    event_provider.SshHostConfig(
        "tmp/printdata tmp/gerrit_json_events 1", "hogklint", "192.168.1.10"
    ),
    event_provider.SshHostConfig(
        "tmp/printdata tmp/gerrit_json_events 1", "hogklint", "192.168.1.10"
    ),
]


def gm_main():
    servers = [
        event_provider.SshGerrit(c, event_handler.event_queue) for c in host_configs
    ]
    jobs = [gevent.spawn(s.get_events) for s in servers]
    jobs.append(gevent.spawn(event_handler.handle_events))
    gevent.joinall(jobs)
