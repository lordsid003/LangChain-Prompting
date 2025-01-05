# Model instantiate, API call, demo

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from config import Config, prompt 

load_dotenv()

class Model(object):
    def __init__(self) -> None:
        self.llm = ChatGroq(
            temperature=0.8,
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def chat(self, message: str) -> str:
        sequence_chain = prompt | self.llm.with_structured_output(Config)
        try:
            data = {"user_message": message}
             # Running State of chain
            response = sequence_chain.invoke(data)
            return response.msg
        except:
            error: str = "Error"
            return error
        
if __name__ == "__main__":
    print(f"------------Welcome User---------------")
    # Instantiate the model
    model = Model()
    while True:
        msg: str = input("Me: ")
        if len(msg) < 1:
            response = "Error"
            msg = "..."
        response = model.chat(message=msg)
        print(f"Snape: {response}")
        check: str = input("Exit? [y/n]: ")
        if check.lower() == "y":
            break

    

    
