import os
import queue
import PySimpleGUI as sg
import locale

sg.user_settings_filename(path='.')

langcode, _ = locale.getdefaultlocale()
defaulelang = "zh"
if langcode.split('_')[0].lower() != 'zh':
    defaulelang = "en"

defaulelang="en"
translist = {
    "zh": {
        "proxyerrortitle": "代理错误",
        "proxyerrorbody": "无法访问google服务，请正确设置代理",
        "softname": "视频字幕翻译和配音",
        "anerror": "出错了",
        "selectvideodir": "必须选择要翻译的视频",
        "sourenotequaltarget": "源语言和目标语言不得相同",
        "running": "执行中",
        "exit": "退出"
    },
    "en": {
        "proxyerrortitle": "Proxy Error",
        "proxyerrorbody": "Failed to access Google services. Please set up the proxy correctly.",
        "softname": "Video Subtitle Translation and Dubbing",
        "anerror": "An error occurred",
        "selectvideodir": "You must select the video to be translated",
        "sourenotequaltarget": "Source language and target language must not be the same",
        "running": "Running",
        "exit": "Exit"
    }
}
transobj = translist['zh']
langlist = {
    "中文简": ['zh-cn', 'chi'],
    "中文繁": ['zh-tw', 'chi'],
    "英语": ['en', 'eng'],
    "法语": ['fr', 'fre'],
    "德语": ['de', 'ger'],
    "日语": ['ja', 'jpn'],
    "韩语": ['ko', 'kor'],
    "俄语": ['ru', 'rus'],
    "西班牙语": ['es', 'spa'],
    "泰国语": ['th', 'tha'],
    "意大利语": ['it', 'ita'],
    "葡萄牙语": ['pt', 'por'],
    "越南语": ['vi', 'vie'],
    "阿拉伯语": ['ar', 'are']
}
layout = [
    [
        sg.Column(
            [
                [sg.Text('原始视频目录', background_color="#e3f2fd", text_color='#212121'), sg.InputText(key="source_dir"),
                 sg.Button('选择待翻译视频', key="getsource_dir", enable_events=True, button_color='#018fff', border_width=0)],
                [sg.Text('输出视频位置', background_color="#e3f2fd", text_color='#212121'),
                 sg.InputText(key="target_dir"),
                 sg.Button('选择输出文件夹', key="gettarget_dir", enable_events=True, button_color='#018fff', border_width=0)],
                [sg.Text('网络代理地址', tooltip="类似 http://127.0.0.1:10809", background_color="#e3f2fd",
                         text_color='#212121'),
                 sg.InputText(sg.user_settings_get_entry('proxy', ''), key="proxy",
                              tooltip="类似 http://127.0.0.1:10809 的形式")
                 ],
                [
                    sg.Text('如果你不能直接打开google，需在上方填写代理地址', background_color="#e3f2fd",
                            text_color='#777777'),
                ],
                [
                    sg.Text('视频原始语言', background_color="#e3f2fd", text_color='#212121'),
                    sg.Combo(list(langlist.keys()), default_value=sg.user_settings_get_entry('source_lang', '英语'),
                             readonly=True, key="source_lang", size=(10, None)),
                    sg.Text('翻译目标语言', background_color="#e3f2fd", text_color='#212121'),
                    sg.Combo(list(langlist.keys()), default_value=sg.user_settings_get_entry('target_lang', '中文简'),
                             readonly=True, key="target_lang", size=(10, None),
                             enable_events=True
                             ),
                    sg.Text('选择配音', background_color="#e3f2fd", text_color='#212121'),
                    sg.Combo(['None'], default_value="None", readonly=True, key="voice_replace", size=(18, None)),
                ],
                [
                    sg.Text('配音语速', tooltip="-50-->+50", background_color="#e3f2fd",
                            text_color='#212121'),
                    sg.InputText(sg.user_settings_get_entry('voice_rate', '+10'), key="voice_rate", size=(8, None),
                                 tooltip="-10 -- +90,代表减慢或加速"),
                    sg.Text('-10到+90，负数代表降速，正数代表加速', background_color="#e3f2fd",
                            text_color='#777777'),
                ],
                [
                    sg.Text('保留字幕文件', background_color="#e3f2fd", text_color='#212121'),
                    sg.Combo(['Yes', 'No'], tooltip="如果保留，下次同一视频切换字幕语种不生效，需要手动删除",
                             default_value=sg.user_settings_get_entry('savesubtitle', '保留'), readonly=True,
                             key="savesubtitle", size=(10, None)),
                    sg.Text('并发翻译数量', background_color="#e3f2fd", text_color='#212121'),
                    sg.InputText(sg.user_settings_get_entry('concurrent', 2), key="concurrent",
                                 tooltip="1-20(cpu的整数倍)", size=(10, 1)),
                    sg.Text('即同时翻译的视频数量，建议为2-cpu的整数倍', background_color="#e3f2fd",
                            text_color='#777777'),
                ],
                [
                    sg.Button('开始执行', key="startbtn", button_color='#2196f3', size=(16, 2), font=16),
                ],
                [
                    sg.Multiline('', key="logs", expand_x=True, expand_y=True, size=(50, 8), autoscroll=True,
                                 background_color="#f1f1f1", text_color='#212121'),
                ]
            ],
            background_color="#e3f2fd",
            expand_x=True,
            expand_y=True,
            size=(640, None)
        ),
        sg.Column(
            [
                [
                    sg.Text("进度显示区", background_color="#e3f2fd", text_color='#212121'),
                ],
                [
                    sg.Column([[]],
                              key="add_row",
                              background_color="#e3f2fd",
                              size=(None, 400),
                              expand_y=True,
                              expand_x=True,
                              scrollable=True,
                              # justification="top",
                              vertical_alignment="top",
                              vertical_scroll_only=True
                              )
                ],
            ],
            # key="add_row",
            background_color="#e3f2fd",
            size=(None, None),
            expand_y=True,
            expand_x=True,
            scrollable=False,
            vertical_scroll_only=True
        )
    ]
]
if defaulelang == "en":
    transobj = translist['en']
    langlist = {
        "Simplified_Chinese": ['zh-cn', 'chi'],
        "Traditional_Chinese": ['zh-tw', 'chi'],
        "English": ['en', 'eng'],
        "French": ['fr', 'fre'],
        "German": ['de', 'ger'],
        "Japanese": ['ja', 'jpn'],
        "Korean": ['ko', 'kor'],
        "Russian": ['ru', 'rus'],
        "Spanish": ['es', 'spa'],
        "Thai": ['th', 'tha'],
        "Italian": ['it', 'ita'],
        "Portuguese": ['pt', 'por'],
        "Vietnamese": ['vi', 'vie'],
        "Arabic": ['ar', 'are']
    }

    layout = [
        [
            sg.Column(
                [
                    [sg.Text('Source Video Directory', background_color="#e3f2fd", text_color='#212121'),
                     sg.InputText(key="source_dir"),
                     sg.Button('Select Source Directory', key="getsource_dir", enable_events=True,
                               button_color='#018fff',
                               border_width=0)],
                    [sg.Text('Output Video Location', background_color="#e3f2fd", text_color='#212121'),
                     sg.InputText(key="target_dir"),
                     sg.Button('Select Target Directory', key="gettarget_dir", enable_events=True,
                               button_color='#018fff',
                               border_width=0)],
                    [sg.Text('Network Proxy', tooltip="e.g. http://127.0.0.1:10809", background_color="#e3f2fd",
                             text_color='#212121'),
                     sg.InputText(sg.user_settings_get_entry('proxy', ''), key="proxy",
                                  tooltip="e.g. http://127.0.0.1:10809")
                     ],
                    [
                        sg.Text('If you cannot access google directly, fill in the proxy address above.',
                                background_color="#e3f2fd",
                                text_color='#777777'),
                    ],
                    [
                        sg.Text('Source Language', background_color="#e3f2fd", text_color='#212121'),
                        sg.Combo(list(langlist.keys()),
                                 default_value=sg.user_settings_get_entry('source_lang', 'Simplified_Chinese'),
                                 readonly=True, key="source_lang", size=(10, None)),
                        sg.Text('Target Language', background_color="#e3f2fd", text_color='#212121'),
                        sg.Combo(list(langlist.keys()),
                                 default_value=sg.user_settings_get_entry('target_lang', 'English'),
                                 readonly=True, key="target_lang", size=(10, None),
                                 enable_events=True
                                 ),
                        sg.Text('Select Voice Replacement', background_color="#e3f2fd", text_color='#212121'),
                        sg.Combo(['None'], default_value="None", readonly=True, key="voice_replace", size=(18, None)),
                    ],
                    [
                        sg.Text('Voice Speed', tooltip="-50-->+50", background_color="#e3f2fd",
                                text_color='#212121'),
                        sg.InputText(sg.user_settings_get_entry('voice_rate', '+10'), key="voice_rate", size=(8, None),
                                     tooltip="-10 -- +90, represents slowing down or speeding up"),
                        sg.Text(
                            '-10 to +90, negative values represent slowing down, positive values represent speeding up',
                            background_color="#e3f2fd",
                            text_color='#777777'),
                    ],
                    [
                        sg.Text('Keep Subtitle Files', background_color="#e3f2fd", text_color='#212121'),
                        sg.Combo(['Yes', 'No'],
                                 tooltip="If 'Yes', changing subtitle language for the same video will not take effect until manually deleted.",
                                 default_value=sg.user_settings_get_entry('savesubtitle', 'Yes'), readonly=True,
                                 key="savesubtitle", size=(10, None)),
                        sg.Text('Concurrent Translation Count', background_color="#e3f2fd", text_color='#212121'),
                        sg.InputText(sg.user_settings_get_entry('concurrent', 2), key="concurrent",
                                     tooltip="1-20 (integer multiple of CPU)", size=(10, 1)),
                        sg.Text('i.e. Number of Videos Translated Simultaneously, suggest 2 - integer multiple of CPU',
                                background_color="#e3f2fd",
                                text_color='#777777'),
                    ],
                    [
                        sg.Button('Start Execution', key="startbtn", button_color='#2196f3', size=(16, 2), font=16),
                    ],
                    [
                        sg.Multiline('', key="logs", expand_x=True, expand_y=True, size=(50, 8), autoscroll=True,
                                     background_color="#f1f1f1", text_color='#212121'),
                    ]
                ],
                background_color="#e3f2fd",
                expand_x=True,
                expand_y=True,
                size=(640, None)
            ),
            sg.Column(
                [
                    [
                        sg.Text("Progress Display Area", background_color="#e3f2fd", text_color='#212121'),
                    ],
                    [
                        sg.Column([[]],
                                  key="add_row",
                                  background_color="#e3f2fd",
                                  size=(None, 400),
                                  expand_y=True,
                                  expand_x=True,
                                  scrollable=True,
                                  vertical_alignment="top",
                                  vertical_scroll_only=True
                                  )
                    ],
                ],
                background_color="#e3f2fd",
                size=(None, None),
                expand_y=True,
                expand_x=True,
                scrollable=False,
                vertical_scroll_only=True
            )
        ]
    ]

# 语言 三字母语言用于软嵌入字幕时 language=

# 当前执行目录
rootdir = os.getcwd()
# 添加环境变量 ffmpeg
os.environ['PATH'] = rootdir + ';' + os.environ['PATH']
# 日志队列
qu = queue.Queue(100)

# 存放所有视频名字键值对，值存放按钮上显示文字，完成后存放视频地址
videolist = {}
# 存放可使用的语音音色
voice_list = {}
# 存放每个视频处理的时间
timelist = {}
# 存放线程list
tc = []
# 开始按钮状态
current_status = "stop"
# 是否已执行过
ishastart = False
# 配置
video_config = {
    "target_dir": "",
    "source_dir": "",
    "detect_language": "en",
    "source_language": "en",
    "target_language": "zh-cn",
    "subtitle_language": "chi",
    "savesubtitle": "Yes",
    "voice_replace": "None",
    "voice_rate": "+10"
}
task_nums = [1, 1]
task_threads = []