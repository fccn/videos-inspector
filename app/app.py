import os
import shutil
from flask import Flask, flash, redirect, render_template, request, send_file, url_for

from services.process_file_service import ProcessFileService

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "fileInput" not in request.files or not request.files["fileInput"].filename:
            flash("No file selected!", "error")
            return redirect(url_for("index"))

        try:
            file = request.files["fileInput"]
            flash(f"File '{file.filename}' uploaded and processed successfully, staring process..", "success")
            output_save_path = ProcessFileService().process_file(file)
            return send_file(output_save_path, as_attachment=True, download_name="output.xlsx")
        except:
            flash("An error occurred", "error")
        finally:
            os.remove(file.filename)
            shutil.rmtree("output")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)