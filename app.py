'''
Mail-To-Me - Send Mail
Author: Andrew McKinney
Creation Date: 2020-08-16
'''

# Import Dependencies
from flask import Flask, render_template
from data_packs import form_dict
from send_mail import send_mail

### DEV TOOLS ###
dev_mode = True


# Flask App Setup
app = Flask(__name__, static_folder='Images')




#################################################
# Flask Routes
#################################################


# homepage
@app.route("/")
@app.route("/index.html")
def index():
    
    return render_template("index.html")


# form submission route
@app.route("/form_submit/<to_mail>/<field_list>", methods=['POST'])
def post(to_mail, field_list):

    try:
        # extracting form data
        field_list = field_list.split(",")
        form_data = form_dict(field_list)

        # determining receiver email
        if to_mail != "demoform":
            to_mail = to_mail
        else:
            to_mail = form_data['to_mail']

        # sending email
        send_mail(to_mail, form_data)

        # returning successful post webpage
        return render_template("post.html", form_data = form_data, to_mail = to_mail)
        

    # returning unseccessful post webpage
    except:
        return render_template("nopost.html")


if __name__ == "__main__":
    if dev_mode:
        app.run(debug=True)
    else:
        app.run(debug=False)
