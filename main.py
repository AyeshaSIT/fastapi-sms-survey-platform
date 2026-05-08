from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sample():
    return {"messgage":"Hello World"}
def main():
    print("Hello from fastapi-sms-survey-platform!")


if __name__ == "__main__":
    main()
