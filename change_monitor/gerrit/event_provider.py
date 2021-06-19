import paramiko
import time


class SshHostConfig:
    def __init__(self, command, username, host, port=22):
        self.command = command
        self.username = username
        self.host = host
        self.port = port


class SshGerrit:
    def __init__(self, host_config, event_queue):
        self.host_config = host_config
        self.event_queue = event_queue

    def get_events(self):
        # TODO exit condition
        while True:
            try:
                client = self._connect()
                stdin, stdout, stderr = client.exec_command(self.host_config.command)
                for line in stdout:
                    self.event_queue.put(line.strip())
            finally:
                client.close()

            # TODO: Increasing time
            time.sleep(10)

    def _connect(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        # TODO: Temporary accept all host keys
        client.set_missing_host_key_policy(paramiko.WarningPolicy)  # nosec

        client.connect(
            self.host_config.host,
            port=self.host_config.port,
            username=self.host_config.username,
        )
        return client
