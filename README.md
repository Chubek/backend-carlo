# Media Translator Backend

This is the backend for Media Translator. It gets, changes, and sets MOGRTs using Premiere application. It also has the ability to launch more than once instance of Premire with with the exchange CEP panel starting on different ports.


# How it works
## CEP Panel
This backend requires a CEP panel made by me. This CEP panel runs two JSX files, one that gets MOGRTs and one that sets MOGRTs.

You can download the CEP panel from here:

```
 https://github.com/Chubek/cep-panel-for-carlo
 ```

 ## Getting and Setting MOGRTs
So here's how it works. You first send a request to `/get_txt_jsons`, given a save path, and your current `.prproj` file. It will exract the texts, and save them in the save path as a singular JSON file that resembles `sample_json.json`.

After that is all done, you should change the JSONs yourself or via a frontend. In casae of the latter, please send a request to `/change_jsons`. It will change the JSON file based on the jsons in the request body.

Then send a request to `/set_txt_jsons`. It will set the MOGRTs for the file based on the saved JSON.

## Starting a Premiere Instance
This is a concurrent application. It uses Sandboxie to launch multiple instances of Premiere. Even if you're testing it locally, DO NOT run Premiere yourself. Use `/op_prem_instance`. It will launch a Premiere instance with the CEP panel's port set to the port youp give it. You can also stop a certain instance using this endpoint.


# Endpoints

The following table lists the endpoints of this backend:

|Endpoint|Body/Args|Job|
|--------|---------|---|
|GET /op_prem_instance?port=port&action=action|action: start or stop<br> port: Target port|Starts or stops a Premiere instance|
|POST /get_txt_jsons|project_id: ID of the project, can be anything<br> job_id: ID of the job, can be anything<br>save_path: Path to save the JSONs<br>current_file: Current prproj file|Gets the MOGRTs and saves them in a folder|
|POST /set_txt_jsons|project_id: ID of the project, can be anything<br> job_id: ID of the job, can be anything<br>save_path: Path to the saved the JSONs<br>current_file: Current prproj file|Sets the MOGRTs based on what is in the folder|
|POST /change_jsons|save_path: Path to the JSONs<br>req_jsons: An array of JSONs you have changed, refer to `sample_jsons.json`.|Change JSONs in folder.|


# Environment Variables
Create a file called `.env` in the root. It should contain the following environment variables:

|Variable|Job|
|--------|---|
|ASSIGN_PORT_LOC|A text file that contains all the assigned ports, no need to create it.|
|BUSY_PORT_LOC|A text file that contains all the busy ports. No need to document it.|
|ADDRESS|Your address, like localhost.|
|PATH_TO_PREMIERE|Path to Premiere executable file.|


# How to Set Up?
1. Clone.
2. Create a Conva env or a VirtualEnv.
3. `pip install -r requirements.txt`
4. Run the [pywin32 post install script](https://github.com/mhammond/pywin32#installing-via-pip)
5. Run `python prem_app.py`


# Notes
This app is still in the testing stage. Report errors to Chubak#7400.