from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request, send_file
app = Flask(__name__)


@app.route('/multi')
def multi():
    return render_template('multi.html')


@app.route('/post_catcher', methods=["POST"])
def post_catcher():
    data = request.form.to_dict()
    rgb = tuple(int(v) for v in data.values())

    new_im = Image.new("RGB", (200, 200), color=rgb)
    evt = BytesIO()  # save image in buffer
    new_im.save(evt, format='png')
    evt.seek(0)
    return send_file(evt, mimetype='image/png')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)  # start a local server
