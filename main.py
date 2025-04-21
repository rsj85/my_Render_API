from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.post("/run-cleanup")
def run_cleanup():
    # 👇 Replace this with your actual voucher-cleaning logic
    print("Running voucher cleanup...")

    # If using Omada API logic, you can import and call that function here.
    return {"status": "Voucher cleanup completed"}
