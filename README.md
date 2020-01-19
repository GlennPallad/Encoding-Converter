* [en_US](#en_us)
* [zh_CN](#zh_cn)

# en_US
## <font style="color: #E91E63">!!! CAUTION !!!</font> 
This program will directly modifies your <b style="color: #E91E63">SOURCE FILES WITHOUT COPY</b>, so make sure to <b style="color: #E91E63">BACK UP</b> before using.

## Usage
### Tools you will need:
* Make sure you have [Python 3](https://www.python.org/downloads/) installed already.
* (Optional) A user-friendly terminal(e.g. [Cmder](http://cmder.net/)).
* (Optional) [Notepad++](https://notepad-plus-plus.org/)

### What's it for?
So let's say you have a messy project folder named **Example** like this:
```
Example(folder)
	├─ A(folder)
	│	├─ A.1(folder)
	│	│	└─ A.1(UTF-8)
	│	├─ A.2(folder)
	│	│	└─ A.2(GB2312)
	│	└─ A.3.txt(GB2312)
	├─ B(folder)
	│	└─ B.1(GB2312)
	├─ whatever.c(folder)
	│	└─ whatever.c(GB2312)
	└─ D.txt(GB2312)
```
And you wanna convert all `GB2312` encoded text files under **Example** folder(including subfolders) to `UTF-8` encoding, these files have different extension names(for example`.c` `.txt`), and there are already some files was encoded in `UTF-8`. I know many editors(e.g. [Notepad++](https://notepad-plus-plus.org/)) have the function of converting files encoding, but you don't wanna do 'open-convert-save' job one by one right? So let's do it only once.

### How to use it?
1. Place `EncodingCoverter.py` under your project folder, for example above, it will looks like this:
```
Example(folder)
	├─ A(folder)
	│	├─ A.1(folder)
	│	│	└─ A.1(UTF-8)
	│	├─ A.2(folder)
	│	│	└─ A.2(GB2312)
	│	└─ A.3.txt(GB2312)
	├─ B(folder)
	│	└─ B.1(GB2312)
	├─ whatever.c(folder)
	│	└─ whatever.c(GB2312)
	├─ D.txt(GB2312)
	└─ EncodingCoverter.py
```

2. Open `EncodingCoverter.py` file, edit codes in `line 4`(sourceEncoding) and `line 5`(targetEncoding) to meet your needs.
Edit codes in `line 46`, you can add extension names or remove extension names as you want, for example there are some `GB2312` encoded `.js` files in your project, and you wanna convert them to `UTF-8`, you can modify it to
```
if extension == '.h' or extension == '.c' or extension == '.cpp' or extension == '.txt' or extension == '.js':
```
save `EncodingCoverter.py` file before you quit it.

3. Open your terminal and navigate to your project folder, run
```
python EncodingConverter.py
```
For the example above, you'll see this
```
python EncodingConverter.py
Files didn't convert:
./A/A.1/A.1.txt
```
The reason why `./A/A.1/A.1.txt` didn't convert is it's not a `GB2312` encoding file(it's a `UTF-8` encoding file), so it was ignored during converting.

# zh_CN
## <font style="color: #E91E63">!!! 警告 !!!</font> 
该程序将直接修改你的 <b style="color: #E91E63">源文件</b>, 使用前请务必 <b style="color: #E91E63">备份</b> 你的源文件.
