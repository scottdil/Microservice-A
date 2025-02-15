"""
Source for code is from: https://grpc.io/docs/languages/python/quickstart/
and https://grpc.io/docs/languages/python/basics/
code is adapted from sample code to learn how to use gRPC with python.
8/2/2024
"""
# import grpc and the generated pb2 files
import grpc
import foodlist_pb2
import foodlist_pb2_grpc
from concurrent import futures
import time


# class that inherits the foodlist_pb2_grpc generated by the proto file
class FoodListServiceServicer (foodlist_pb2_grpc.FoodListServiceServicer):
    def GetPurchaseList(self, request, context):
        # convert request object to list
        recipe_list = list(request.recipeList)
        food_list = list(request.foodList)

        time.sleep(2)
        print("\nReceived recipe list: ", recipe_list, '\n')
        print("Received kitchen list: ", food_list, '\n')

        # convert all strings in lists to lower case
        recipe_list = [x.upper() for x in recipe_list]
        food_list = [x.upper() for x in food_list]

        # compare recipe item (food) to the list of food owned (food_list)
        # if food not in food_list add to buy_list
        buy_list = []
        for food in recipe_list:
            if food not in food_list:
                buy_list.append(food)

        time.sleep(2)
        print("Sending purchase list: ", buy_list, '\n')

        # send the response of items to purchase
        return foodlist_pb2.FoodListResponse(purchaseList=buy_list)


# grpc server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    foodlist_pb2_grpc.add_FoodListServiceServicer_to_server(
        FoodListServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()