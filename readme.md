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
	Edit codes in `line 35`, you can add extension names or remove extension names as you want, for example there are some `GB2312` encoded `.js` files in your project, and you wanna convert them to `UTF-8`, you can modify it to
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
Files didn't converted:
./A/A.1/A.1.txt
```
The reason why `./A/A.1/A.1.txt` didn't converted is it's not a `GB2312` encoding file(it's a `UTF-8` encoding file), so it was ignored during converting.

# zh_CN
## <font style="color: #E91E63">!!! 警告 !!!</font> 
改程序将直接修改你的 <b style="color: #E91E63">源文件</b>, 使用前请务必 <b style="color: #E91E63">备份</b> 你的源文件.

## 使用
### 你需要的工具:
* 安装 [Python 3](https://www.python.org/downloads/)。
* (非必须) 一个好用的终端(e.g. [Cmder](http://cmder.net/))。
* (非必须) [Notepad++](https://notepad-plus-plus.org/)。

### 这个程序是用来干嘛的？
假设你有个叫做 **Example** 的凌乱的项目文件夹：
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
你想将所有 `GB2312` 编码的 **Example** 目录下（包括子目录）的文件转换为 `UTF-8` 编码, 这些文件的扩展名不一定一样(比如有`.c` `.txt`), 并且有些文件本来就是 `UTF-8` 编码的。 我知道有些编辑器(比如 [Notepad++](https://notepad-plus-plus.org/)) 自带文件编码转换功能, 但你不想一个一个地手动转换对吧？ 那就一次全都转换掉吧。

### 怎么用啊？
1. 把 `EncodingCoverter.py` 放到你的项目目录下, 以上面的例子来说，就是这样：
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
2. 打开 `EncodingCoverter.py` 文件, 编辑 `第4行`(原来的编码) 和 `第五行`(想要的编码) 来满足你的需要。
	编辑 `第35行`添加或删除文件扩展名，比方说你的项目文件中有一些 `GB2312` 编码的 `.js` 文件你想改为 `UTF-8` 编码，你可以将这行代码修改为
	```
			if extension == '.h' or extension == '.c' or extension == '.cpp' or extension == '.txt' or extension == '.js':
	```
	退出 `EncodingCoverter.py` 文件之前记得保存。
3. 打开你的终端，将路径改到你的项目文件目录下，运行
```
python EncodingConverter.py
```
对于上面的例子，你会看到
```
python EncodingConverter.py
Files didn't converted:
./A/A.1/A.1.txt
```
`./A/A.1/A.1.txt` 没被转换的原因是它不是你所指定的 `GB2312` 编码文件所以程序会忽略它。
