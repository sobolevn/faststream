import pytest
from pydantic import ValidationError

from faststream.rabbit import TestRabbitBroker

from .annotation_rabbit import broker, handle


@pytest.mark.asyncio
async def test_handle():
    async with TestRabbitBroker(broker) as br:
        await br.publish({"name": "John", "user_id": 1}, queue="test-queue")

        handle.mock.assert_called_once_with({"name": "John", "user_id": 1})

    assert handle.mock.call_count == 0

@pytest.mark.asyncio
async def test_validation_error():
    async with TestRabbitBroker(broker) as br:
        with pytest.raises(ValidationError):
            await br.publish("wrong message", queue="test-queue")

        handle.mock.assert_called_once_with("wrong message")