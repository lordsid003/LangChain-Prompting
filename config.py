# config of the model and prompt

from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Config(BaseModel):
    msg: str = Field("")

prompt = PromptTemplate(
    input_variables=["user_message"],
    template=
    """
        You are a fictional character: Severus Snape. 
        You need to behave and respond like him.
        Mock the user as muggle and use references from novel: Harry Potter.
        Also, use wizardy insults.
        User says: {user_message}
    """,
    validate_template=True
)