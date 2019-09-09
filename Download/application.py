from PIL import Image
from io import BytesIO
from flask import Flask, render_template, Response, request
app = Flask(__name__)


@app.route('/multi')
def multi():
    return render_template('multi.html')


@app.route("/download", methods=["POST"])
def download():
    data = request.form.to_dict()
    rgb = tuple(int(v) for v in data.values())

    new_im = Image.new("RGB", (200, 200), color=rgb)
    evt = BytesIO()  # save image in buffer
    new_im.save(evt, format='png')
    evt.seek(0)

    return Response(
        evt, mimetype="image/png",
        headers={"Content-disposition": "attachment; filename=data.png "}
    )


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)  # start a local server
