import grpc
import item_pb2
import item_pb2_grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = item_pb2_grpc.ItemServiceStub(channel)
stub1 = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
item = item_pb2.ItemMessage(
    name="Non-Stick Frying Pan",
    brand_name="Proof",
    id=4,
    weight=4.5
)

order = order_pb2.OrderMessage(
    id="12",
    created_by="User_12",
    created_at="2021-11-08",
    status=order_pb2.OrderMessage.Status.QUEUED,
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
)

response = stub.Create(item)
response1 = stub1.Create(order)
response2 = stub1.Get(order_pb2.Empty())

print(response2)
