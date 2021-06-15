import paramiko


def get_events():
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
        for line in stdout:
            yield line
    finally:
        client.close()
