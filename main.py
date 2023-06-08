import os
import uvicorn

if __name__ == "__main__":
    os.system("""export $( grep -vE "^(#.*|\s*)$" .env )""")    # load environment variable from .env file
    uvicorn.run(app="app.api:app", host="127.0.0.1", port=8081, reload=True)
    