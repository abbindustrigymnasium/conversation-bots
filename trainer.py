from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

Ray = ChatBot(
            "Ray",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri='sqlite:///database.sqlite3',
            logic_apapter=[
            "chatterbot.logic.TimeLogicAdapter",
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.BestMatch"]
)

trainer = ChatterBotCorpusTrainer(Ray)

trainer.train("chatterbot.corpus.english")