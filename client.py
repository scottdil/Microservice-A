"""
Source for code is from: https://grpc.io/docs/languages/python/quickstart/
and https://grpc.io/docs/languages/python/basics/
code is adapted from sample code to learn how to use gRPC with python.
8/2/2024
"""

import grpc
import foodlist_pb2_grpc
import foodlist_pb2
import time


# test client to send request to server with gRPC
def run():
    # connect channel to grpc server
    channel = grpc.insecure_channel('localhost:50051')
    # create the stub to send the grpc request
    stub = foodlist_pb2_grpc.FoodListServiceStub(channel)
    
    # list of items needed for the recipe
    recipe = ['chicken', 'carrots', 'butter', 'Onion', 'pie crust', 
              'eggs', 'garlic', 'FLOUR', 'CHICKEN STOCK', 
              'half-and-half', 'peas', 'salt', 'black pepper', 'thyme']
    # list of items that the user already has
    kitchen = ['CHICKeN', 'cheese', 'eGgs', 'peAs', 'salt', 'black pepper']

    print("\nSending recipe list: ", recipe, '\n')
    print("Sending kitchen list: ", kitchen, '\n')

    # send the grpc request
    request = foodlist_pb2.FoodListRequest(recipeList=recipe, foodList=kitchen)
    # get the grpc response
    response = stub.GetPurchaseList(request)
    time.sleep(3)
    print("Response received: ", '\n', response.purchaseList)


if __name__ == '__main__':
    run()