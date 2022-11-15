import aws_cdk as core
import aws_cdk.assertions as assertions

from contextstack.contextstack_stack import ContextstackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in contextstack/contextstack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ContextstackStack(app, "contextstack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
