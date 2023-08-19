# 空 kong
键盘组合键编辑器，fn层设定 Keyboard Combination Editor

bilibili：慵懒的叮咚   微博：慵懒的叮咚  微信公众号：叮咚的学习小屋

文件夹里面一共是3个文件
icon.png      是图标文件，可以自己替换，这样显示在右下角的图标会变换

kong-fn层编辑器.exe       是主程序，双击打开即可

keys_key.json       是快捷键数据文件，可以在里面编辑想要的组合方式
你可以用txt的方式打开这个文件，或者直接右键编辑
第一次打开的时候大概是以下状态：
{
    "name": "Key.caps_lock",
    "o": "delete",
    "u": "Backspace",
    "i": "up",
    "k": "down",
    "j": "left",
    "l": "right",
    "c": "ctrl+c",
    "v": "ctrl+v",
    "h": "enter"
}

除了第一行的name不能换其它都可以换

name右边的Key.cap_lock是一个超级键，可以理解成fn键，你可以替换成任何按钮，如果只需要替换成字母键的话直接打字母就行
如果你要替换成如“space”或“ctrl”这样的功能键的话，需要加上Key.的前缀，空格需要用_代替，
而且有左右区别的话需要加上后缀，如：“Key.ctlr_l”或“Key.ctlr_r”
记住K要大写！！！


第二行开始：
“：”号的左边为要和超级键组合的按键，右边为主要功能
左边的输入也是跟超级键一样的加前缀和后缀
右边则是要实现的功能，不要加什么前后缀，并且需要组合键的话就用+号链接就行

可以b站或者微博搜索：慵懒的叮咚  ，获取使用视频

==============================================================================================================================
Keyboard combination key editor, fn layer setting Keyboard Combination Editor

bilibili: 慵懒的叮咚  Weibo: 慵懒的叮咚  WeChat Official Account: 叮咚的学习小屋

There are a total of 3 files in the folder
icon.png is the icon file, you can replace it yourself, so the icon displayed in the lower right corner will change

kong-fn layer editor.exe is the main program, double-click to open

keys_key.json is the shortcut key data file, you can edit the desired combination method inside
You can open this file with a text editor or directly right-click to edit
The initial state when opened for the first time is approximately as follows:
{
"name": "Key.caps_lock",
"o": "delete",
"u": "Backspace",
"i": "up",
"k": "down",
"j": "left",
"l": "right",
"c": "ctrl+c",
"v": "ctrl+v",
"h": "enter"
}

Except for the first line where the name cannot be changed, everything else can be changed

The Key.caps_lock on the right side of the name is a super key, which can be understood as the fn key. You can replace it with any button. If you only need to replace it with a letter key, just type the letter
If you want to replace it with functional keys like "space" or "ctrl", you need to add the prefix Key., and use "_" to represent the space.
And if there is a left-right distinction, you need to add a suffix, such as "Key.ctlr_l" or "Key.ctlr_r"
Remember that K must be capitalized!!!

Starting from the second line:
The left side of the colon ":" is the key to be combined with the super key, and the right side is the primary function
The input on the left side also requires adding prefixes and suffixes just like the super key
On the right side, you implement the desired function without adding any prefixes or suffixes, and if you need a combination key, use the plus sign "+" to link them

You can search on Bilibili or Weibo: "慵懒的叮咚" to get instructional videos.
