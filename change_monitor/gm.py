from gerrit import events, event_provider
from change import Change


def main():
    event_dict = {}
    for line in event_provider.get_events():
        event = events.create_event(line)
        if event is None:
            continue

        # s = event.to_string()
        change = event_dict.get(event.id)
        if not change:
            change = Change()
            event_dict[event.id] = change

        change.add_event(event)

    print(len(event_dict))


if __name__ == "__main__":
    main()
