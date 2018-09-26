# WICS Website

This repository holds the WICS website's source code!

## Contributing to the Site

You don't need much to work on the site, just a text editor and a few basic tools.
Here is a guide to get you started.

Before anything else, if you run into issues with this guide, don't hesitate to reach out over Slack, we're happy to help out!

### Installing an Editor

A decent all-round editor/IDE is IntelliJ: download [here](https://www.jetbrains.com/idea/download/).
However, everyone has their own preference and you're welcome to use whatever you like.

### Setting up Git

See [this article](https://help.github.com/articles/set-up-git/).
You don't need to worry about the "Authenticating with GitHub from Git" section, just complete 1-3.

### Making Changes

Once you have Git installed, clone the repository, then change directory to it with this command:

```sh
$ git clone https://github.com/umwics/wics-site
$ cd wics-site
```
Next, create a new branch.
You should name it something concise but relevant to what you're going to work on.
Here I've used the name `fix-broken-link` to hint at what my branch will contain.

```sh
$ git checkout -b fix-broken-link
```

Now feel free to make changes to the site!

### Testing the Site Locally

Now that you've made some changes, you probably want to see what they look like.

[This article](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/) describes everything here and more, but some of it is not necessary and might just trip you up.

**Note**: If you're on Windows, you should run the commands listed here with Git Bash, which should have been installed along with Git.
If you're on Linux or MacOS, use your terminal to run the commands.

You will need the Ruby programming language and `bundler` installed on your computer.

To install Ruby, go [here](https://www.ruby-lang.org/en/downloads/) and follow the instructions.

Now with Ruby installed, you should be able to install `bundler` with the `gem` utility (Ruby's package manager) with the following command:

```sh
$ gem install bundler
```

You might see a warning that looks like so:
```
WARNING:  You don't have /homedir/.gem/ruby/2.5.0/bin in your PATH,
          gem executables will not run.
```

If so, run this command, replacing the path with the exact path found in the warning message:

```sh
$ export PATH=$PATH:/homedir/.gem/ruby/2.5.0/bin
```

Next, change directory to the repository and install the site's dependencies (this might take a while).

```sh
$ cd <repo>  # Skip this step if you're already inside the WICS website repository, otherwise replace <repo> with the path to the repository.
$ bundle install
```

We're ready now to run the website.
Run the following command:

```sh
bundle exec jekyll serve
```

You should see a message that ends with these lines (or similar):

```
Server address: http://127.0.0.1:4000/~wics/
Server running... press ctrl-c to stop.
```

Now you can navigate to `http://localhost:4000/~wics/` to view the  website.
Note that the trailing slash is necessary!

While the site is running, you can edit pages and they will update in real time.

## Submitting Changes

Now that you've written a great new feature, the next step is to *commit* those changes, and *push* them to the GitHub repository.
Afterwards, you will make a *pull request* for us to review and *merge*.

First, we need to *stage* our files with this command:

```sh
$ git add .
```

Next, make a *commit*.
Your *commit message* should concisely describe what you did.

```sh
$ git commit -m 'Fix broken link to CSS tutorial'
```

Now, *push* the commit to the GitHub repository.

```sh
$ git push origin fix-broken-link  # Remember to use the same name as your own branch!
```

Here, Git will ask you for your username and password.
Enter your GitHub username and password here.

Finally, create a *pull request*.
To do so, follow the instructions found [here](https://help.github.com/articles/creating-a-pull-request/)!

With all this done, you may receive some feedback or requests for changes, or it may be merged straight into the live website.

## Learning Resoures

Here are some tutorials for getting you on your feet with various tools and technologies:

* [Git](https://try.github.io/levels/1/challenges/1)
* [HTML](https://www.w3schools.com/html/html_intro.asp)
* [CSS](https://www.w3schools.com/css/css_intro.asp)
* [Bootstrap](https://www.w3schools.com/bootstrap/bootstrap_get_started.asp)
