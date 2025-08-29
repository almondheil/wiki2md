# This is an example wiki file

It has all of the features we care about converting, which are:

  - headers
  - **bold**
  - *italics*
  - code fenced sections
  - `inline code`

And no, it does **NOT** do anything to convert [[links]]. Those stay the same.

## Code might be complicated

Obviously, if we have **bold** or even ***bold italics*** in normal text they should be converted.

```
but in a fenced block, *bold* and _*bold italics*_ should stay the same.
```

```python
def fenced_blocks_should(also):
  keep_their['languages'] = True
```

the same logic should apply to `inline code`, where `wiki-style *bold* and _italics_ inside of them` should not get converted.

###### here is a random h6 because why not

  1. you should also expect
  2. that lists stay the same
    a) including the fancy sub-items
    b) although idk if markdown fully supports these
  3. they are not something I am willing to convert
    - and idk if I have the ability, to be honest.
