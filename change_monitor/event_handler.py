import gevent
from gerrit import events

event_dict = {}
event_queue = gevent.queue.Queue()

def handle_events():
    global event_queue
    global event_dict

    for line in event_queue:
        #print(line)
        event = events.create_event(line)
        if event is None:
            continue

        # s = event.to_string()
        change = event_dict.get(event.id)
        if not change:
            change = Change()
            event_dict[event.id] = change

        change.add_event(event)
