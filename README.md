# WeeChat Scripts

This repository contains all my WeeChat scripts.

- [chancomp.py](chancomp.py)
  - Compares channels with a different user via WHOIS and returns the number
    of channels being shared between the two.

## Installation

Copy the file source in to `~/.weechat/{script_language}/` and run `/script load {script_name}.extension`

Proceed by configuring the script (if it has any configuration options) with /help 
and `/set plugins.var.{script_language}.{script_name}.*`

For a python script, the weechat directory path would be `~/.weechat/python/`, and the set command would be
`plugins.var.python.`

For further support, refer to the 
[weechat script documentation](https://weechat.org/files/doc/stable/weechat_quickstart.en.html#plugins_scripts)

## License

All my plugins are licensed under the MIT license. See [the license](LICENSE) for more information.
