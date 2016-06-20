# smyck_pygment

Pygment version of [Smyck](https://github.com/hukl/Smyck-Color-Scheme) color scheme.

### Installation
To use with [Rouge](https://github.com/jneen/rouge), you can use the `.css` and
change `.highlight` to whatever class you're using. You should be able to copy
and paste this file to use with Jekyll.

If you alter `smyck.py`, you'll need [Pygments](http://pygments.org) installed.
Once installed, move `smyck.py` to the Pygment's path and place it in the `../style/`.

Then you can generate the CSS by running:

```
pygmentize -S smyck -f html -a .highlight > smyck.css
```
