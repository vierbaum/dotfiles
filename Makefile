install:
	# qtile
	mkdir "$(XDG_CONFIG_HOME)/qtile"
	ln -s $(shell pwd)/qtile/config.py $(XDG_CONFIG_HOME)/qtile/config.py
	ln -s $(shell pwd)/colors.py $(XDG_CONFIG_HOME)/qtile/colors.py

	# alacritty
	ln -s $(shell pwd)/alacritty/alacritty.toml $(XDG_CONFIG_HOME)/alacritty.toml
