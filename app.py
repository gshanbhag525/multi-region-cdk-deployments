#!/usr/bin/env python3
import os

import aws_cdk as cdk

from contextstack.contextstack_stack import ContextstackStack

from ContextGroup import *

app = cdk.App()

# Load the context group
context_group = ContextGroup(app)

# Context variables within group name as loaded as attribute onto ContextGroup object
# print(context_group.AWSAccountID)
# print(context_group.AWSProfileName)

# Pass the group to print() or other string functions to see all of the group variables
# print(context_group)

ContextstackStack(app, "ContextstackStack", context_group=context_group
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
