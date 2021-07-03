from flask import Flask, jsonify, request
from parse_json import *
from send_command import *
import os
import glob

app = Flask(__name__)


@app.route("/get_txt_jsons", methods=["POST"])
def send_jsons():
    project_id, job_id, save_path, current_file = request.body

    command_result = send_command({"PROJECT_ID": project_id, "JOB_ID": job_id, "SAVE_PATH": save_path, "CURRENT_FILE": current_file, "COMMAND": "get_text"})

    if command_result["command"] == "Get Text Done":
        json_file = glob.glob(f"{save_path}/*.json")[0]

        return jsonify({"jsons": parse_jsons(json_file)})
    else:
        return jsonify({"jsons": "An error occured"})


@app.route("change_jsons", methods=["POST"])
def send_jsons():
    save_path, req_jsons = request.body


    json_file = glob.glob(f"{save_path}/*.json")[0]

    return jsonify({"save_result": save_jsons(json_file, req_jsons)})
    


@app.route("set_txt_jsons", methods=["POST"])
def send_jsons():
    project_id, job_id, save_path, current_file = request.body

    command_result = send_command({"PROJECT_ID": project_id, "JOB_ID": job_id, "SAVE_PATH": save_path, "CURRENT_FILE": current_file, "COMMAND": "set_text"})

    if command_result["command"] == "Set Text Done":        
        return jsonify({"text_set": True})
    else:
        return jsonify({"text_set": False})


if __name__ == "__main__":
    app.run()