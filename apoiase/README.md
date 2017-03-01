# Apoia.se Supporters Scrapper
A [Flask][1] app for scrapping [Apoia.se][2] supporters names.

#### Enviroment variables
We use [environment variables][3] to set the Apoia.se URL for this scrapper.
You can set yours by using:

`export APOIASE_URL='https://apoia.se/api/v1/users/serenata?format=json'`

or any other Apoia.se API URL.

#### Virtual enviroments
We recomend that you use virtual environments to run this project.
You can do so by installing [virtualenv][4], which is a tool that
gives support to manage Python's virtual environments.

##### virtualenv
1. Install [virtualenv][1]

2. Create your Python 3 environment with:

`virtualenv -p python3 apoiase`

3. Activate your environment using:

`source apoiase/bin/activate`

4. Run the setup:

`python setup`

#### Without virtual
If you want, you can only install the dependencies in your computer
by running:

`python3 setup`

### Running the app
To check your work you can run locally the app on your terminal run the following:

`python3 app.py`

and after that open a browser and access:

`localhost:5000`

If everything is working properly you should see a JSON with all not private
supporters names.


[1]: https://apoia.se/
[2]: http://flask.pocoo.org/
[3]: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps
[4]: https://virtualenv.pypa.io/
