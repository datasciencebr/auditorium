# Apoia.se Supporters Scrapper
A [Flask][1] app for scrapping [Apoia.se][2] supporters names.

#### Enviroment variables
We use [environment variables][3] to set the Apoia.se URL for this scrapper.
You can set yours by using:

```console
$ export APOIASE_URL='https://apoia.se/api/v1/users/serenata?format=json'
```

or any other Apoia.se API URL.

#### Virtual enviroments
We recomend that you use virtual environments to run this project.
You can do so by installing [virtualenv][4], which is a tool that
gives support to manage Python's virtual environments.

##### virtualenv
1. Install [virtualenv][4]

2. Create your Python 3 environment with:

```console
$ virtualenv -p python3 apoiase
```

3. Activate your environment using:

```console
$ source apoiase/bin/activate
```

4. Run the setup:

```console
$ python setup
```

#### Without virtual
If you want, you can only install the dependencies in your computer
by running:

```console
$ python3 setup
```

### Running the app
Following [Flask's new CLI][5] we need a environment variable with our app — 
optionally you can set the debug mode too:

```console
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
```

To start the server you can run the app locally on your terminal:

```console
$ cd apoiase/
$ flask run
```

and after that open a browser and access:

`localhost:5000`

If everything is working properly you should see a JSON with all not private
supporters names.


[1]: http://flask.pocoo.org/
[2]: https://apoia.se/
[3]: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps
[4]: https://virtualenv.pypa.io/
[5]: http://flask.pocoo.org/docs/0.12/cli/
