import paramiko
from gerrit import events
from change import Change


def main():
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        # TODO: Temporary accept all host keys
        client.set_missing_host_key_policy(paramiko.WarningPolicy)  # nosec

        client.connect("192.168.1.10", port=22, username="hogklint")
        # TODO: Temporary hardcoded command
        stdin, stdout, stderr = client.exec_command(  # nosec
            "cat tmp/gerrit_json_events"
        )
        event_dict = {}
        for line in stdout:
            event = events.create_event(line)
            if event is None:
                continue

            #s = event.to_string()
            change = event_dict.get(event.id)
            if not change:
                change = Change()
                event_dict[event.id] = change

            change.add_event(event)

        print(len(event_dict))

    finally:
        client.close()


if __name__ == "__main__":
    main()
