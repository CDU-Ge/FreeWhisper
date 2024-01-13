# FreeWhisper

让每个人享受到科技的发展

## 开发者指南

### 环境准备

> only for Windows

1. install whisper

```powershell
# intall whisper.
pip install -U openai-whisper
# install whisper(no dependencies) in project.
pip install -U --no-dependencies -t . openai-whisper
```

其他实现

```powershell
pip install faster-whisper
```

## 模块设计

### pip 自动安装

### FreeWhisper

- 模型索引模块
- 语言选择与处理模块
- 简繁转换模块
- 复制与粘贴
- 音频文件选择模块
- 进度信息处理
- 日志记录
- 线程监控
- 断句分割模块

### UI Designer

#### Widgets

- w_main_copy
- w_main_paste

- w_main_result

- w_control_start
- w_control_stop

#### 输入区域

音频文件

- w_input_file
- w_input_select

- w_models_model
- w_lang_lang

- w_zh_convert
- w_zh_method

## 开发者日志

在Alpha版本中，我使用`openai`原本的库作为软件运行的后端，但是该效果似乎并不是十分友好。
在`hugging face`中，有许多其他开发者训练的模型，这些模型为许多语言带来了便利。用户也可以从中获取期望的模型。
我应该试着将这些加入其中。

原本`openai`的库应当作为基础库来运行！
我应当设置一个较为通用的接口。
