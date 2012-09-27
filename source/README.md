# SGVLUG Website

## Contributing

This site uses [Octopress](http://octopress.org/). In order to contribute you must first [setup](http://octopress.org/docs/setup/) Octopress according to their [documentation](http://octopress.org/docs/). Their documentation contains easy to follow step-by-step instructions for setting up and getting started using their software.

The "master" branch is the Jekyll processed version of the site. It is the branch that will show this README when you view the website's Github source. Do not edit on this branch, instead edit on the "source" branch. To set up your clone of the site properly, perform the following steps:

     git clone git@github.com:sgvlug/sgvlug.github.com.git
     git checkout source # checkout the branch where you make changes
     rake setup_github_pages[git@github.com:sgvlug/sgvlug.github.com.git] # setup Octopress to enable deploy task

You can [add content](http://octopress.org/docs/blogging/) with one of these two commands:

     rake new_post["title"]
     rake new_page[filename]

See the Octopress [documentation](http://octopress.org/docs/) for more information.

To [deploy to Github](http://octopress.org/docs/deploying/github/) you generally will execute:

     rake generate
     rake deploy

Then commit the changes you have made on the source branch and push to Github:

     git add <files you changed or added>
     git commit -m "My commit message"
     git push origin source

## License

[Creative Commons](http://creativecommons.org/licenses/by-nc-sa/3.0/)
