### [README- get_data](https://github.com/gadia-aayush/AayushGadia_Submission/tree/master/aayushassign/get_data)


#### Description-
- It is a **GET API**.
- Fetches the data in JSON in the [**given format**](rough/TestJSON.json)
- Here we have 2 models- **User** & **ActivityPeriod**.
  - **User model** has **u_id** (user id, here it is also a primary key), **u_name** (user full name) & **u_tz** (user time zone) as the fields.
  - **ActivityPeriod model** has **u_id** (user id), **start_timestamp** (start timestamp of the activity) & **end_timestamp** (end timestamp of the activity) as the fields.
  - All the fields in both the models are **CharField** with maximum length of **255**.
- The Database Table Name of **User model** is **user**, & **ActivityPeriod model** is **activityperiod**.
- We are using the default **Sqlite database** for storing the data.
- Also, custom management command has been written to populate the database with dummy data. <br>[**Here is the link**](https://github.com/gadia-aayush/AayushGadia_Submission/blob/master/aayushassign/get_data/management/commands/populatedata.py)

---

#### Requirements-
- [**Link to Requirements file**](requirements.txt)

---

#### API Endpoint-
- http://aayushgadia.pythonanywhere.com/get-data/

---

#### Test Data-
- No data to pass, since **GET API**.

---

#### Output Screenshots-
- **Server :**
![server](rough/server.png)

- **Local Host :**
![local](rough/local.png)

- [JSON Output File](rough/aayush_response.json)

---

#### AUTHOR-
- **coded by AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
