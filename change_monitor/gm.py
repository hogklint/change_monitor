import gevent
from gevent import monkey

monkey.patch_all()

from gerrit import events, event_provider
from change import Change

host_configs = [
    event_provider.SshHostConfig(
        "tmp/printdata tmp/gerrit_json_events 1", "hogklint", "192.168.1.10"
    ),
    event_provider.SshHostConfig(
        "tmp/printdata tmp/gerrit_json_events 1", "hogklint", "192.168.1.10"
    ),
]
event_queue = gevent.queue.Queue()
event_dict = {}


def handle_events(event_queue):
    for line in event_queue:
        event = events.create_event(line)
        if event is None:
            continue

        # s = event.to_string()
        change = event_dict.get(event.id)
        if not change:
            change = Change()
            event_dict[event.id] = change

        change.add_event(event)


def main():
    servers = [event_provider.SshGerrit(c, event_queue) for c in host_configs]
    jobs = [gevent.spawn(s.get_events) for s in servers]
    jobs.append(gevent.spawn(handle_events, event_queue))
    gevent.joinall(jobs)
    # for line in event_provider.get_events():

    # print(len(event_dict))


if __name__ == "__main__":
    main()
