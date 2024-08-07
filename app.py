from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello, welcome to testing APIs using Flask!"

@app.route("/about")
def about():
    return "Here is some information about me."

@app.route("/contact")
def contactus():
    return "MY contact details are ____________"

courses = [
    {
        "code": 101,
        "Name": "Diploma of IT",
        "Duration": "1.5 years"
    },
    {
        "code": 102,
        "Name": "Diploma of Web Dev",
        "Duration": "1.5 years"
    },
    {
        "code": 103,
        "Name": "Diploma of Data Science",
        "Duration": "2 years"
    },    
    {
        "code": 104,
        "Name": "Diploma of IT",
        "Duration": "3 years"
    },
    {
        "code": 105,
        "Name": "Diploma of Web Dev",
        "Duration": "3 years"
    },
    {
        "code": 106,
        "Name": "Diploma of Data Science",
        "Duration": "4 years"
    }, 
]


@app.route("/courses")
def list_courses():
    limit = request.args.get("limit")
    if limit:
        return courses[0:int(limit)]
    return courses

@app.route("/courses/101")
def get_course_101():
    return courses[0]

@app.route("/courses/102")
def get_course_102():
    return courses[0]

@app.route("/courses/200")
def error_route():
    return {"error": "Course does not exist"}, 404


# POST Request
# Add a new course
@app.route("/courses", methods=["POST"])
def add_course():
    body = request.get_json()
    courses.append(body)
    return courses

# DELETE Request
# Delete a course
@app.route("/courses/107", methods=["DELETE"])
def delete_course_107():
    del courses[-1]
    return {"message": "Duplicate course 107 successfully deleted!"}

# PUT and PATCH
# Updating an entire course
@app.route("/courses/107", methods=["PUT"])
def update_course_107():
    body = request.get_json()
    courses[-1] = body
    return courses[-1]

# PATCH Request
# Patching a part of a course
@app.route("/courses/101", methods=["PATCH"])
def patch_101():
    body = request.get_json()
    
    courses[0]["Duration"] = body.get("Duration") or courses[0]["Duration"]
    courses[0]["Name"] = body.get("Name") or courses[0]["Name"]
    
    return courses[0]

if __name__ == "__main__":
    app.run(debug=True)