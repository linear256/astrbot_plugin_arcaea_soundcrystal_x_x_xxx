from pickle import FALSE

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.event import filter, AstrMessageEvent

@register("X_X_XXX", "linear256", "Only feels like nothing could be better when I'm with you...", "1.0.0")
class XterPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    """
    X X XXX | O O OOO
    XX X XXX | OO O OOO
    X X X XXXX | O O O OOOO
    XX XX XXX XX | OO OO OOO OO
    XXX | OOO
    XXX X | OOO O
    XXX XXX | OOO OOO
    XXXXX | OOOOO
    XXXXXXX | OOOOOOO
    XXX XX | OOO OO
    XX | OO
    XX | OO
    XX | OO
    XX | OO
    X | O
    X | O
    X | O
    X | O
    X | O
    X | O
    X | O
    X | O
    X | O
    X | O
    """

    list = ['X X XXX','XX X XXX','X X X XXXX','XX XX XXX XX','XXX','XXX X','XXX XXX','XXXXX','XXXXXXX','XXX XX','XX','XX','XX','XX','X','X','X','X','X','X','X','X','X','X']
    bot_start = 0 #是否由bot开始X X XXX，bool值，0=False 1=True

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @filter.event_message_type(filter.EventMessageType.ALL)
    async def spawn_soundcrystal(self, event: AstrMessageEvent, *args, **kwargs):
        """
        处理消息，检查是否包含配置的关键词。

        Args:
            event: 消息事件
            **kwargs: AstrBot 框架传入的额外参数
        """
        # 获取消息文本内容
        message_text = event.message_str
        if not message_text:
            return

        try:
            # 立即阻止默认 LLM 请求
            # 注意：在 AstrBot 中，调用前会检查 'if not event.call_llm'
            # 所以设置 call_llm=True 实际上是阻止默认 LLM 被调用
            event.should_call_llm(True)


        except Exception as e:
            logger.exception("音晶插件发生错误")
            try:
                yield event.plain_result("哎呀，出错了...")
                event.stop_event()
            except Exception as inner_e:
                # 区分原始异常和发送失败异常
                logger.error(f"发送错误消息失败: {inner_e}")
                # 检测可能的系统性错误（事件系统故障等）
                error_msg = str(inner_e).lower()
                if any(kw in error_msg for kw in ["event", "yield", "generator", "async"]):
                    logger.critical(f"事件系统错误: {inner_e}")

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
