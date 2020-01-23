# align-yaml Python version

> Format, prettify, align, whatever you want to call it. This does that to YAML. Great for making long config files more readable!

Reformats this:

```yaml
one: two
three: four
seventeen: five
```

to this:

```yaml
one:       two
three:     four
seventeen: five
```

## How to use

Pass a string to align(str). This is important! Read in the YAML as a string, DON'T PARSE IT.

## Credits

Translated to Python from https://github.com/jonschlinkert/align-yaml
