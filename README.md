# To Tanami:

Please make a README based on the flask app.

How to use:

1- You need Premiere running, with the CEP panel that I've made.

2- Endpoints:

```
/get_txt_jsons

BODY PARAMS: project_id, job_id, save_path, current_file

Returns: {"jsons": parse_jsons(json_file)}
```

Create text fields for these jsons. Let users edit them. Run Length should change based on the changed text length.


```
/change_jsons

BODY PARAMS: save_path, req_jsons

Returns: {"save_result": save_jsons(json_file, req_jsons)}
```

This saves the changed JSONs in the file.


```
/set_txt_jsons

BODY PARAMS: project_id, job_id, save_path, current_file

Returns: {"text_set": True | False}

```

Run this after you've changed the JSONs. It will change the file, provided CEP is running.