from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from time import sleep

Norman = ChatBot(
            "Norman",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri="sqlite:///database.sqlite3",
            logic_apapter=[
                "chatterbot.logic.TimeLogicAdapter",
                "chatterbot.logic.MathematicalEvaluation",
                "chatterbot.logic.BestMatch"]
            )

# Emma = ChatBot(
#             "Emma",
#             storage_adapter="chatterbot.storage.SQLStorageAdapter",
#             logic_apapter=[
#                 "chatterbot.logic.TimeLogicAdapter",
#                 "chatterbot.logic.MathematicalEvaluation",
#                 "chatterbot.logic.BestMatch"]
#             )

# TrainerN = ChatterBotCorpusTrainer(Norman)
# TrainerE = UbuntuCorpusTrainer(Emma)
# TrainerE.train("chatterbot.corpus.english")
# TrainerN.train("chatterbot.corpus.english")

def messageArrive(input):
    bot_output = Norman.get_response(input)
    return bot_output


if __name__ == "__main__":
    while True:
        try:
            Norman_input = Norman.get_response(input("You: "))
            print("Norman:", Norman_input)

    #         # Norman_input = "Hello"
    #         # Emma_input = Emma.get_response(Norman_input)
    #         # Norman_input = Norman.get_response(Emma_input)
    #         # print("Emma:", Emma_input)
    #         # sleep(2)
    #         # print("Norman:", Norman_input)
    #         # sleep(2)

            
        except(KeyboardInterrupt, EOFError, SystemExit):
            break