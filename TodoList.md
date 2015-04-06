
# litebook计划在将来的版本中实现的功能列表 #

## 短期目标 ##
  * ~~制作For Arch Linux的运行包~~
  * 检查更新 （已在ver1.5中实现）
  * [阅读历史全部记录](http://code.google.com/p/litebook-project/issues/detail?id=3)(已在ver1.51 中实现）
  * [目录选择侧栏](http://code.google.com/p/litebook-project/issues/detail?id=5)（已在ver1.5中实现）
  * [支持EPUB格式](http://code.google.com/p/litebook-project/issues/detail?id=10) (已支持）
  * [支持PDF格式](http://code.google.com/p/litebook-project/issues/detail?id=11)

## 中长期目标 ##
下面列出的是我对litebook未来发展的一些初步考虑，并不意味着肯定会按照这个列表去做。如果你有什么好的建议，欢迎给我Comments或是email。

  * 对保存用户的阅读数据进行数据挖掘，并实现和看书网站如douban的联动。(感谢Zoom.Quiet的建议）
  * 实现一个P2P的共享网络，方便大家对图书进行共享，目前的初步想法是Kademlia。不过一直没找到成熟的库，估计得自己写一个，工作量不小。 (已在3.0中支持)
  * 扩展目前所使用的TextCtrl控件的功能，从而能够实现一些高级的显示功能，如行间距/当前行高亮/页边距/全行下划线等。不过好像也没有现成的控件，也得自己写，而且还得用C++，也是个痛苦的事情。（已在2.0中实现）