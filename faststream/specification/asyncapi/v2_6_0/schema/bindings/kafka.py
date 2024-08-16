"""AsyncAPI Kafka bindings.

References: https://github.com/asyncapi/bindings/tree/master/kafka
"""
from typing import Optional

from pydantic import BaseModel, PositiveInt
from typing_extensions import Self

from faststream.specification import schema as spec
from faststream.types import AnyDict


class ChannelBinding(BaseModel):
    """A class to represent a channel binding.

    Attributes:
        topic : optional string representing the topic
        partitions : optional positive integer representing the number of partitions
        replicas : optional positive integer representing the number of replicas
        bindingVersion : string representing the binding version
    """

    topic: Optional[str] = None
    partitions: Optional[PositiveInt] = None
    replicas: Optional[PositiveInt] = None
    bindingVersion: str = "0.4.0"

    # TODO:
    # topicConfiguration

    @classmethod
    def from_spec(cls, binding: spec.bindings.kafka.ChannelBinding) -> Self:
        return cls(
            topic=binding.topic,
            partitions=binding.partitions,
            replicas=binding.replicas,
            bindingVersion=binding.bindingVersion,
        )


class OperationBinding(BaseModel):
    """A class to represent an operation binding.

    Attributes:
        groupId : optional dictionary representing the group ID
        clientId : optional dictionary representing the client ID
        replyTo : optional dictionary representing the reply-to
        bindingVersion : version of the binding (default: "0.4.0")
    """

    groupId: Optional[AnyDict] = None
    clientId: Optional[AnyDict] = None
    replyTo: Optional[AnyDict] = None
    bindingVersion: str = "0.4.0"

    @classmethod
    def from_spec(cls, binding: spec.bindings.kafka.OperationBinding) -> Self:
        return cls(
            groupId=binding.groupId,
            clientId=binding.clientId,
            replyTo=binding.replyTo,
            bindingVersion=binding.bindingVersion,
        )
