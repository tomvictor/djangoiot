class _IotCore:
    """
    IotCore main class
    """

    def __init__(self, server, port, callback) -> _IotCore:
        """
        Init function
        :param server: server host
        :param port: port
        :param callback: call back function
        """
        ...

    def publish(self, topic: str, data: str):
        """
        Publish date over mqtt
        :param topic: topic
        :param data: data
        :return: None
        """
        ...

    def subscribe(self, topic):
        """
        subscribe to mqtt topic
        :param topic:
        :return:
        """
        ...

    def initialize_broker(self):
        """
        Run mqtt broker
        :return: None
        """
        ...

    def begin_subscription(self):
        """
        Run mqtt broker
        :return: None
        """
        ...

