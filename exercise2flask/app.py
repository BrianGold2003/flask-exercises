from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def render_form():
    form = '''
            <div class="col-2">
                <h1>Home</h1>
                <h3>Enter an integer to find if it is even or odd</h3>
                <form action="calculate" method="post">
                    <label for="number">Number: </label>
                    <input type="text" id="number" name="number" placeholder="Enter a number:">
                    <button type="submit">Submit</button>
                </form>
            </div>
        '''
    return Response(form)


@app.route('/calculate', methods=["POST", "GET"])
def calculate():
    if request.method == "POST":
        number = request.form.get("number")

        if not number:
            return 'No number provided.<br><a href="/">Back to home</a>'
        elif number.isalpha():
            return f'{number} is not an integer!<br><a href="/">Back to home</a>'
        if int(number) % 2 == 0:
            return f'{number} is even.<br><a href="/">Back to home</a>'
        else:
            return f'{number} is odd.<br><a href="/">Back to home</a>'


if __name__ == '__main__':
    app.run()