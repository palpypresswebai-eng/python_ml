# import random

# while True:
#     computer_random = random.choice("rps")
#     user_input = input("Please select r/p/s: ").lower()

#     if user_input not in ["r", "p", "s"]:
#         print("Invalid input! Try again.")
#         continue

#     print(f"Computer choice: {computer_random}")

#     if user_input == computer_random:
#         print("Game is a tie! Try again.")
#     elif (user_input == "r" and computer_random == "p") or \
#          (user_input == "p" and computer_random == "s") or \
#          (user_input == "s" and computer_random == "r"):
#         print("You lose the game. Try again.")
#     else:
#         print("🎉 You won the game!")
#         again = input("you want to countinu y/n: ").lower()
#         if again == "y":
#             continue
#         else:
#             break

# import pandas as pd

# data = {"a": 1,"b":2,"c":3,"d":4}
# series_data = pd.Series(data)
# print(series_data)



# data = [10,20,30]
# index=["a","b","c"]
# print(pd.Series[data,index])



import pandas as pd
# data ={
#     "name": ["pal","deep","vansh","vaja"],
#     "age": [21,20,21,22],
#     "gendar": ["male","male","female","male"],
#     "city" : ["ahem","surat","rajkot","porbandar"]
# }

# data["name"]
# data.loc[0][0]


# df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data")
# df



from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to over 1st flaskk"


if __name__=="__main__":
    app.run()


