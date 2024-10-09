import base64
import sys
import requests

def get_shift_number(raw_input: str) -> str | None:
    if (len(raw_input) < 4):
      return None
    return raw_input[-4:]

def repl():
    print("Enter 'exit' to quit the REPL.")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == 'exit':
            print("Exiting REPL.")
            break
        else:
            shift_number = get_shift_number(user_input)
            if shift_number is None:
                print("Invalid input. Please enter a valid shift number.")
            else:
                print(f"Shift number: {shift_number}")

                # url = "http://localhost:8013/api/preview/text?return_format=base64"
                url = "http://localhost:8013/api/print/text"
                
                label_data = {
                  "text": shift_number,
                  "font_family": "DejaVu Sans (Bold)",
                  "font_size": "150",
                  "label_size": "17x54",
                  "align": "center",
                  "orientation": "standard",
                  "margin_top": 0,
                  "margin_bottom": 30,
                  "margin_left": 35,
                  "margin_right": 35,
                  "label_count": 1,
                }


                response = requests.post(url, data=label_data)

                if response.status_code == 200:
                  # with open("label.png", "wb") as image_file:
                  #   image_file.write(base64.b64decode(response.content))
                  # print("Image saved as label.png")
                  print("Label printed")
                else:
                  print(f"Failed {response.status_code}")

if __name__ == "__main__":
    repl()