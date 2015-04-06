**Note: litebook 2.0测试版已经放入SVN中，欢迎尝鲜。**

litebook 2.0中最主要的改进是放弃了1.0中使用的wxpython自带的简单文本控件，而是从头写了一个专为“显示文本”而优化的文本控件：liteview，具备如下特点：
  * 只读
  * 三种不同的显示模式：纸张/书本/竖排书本
  * 载入排版速度和文本大小无关，也就是说，载入20M的文本的时间和载入2M文本的时间几乎是一样的。
  * 支持背景图片
  * 页边距/行间距可调
  * 支持不同类型的下划线
  * 字体/大小/颜色可调
  * 在三种显示模式下都可选择并拷贝文字

下面是三种显示模式的截屏：

1. 纸张模式

<a href='http://www.flickr.com/photos/56129552@N06/5191642006/' title='liteview 纸张显示模式 by litebook.author, on Flickr'><img src='http://farm5.static.flickr.com/4154/5191642006_a1e7fedd28.jpg' alt='liteview 纸张显示模式' width='500' height='308' /></a>

2.书本模式

<a href='http://www.flickr.com/photos/56129552@N06/5191756398/' title='liteview 书本显示模式 by litebook.author, on Flickr'><img src='http://farm5.static.flickr.com/4110/5191756398_5729c35bb9.jpg' alt='liteview 书本显示模式' width='500' height='308' /></a>

3.竖排书本模式

<a href='http://www.flickr.com/photos/56129552@N06/5191180521/' title='liteview 竖排书本显示模式 by litebook.author, on Flickr'><img src='http://farm5.static.flickr.com/4091/5191180521_d8e68f18f3.jpg' alt='liteview 竖排书本显示模式' width='500' height='308' /></a>





liteview组件目前以完成第一个beta版，所有主要的功能都已实现，剩下的工作就是debug，然后再把liteview整合到litebook中，工作量不小...

大家多提意见。