# zalgoify
A small library to process zalgo text, as on [eeemo.net](https://eeemo.net).

Some initial code based on Gregory Neal's [zalgo-text](https://github.com/gregoryneal/zalgo) package.

# Installation
To install the package from `pip`:

    pip install zalgoify

Then in your project you can use it like so:

```py
import zalgoify
print(zalgoify.process("Some text to zalgoify!"))
```

(This would print `S͈̝ͨơ̖̬͔͐̅ͤm̱̪͇̎̈́̋e̮͇̲̅͛̕ t͖͖̰̆̒̇҉̨e̛̙͔̍͗́x̷̶͓̅t̹̙̠͗ͤ́ t̲̦̦ͤͧ͢o͇̝̥͒́̏ z̷̢̬͚̪̾̈́a̧̯̙ͥl̨̯̘ͦg̸̛̰̻̲ͯ̎ǫ̺̦ͬͩͅif̖̰̰̉y̛͍̘̏̅̍!`)

To remove zalgo diacritics from text, use:

```py
print(zalgoify.strip(text))
```
