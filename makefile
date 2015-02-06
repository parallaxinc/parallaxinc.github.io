all: #css/style.css
	jekyll serve

#css/style.css: less/style.less less/custom_variables.less
#	lessc less/style.less > css/style.css

install:
	sudo apt-get install ruby ruby-dev make nodejs
	sudo gem install jekyll --no-rdoc --no-ri
	sudo gem install github-pages --no-rdoc --no-ri
