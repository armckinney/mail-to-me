<!-- header -->
<div align="center">
    <p>
    <!-- Header -->
        <img width="100px" src="/static/Images/readme_logo.png"  alt="mail-to-me" />
        <h2>Mail To Me</h2>
        <p><i>Webpage Form Handler</i></p>
    </p>
    <p>
    <!-- Shields -->
        <a href="https://github.com/armckinney/mail-to-me/LICENSE">
            <img alt="License" src="https://img.shields.io/github/license/armckinney/mail-to-me.svg" />
        </a>
        <a href="https://github.com/armckinney/mail-to-me/actions">
            <img alt="Tests Passing" src="https://github.com/armckinney/mail-to-me/workflows/CI/badge.svg" />
        </a>
        <a href="https://codecov.io/gh/armckinney/mail-to-me">
            <img alt="Code Coverage" src="https://codecov.io/gh/armckinney/mail-to-me/branch/master/graph/badge.svg" />
        </a>
        <a href="https://github.com/armckinney/mail-to-me/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/armckinney/mail-to-me" />
        </a>
        <a href="https://github.com/armckinney/mail-to-me/pulls">
            <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/armckinney/mail-to-me" />
        </a>
        <a href="https://stackshare.io/armck/mail-to-me">
            <img alt="StackShare.io" src="http://img.shields.io/badge/tech-stack-0690fa.svg?label=StackShare.io">
        </a>
    </p>
    <p>
    <!-- Links -->
        <a href="https://armckinney.github.io/demo-to-me/">View Demo</a>
        ·
        <a href="https://github.com/armckinney/mail-to-me/issues/new/choose">Report Bug</a>
        ·
        <a href="https://github.com/armckinney/mail-to-me/issues/new/choose">Request Feature</a>
    </p>
</div>
<br>
<br>

<!-- Description -->
Mail-To-Me is a HTML Form handler hosted on Heroku. Its Flask-driven infrastructure listens for Form Submissions and redirects the information to the receiving email designated in the Form Submission Data Packet. Forms can come from anywhere and be redirected to anyone! This gives flexibility and ease of use when using contact forms on static websites like GitHub Pages! Feel free to give it a try by navigating to the Demo @ Demo-To-Me!

Here's why Mail-To-Me is important:
* Offers an easy solution to using Contact Forms on static web pages


### Building for Heroku Deployment
Heroku requires a `requirements.txt` in the root directory and Continuous Deployment is not configured for this repository. Thus, a manual dump of dependencies is required via executing `poetry export -f requirements.txt -o requirements.txt --without-hashes` prior to deploying on Heroku.