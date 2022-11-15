from aws_cdk import (
    Duration,
    Stack,
)

from aws_cdk.aws_lambda import Code, Function, Runtime, LayerVersion
from constructs import Construct

from ContextGroup import *

class ContextstackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,  context_group: ContextGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        print(context_group.AWSProfileName)

        demofn = Function(self, "DemoFunction",
            runtime=Runtime.PYTHON_3_7,
            handler="index.handler",
            code=Code.from_asset("Lambda"),
            timeout=Duration.seconds(40)
        )
        