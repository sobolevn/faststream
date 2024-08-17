from faststream import FastStream
from faststream.kafka import KafkaBroker
from faststream.specification.asyncapi.generate import get_app_schema
from faststream.specification.asyncapi.version import AsyncAPIVersion
from faststream.specification.schema.contact import Contact
from faststream.specification.schema.docs import ExternalDocs
from faststream.specification.schema.license import License
from faststream.specification.schema.tag import Tag


def test_base():
    schema = get_app_schema(FastStream(KafkaBroker()), version=AsyncAPIVersion.v2_6).to_jsonable()

    assert schema == {
        "asyncapi": "2.6.0",
        "channels": {},
        "components": {"messages": {}, "schemas": {}},
        "defaultContentType": "application/json",
        "info": {"description": "", "title": "FastStream", "version": "0.1.0"},
        "servers": {
            "development": {
                "protocol": "kafka",
                "protocolVersion": "auto",
                "url": "localhost",
            }
        },
    }


def test_with_name():
    schema = get_app_schema(
        FastStream(
            KafkaBroker(),
            title="My App",
            version="1.0.0",
            description="Test description",
        ),
        version=AsyncAPIVersion.v2_6,
    ).to_jsonable()

    assert schema == {
        "asyncapi": "2.6.0",
        "channels": {},
        "components": {"messages": {}, "schemas": {}},
        "defaultContentType": "application/json",
        "info": {
            "description": "Test description",
            "title": "My App",
            "version": "1.0.0",
        },
        "servers": {
            "development": {
                "protocol": "kafka",
                "protocolVersion": "auto",
                "url": "localhost",
            }
        },
    }


def test_full():
    schema = get_app_schema(
        FastStream(
            KafkaBroker(),
            title="My App",
            version="1.0.0",
            description="Test description",
            license=License(name="MIT", url="https://mit.com/"),
            terms_of_service="https://my-terms.com/",
            contact=Contact(name="support", url="https://help.com/"),
            tags=(Tag(name="some-tag", description="experimental"),),
            identifier="some-unique-uuid",
            external_docs=ExternalDocs(
                url="https://extra-docs.py/",
            ),
        ),
        version=AsyncAPIVersion.v2_6
    ).to_jsonable()

    assert schema == {
        "asyncapi": "2.6.0",
        "channels": {},
        "components": {"messages": {}, "schemas": {}},
        "defaultContentType": "application/json",
        "externalDocs": {"url": "https://extra-docs.py/"},
        "id": "some-unique-uuid",
        "info": {
            "contact": {"name": "support", "url": "https://help.com/"},
            "description": "Test description",
            "license": {"name": "MIT", "url": "https://mit.com/"},
            "termsOfService": "https://my-terms.com/",
            "title": "My App",
            "version": "1.0.0",
        },
        "servers": {
            "development": {
                "protocol": "kafka",
                "protocolVersion": "auto",
                "url": "localhost",
            }
        },
        "tags": [{"description": "experimental", "name": "some-tag"}],
    }


def test_full_dict():
    schema = get_app_schema(
        FastStream(
            KafkaBroker(),
            title="My App",
            version="1.0.0",
            description="Test description",
            license={"name": "MIT", "url": "https://mit.com/"},
            terms_of_service="https://my-terms.com/",
            contact={"name": "support", "url": "https://help.com/"},
            tags=({"name": "some-tag", "description": "experimental"},),
            identifier="some-unique-uuid",
            external_docs={
                "url": "https://extra-docs.py/",
            },
        ),
        version=AsyncAPIVersion.v2_6
    ).to_jsonable()

    assert schema == {
        "asyncapi": "2.6.0",
        "channels": {},
        "components": {"messages": {}, "schemas": {}},
        "defaultContentType": "application/json",
        "externalDocs": {"url": "https://extra-docs.py/"},
        "id": "some-unique-uuid",
        "info": {
            "contact": {"name": "support", "url": "https://help.com/"},
            "description": "Test description",
            "license": {"name": "MIT", "url": "https://mit.com/"},
            "termsOfService": "https://my-terms.com/",
            "title": "My App",
            "version": "1.0.0",
        },
        "servers": {
            "development": {
                "protocol": "kafka",
                "protocolVersion": "auto",
                "url": "localhost",
            }
        },
        "tags": [{"description": "experimental", "name": "some-tag"}],
    }


def test_extra():
    schema = get_app_schema(
        FastStream(
            KafkaBroker(),
            title="My App",
            version="1.0.0",
            description="Test description",
            license={"name": "MIT", "url": "https://mit.com/", "x-field": "extra"},
            terms_of_service="https://my-terms.com/",
            contact={"name": "support", "url": "https://help.com/", "x-field": "extra"},
            tags=(
                {"name": "some-tag", "description": "experimental", "x-field": "extra"},
            ),
            identifier="some-unique-uuid",
            external_docs={
                "url": "https://extra-docs.py/",
                "x-field": "extra",
            },
        ),
        version=AsyncAPIVersion.v2_6
    ).to_jsonable()

    assert schema == {
        "asyncapi": "2.6.0",
        "channels": {},
        "components": {"messages": {}, "schemas": {}},
        "defaultContentType": "application/json",
        "externalDocs": {"url": "https://extra-docs.py/", "x-field": "extra"},
        "id": "some-unique-uuid",
        "info": {
            "contact": {
                "name": "support",
                "url": "https://help.com/",
                "x-field": "extra",
            },
            "description": "Test description",
            "license": {"name": "MIT", "url": "https://mit.com/", "x-field": "extra"},
            "termsOfService": "https://my-terms.com/",
            "title": "My App",
            "version": "1.0.0",
        },
        "servers": {
            "development": {
                "protocol": "kafka",
                "protocolVersion": "auto",
                "url": "localhost",
            }
        },
        "tags": [
            {"description": "experimental", "name": "some-tag", "x-field": "extra"}
        ],
    }
