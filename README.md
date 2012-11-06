exec_ruby_marker
================

This is a sublime plugin to execute the current view/buffer via Ruby and replace marker such as # => with actual calculated value

As an example the following line when executed would calculate the results

    1 + 1 # => 

Would become

    1 + 1 # => 2

For more details , see xmpfilter in the project https://github.com/tnoda/rcodetools

Prerequisites
-------------

- Sublime Text 2.x editor
- A version of ruby installed (1.8.7, 1.9 or 2.0).
- rcodetools gem installed (see following section on how to install it)

This also works with rvm or rbenv.

Installation
------------

First you need to install the following gem for all the version of ruby you will want to support

    gem install rcodetools

Next you will need to clone the repository into the packages folder

* On Linux
    
    cd $HOME/.gnome2/Sublime2/Packages/
    git clone git://github.com/epinault-ttc/exec_ruby_marker.git ExecRubyMarker

To use the plugin, press CTRL + SHIFT + C on the current selected file

* On OSX 

    cd $HOME/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    git clone git://github.com/epinault-ttc/exec_ruby_marker.git ExecRubyMarker

To use the plugin, press CMD + SHIFT + C on the current selected file
    
Configuration
-------------

The following settings are available to override the default ones. They should be added/merged into the normal User preferences in
Sublime

```python
{ 
  "ruby_exec": "/path/to/ruby",
  "xmpfilter": "/path/to/xmpfilter"
}
```

By default it picks the current installed Ruby on your machine as followed


```python
{ 
  "ruby_exec": "/usr/bin/ruby",
  "xmpfilter": "/usr/bin/xmpfilter"
}
```

* If you are using RVM, you should point the ruby_exec to **$HOME/.rvm/bin/rvm-auto-ruby**

* If you are using RBENV, you should point the ruby_exec to **$HOME/.rbenv/shims/ruby**
