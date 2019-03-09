# E-Fonenana Polymer

## Scripts

- Initial setup: `script/setup`
- Production build: `script/build_frontend`
- Gallery: `cd gallery && script/develop_gallery`

## Frontend development

### Classic environment

#### Getting the code

First clone the project

```bash
git clone ...
```

#### Configuring

You will need to have an instance of E-Fonenana setup.

Next step is to configure E-Fonenana to use the development mode for the frontend. Do this by updating the frontend config in your configuration.yaml and set the path to the project repository that you cloned in the last step:

```yaml
frontend:
  # Example absolute path: /home/paulus/dev/frontend
  development_repo: <absolute path to repo>
```

#### Installing Node.js 8.x

Node.js is required to build the frontend. The preferred method of installing node.js is with nvm. Install nvm using the instructions in the README, and install the correct node.js by running the following command:

```bash
nvm install 8.15
```

Yarn is used as the package manager for node modules. Install yarn using the instructions [here](https://yarnpkg.com/en/docs/install).

Next, development dependencies need to be installed to bootstrap the frontend development environment. Download all the dependencies:

```bash
script/bootstrap
```

#### Development

During development, you will need to run the development script to maintain a development build of the frontend that auto updates when you change any of the source files. To run this server, run:

```bash
script/develop
```

#### Building the Polymer frontend

If you're making changes to the way the frontend is packaged, it might be necessary to try out a new packaged build of the frontend in the main repository (instead of pointing it at the frontend repo). To do so, first build a production version of the frontend by running `script/build_frontend`

To test it out inside E-Fonenana, run the following command from the main E-Fonenana repository:

```bash
pip3 install -e /path/to/frontend/
hass --skip-pip
```

#### Generating distribution archives

Make sure you have the latest versions of setuptools and wheel installed:

```bash
python3 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```bash
python3 setup.py sdist bdist_wheel
```

This command should output a lot of text and once completed should generate two files in the dist directory:

```bash
dist/
  example_pkg_your_username-0.0.1-py3-none-any.whl
  example_pkg_your_username-0.0.1.tar.gz
```

### Docker environment

It is possible to compile the project and/or run commands in the development environment having only the [Docker](https://www.docker.com) pre-installed in the system. On the root of project you can do:

- `sh ./script/docker_run.sh build` Build all the project with one command
- `sh ./script/docker_run.sh bash` Open an interactive shell (the same environment generated by the _classic environment_) where you can run commands. This bash work on your project directory and any change on your file is automatically present within your build bash.

**Note**: if you have installed `npm` in addition to the `docker`, you can use the commands `npm run docker_build` and `npm run bash` to get a full build or bash as explained above

## License

E-Fonenana is open-source and Apache 2 licensed. Feel free to browse the repository, learn and reuse parts in your own projects.
