from faststream.asyncapi.generate import get_app_schema
from faststream.nats import NatsBroker
from tests.asyncapi.base.v3_0_0.arguments import ArgumentsTestcase


class TestArguments(ArgumentsTestcase):
    broker_factory = NatsBroker

    def test_subscriber_bindings(self):
        broker = self.broker_factory()

        @broker.subscriber("test")
        async def handle(msg): ...

        schema = get_app_schema(self.build_app(broker)).to_jsonable()
        key = tuple(schema["channels"].keys())[0]  # noqa: RUF015

        assert schema["channels"][key]["bindings"] == {
            "nats": {"bindingVersion": "custom", "subject": "test"}
        }
