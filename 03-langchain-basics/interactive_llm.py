from langchain_ollama import ChatOllama

# #create the llm connection 
# llm = ChatOllama(model = "llama3.2:3b")
#load all the configurations from the .env file
load dotenv()

#get input from user
query = input("> ")

#send the query to themodel
response = llm.invoke(query)

#print the response
print(response.content)
