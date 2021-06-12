[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![Issues2][issues2-shield]][issues2-url]

          
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio">
    <img src="app/static/img/MLH_Logo.svg" alt="Logo" width="200" height="100">
  </a>

  <h3 align="center">Pod 3.3.0 Team 1 Portfolio</h3>

  <p align="center">
    A great kickoff to the MLH Production Engineering Fellowship!
    <br />
    <a href="https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio"><strong>Explore the repo »</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">View Demo</a>
    ·
    <a href="https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/issues">Report Bug</a>
    ·
    <a href="https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributors">Contributors</a></li>
     <ul>   
         <li><a href="#github">Github</a></li>
         <li><a href="#linkedin">LinkedIn</a></li> 
     </ul>
    <li><a href="#devpost">Devpost</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About the Project

Welcome to pod 3.3.0 team 1's portfolio webpage! As you may or may not know, our pod's nickname is the C Turtles. We wanted to incorporate this theme and represent it on our landing page with a unique underwater design. The portfolio overall runs from a Flask server written in Python and features the use of Bootstrap for our styling where ✨aesthetic✨ animations and transitions have been applied! 

Upon establishing the Flask server and accessing our page, you will be welcomed by our __Landing Page__ designed by 
[Carlos Ricoveri](https://github.com/carlosricov) and [Jorge Sanchez](https://github.com/S4ND1X). If interested in learning more about our pod, feel free to explore the __About__ section, also designed by Jorge. For the time being, only the profiles of the members of team 1 will be accessible. To see them, click on the corresponding image within the landing page. The profile section was designed by [Saul Montes De Oca](https://github.com/saulmontesdeoca). A primitive design created on Figma is shown here _(please note this is a WIP and the design is not yet finalized)_:

![Figma Landing Page Revised Design][product-screenshot]

### Built With
* [Bootstrap](https://getbootstrap.com)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Figma](https://www.figma.com/)

## Getting Started

In order to successfully run our webpage, you must follow these steps and adhere to the prerequisites. This will ensure you establish a correct running environment. For the sake of good practice, we recommend using a virtual environment and will thus be showing how to set that up in the following sub-sections!

### Prerequisites 
* [Bash](https://www.gnu.org/software/bash/manual/html_node/Installing-Bash.html)
* [Python](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
* _pip3_ or _pip_
* _virtualenv_
* Flask

### Installation

To install _pip3_ run the following commands in your bash terminal:

* Update your system:
```sh
sudo apt-get update
```
* Pip3 install:
```sh
sudo apt-get -y install python3-pip
```

* Verify installation:
```sh
pip3 --version
```
Once _pip3_ is installed, we can now install virtualenv packages.

* Virtualenv: 
```sh
python3 -m pip install --user virtualenv
```
* Verify installation:
```sh 
virtualenv --version
```
Once that completes, download or clone this repository and using the bash shell navigate into the _../app/_ folder. From here we are ready to set up our virtual environmment.

* Set up virtual environmment:
```sh
virtualenv env
```

* Activate virtual environment:
```sh
source /env/bin/activate
```

From there you should see a _(environment)_ indicator appear in your shell. If this does not appear, please retrace your steps. The next item needed is Flask. 

* Install Flask:
```sh
pip3 install Flask
```

From here your environment should be ready to go! Congrats 🎊 

## Usage
To run the app you have to follow the next commandlines:
```ssh
git clone git@github.com:MLH-Fellowship/LATAM-C-Turtles-Portfolio.git
cd LATAM-C-Turtles-Portfolio
pip3 install -r requirements.txt
python3 app.py
```

## Contributors
This team is composed of 3 members. Below are their Github and LinkedIn accounts.

### Github
[Jorge Sanchez](https://github.com/S4ND1X)

[Carlos Ricoveri](https://github.com/carlosricov)

[Saul Montes De Oca](https://github.com/saulmontesdeoca)

### LinkedIn
[Jorge Sanchez](https://www.linkedin.com/in/jorgesanchezdiaz/)

[Carlos Ricoveri](https://www.linkedin.com/in/carlosricoveri/)

[Saul Montes De Oca](https://www.linkedin.com/in/saulmontesdeoca/)

## Devpost
[Check it out]()

## License
[LICENSE](https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/LICENSE)

## Acknowledgements
[GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)

[Img Shields](https://shields.io)

[Pip3 Install](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)

[Readme Template](https://github.com/othneildrew/Best-README-Template)

[Wave Animations](https://www.youtube.com/watch?v=MMNEEdGa5eE)

[Flask Blog Template MLH Logo](https://github.com/MLH-Fellowship/flask-blog)

[Turtle clipart](https://www.jing.fm/iclipt/oomTim/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/images/Contributors.svg
[contributors-url]: https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/graphs/contributors
[issues-shield]: https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/images/issues.svg
[issues-url]: https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/issues
[issues2-shield]: https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/images/issues2.svg
[issues2-url]: https://github.com/MLH-Fellowship/LATAM-C-Turtles-Portfolio/issues
[product-screenshot]: images/landingpage.png

