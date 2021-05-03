# Summary of the code and what I tried

## Decompiling

Used this link [here](https://gchq.github.io/CyberChef/#recipe=Zlib_Deflate('Dynamic%20Huffman%20Coding')Zlib_Inflate(0,0,'Adaptive',false,false)From_Hex('None')Zlib_Inflate(0,0,'Adaptive',false,false)) to expand the grossness of the code from zlib to standard python

## What I did then
I hooked the python3 debugger from Visual Studio Code to the nasty program. Found out that the debugger does not enter the mainloop of tkinter because tkinter runs on a seperate process and therefore immutable. That is just a guess I do not know

## The error

There was a line on error 90, so I went there and saw this
```python
sample_KHTs = (array(release_times) - array(press_times)).tolist()
```
After adding a try except statement, we deduced that it was the release_times not being filled with values. 

## The "bang head against wall error"

Where the release_times were be being populated was a weird edge case with this line
```python
if (key.char in VALID_KEYS):
    release_times.append(time())

```
was not working while

```python
if (key.char in "".join(VALID_KEYS)):
    release_times.append(time())
```
Allows for release_times to be filled with actual values
But then the program stopped executing, never reaching the return or debug statement :(


