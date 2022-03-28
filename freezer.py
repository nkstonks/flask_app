import os
from app import app
from status_app import status_app
from flask_frozen import Freezer

status_app.config["FREEZER_DESTINATION"] = "status"

app.config["FREEZER_DESTINATION"] = "docs"
app.config["FREEZER_DESTINATION_IGNORE"] = ["CNAME"]

freezer = Freezer(app)
freezer2 = Freezer(status_app)

def add_html_ext():
    path = "docs"
    files = os.listdir(path)
    for file_name in files:
        # print(file_name)
        if file_name == "static" or file_name == "CNAME":
            continue
        if os.path.splitext(file_name)[1] == ".html":
            continue
        old_path = os.path.join("docs", file_name)
        new_path = os.path.join("docs", file_name + '.html')
        os.rename(old_path, new_path)

if __name__ == '__main__':

    freezer.freeze()

    freezer2.freeze()
    
    add_html_ext()