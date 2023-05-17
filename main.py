# first: py -m pip install fastapi[all]
# run server: uvicorn main(name of file):app(name of fast api instance)
# uvicorn main:app --reload: to automatically reload server, only used in development enviroment

app = FastAPI()

# [path operation]
# decorator to turn a function to an api call
@app.get("/") # << url path
def root():
    return {"message": "welcome to my api"}

@app.get("/") 
def get_posts():
    return {"data": "This is your posts"}