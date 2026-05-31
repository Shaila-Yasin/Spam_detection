from predict import predict_message

while True:
    msg = input("Enter email: ")

    if msg.lower() == "exit":
        break

    print("Prediction:", predict_message(msg))