from flask import Flask
import utils

app = Flask(__name__)

users = utils.get_users()


@app.route('/')
def page_index():
    result = "<pre>"
    for user in users.values():
        html = "<pre>"
        html += f"{user['name']}<br>" \
                f"{user['gender']}<br>" \
                f"{user['age']}<br>"

        html += "</pre>"
        result += html
    result += "</pre>"

    return result


@app.route('/users/<int:id>')
def page_user_profile(id):
    user = users[id]
    html = "<pre>"
    html += f"<img src='{user['picture']}'/><br><br>" \
            f"{user['name']}<br>" \
            f"{user['gender']}<br>" \
            f"{user['age']}<br>"
    html += "</pre>"

    return html


@app.route('/genders/<gender>')
def page_gender(gender):
    users_group_gender = "<pre>"

    for user in users.values():
        user_gender = user['gender'].split()
        if gender in user_gender:
            users_group_gender += f"{user['name']}<br>" \
                                  f"{user['gender']}<br>" \
                                  f"{user['age']}<br><br>"
    users_group_gender += "</pre>"

    return users_group_gender


if __name__ == "__main__":
    app.run()
