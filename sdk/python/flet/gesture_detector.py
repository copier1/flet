import json
from enum import Enum
from typing import Any, Optional, Union

from beartype import beartype

from flet.constrained_control import ConstrainedControl
from flet.control import Control, OptionalNumber
from flet.control_event import ControlEvent
from flet.event_handler import EventHandler
from flet.ref import Ref
from flet.types import AnimationValue, OffsetValue, RotateValue, ScaleValue


class MouseCursor(Enum):
    ALIAS = "alias"
    ALL_SCROLL = "allScroll"
    BASIC = "basic"
    CELL = "cell"
    CLICK = "click"
    CONTEXT_MENU = "contextMenu"
    COPY = "copy"
    DISAPPEARING = "disappearing"
    FORBIDDEN = "forbidden"
    GRAB = "grab"
    GRABBING = "grabbing"
    HELP = "help"
    MOVE = "move"
    NO_DROP = "noDrop"
    NONE = "none"
    PRECISE = "precise"
    PROGRESS = "progress"
    RESIZE_COLUMN = "ResizeColumn"
    RESIZE_DOWN = "ResizeDown"
    RESIZE_DOWN_LEFT = "ResizeDownLeft"
    RESIZE_DOWN_RIGHT = "ResizeDownRight"
    RESIZE_LEFT = "ResizeLeft"
    RESIZE_LEFT_RIGHT = "ResizeLeftRight"
    RESIZE_RIGHT = "ResizeRight"
    RESIZE_ROW = "ResizeRow"
    RESIZE_UP = "ResizeUp"
    RESIZE_UP_DOWN = "ResizeUpDown"
    RESIZE_UP_LEFT = "ResizeUpLeft"
    RESIZE_UP_LEFT_DOWN_RIGHT = "ResizeUpLeftDownRight"
    RESIZE_UP_RIGHT = "ResizeUpRight"
    RESIZE_UP_RIGHT_DOWN_LEFT = "ResizeUpRightDownLeft"
    TEXT = "text"
    VERTICAL_TEXT = "verticalText"
    WAIT = "wait"
    ZOOM_IN = "zoomIn"
    ZOOM_OUT = "zoomOut"


class GestureDetector(ConstrainedControl):
    def __init__(
        self,
        content: Optional[Control] = None,
        ref: Optional[Ref] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        #
        # Specific
        #
        mouse_cursor: Optional[MouseCursor] = None,
        drag_interval: Optional[int] = None,
        hover_interval: Optional[int] = None,
        on_tap=None,
        on_tap_down=None,
        on_tap_up=None,
        on_secondary_tap=None,
        on_secondary_tap_down=None,
        on_secondary_tap_up=None,
        on_long_press_start=None,
        on_long_press_end=None,
        on_secondary_long_press_start=None,
        on_secondary_long_press_end=None,
        on_double_tap=None,
        on_double_tap_down=None,
        on_horizontal_drag_start=None,
        on_horizontal_drag_update=None,
        on_horizontal_drag_end=None,
        on_vertical_drag_start=None,
        on_vertical_drag_update=None,
        on_vertical_drag_end=None,
        on_pan_start=None,
        on_pan_update=None,
        on_pan_end=None,
        on_scale_start=None,
        on_scale_update=None,
        on_scale_end=None,
        on_hover=None,
        on_enter=None,
        on_exit=None,
    ):

        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.__on_tap_down = EventHandler(lambda e: TapEvent(**json.loads(e.data)))
        self._add_event_handler("tap_down", self.__on_tap_down.handler)

        self.__on_tap_up = EventHandler(lambda e: TapEvent(**json.loads(e.data)))
        self._add_event_handler("tap_up", self.__on_tap_up.handler)

        self.__on_secondary_tap_down = EventHandler(
            lambda e: TapEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "secondary_tap_down", self.__on_secondary_tap_down.handler
        )

        self.__on_secondary_tap_up = EventHandler(
            lambda e: TapEvent(**json.loads(e.data))
        )
        self._add_event_handler("secondary_tap_up", self.__on_secondary_tap_up.handler)

        self.__on_long_press_start = EventHandler(
            lambda e: LongPressStartEvent(**json.loads(e.data))
        )
        self._add_event_handler("long_press_start", self.__on_long_press_start.handler)

        self.__on_long_press_end = EventHandler(
            lambda e: LongPressEndEvent(**json.loads(e.data))
        )
        self._add_event_handler("long_press_end", self.__on_long_press_end.handler)

        self.__on_secondary_long_press_start = EventHandler(
            lambda e: LongPressStartEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "secondary_long_press_start", self.__on_secondary_long_press_start.handler
        )

        self.__on_secondary_long_press_end = EventHandler(
            lambda e: LongPressEndEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "secondary_long_press_end", self.__on_secondary_long_press_end.handler
        )
        self.__on_double_tap_down = EventHandler(
            lambda e: TapEvent(**json.loads(e.data))
        )
        self._add_event_handler("double_tap_down", self.__on_double_tap_down.handler)

        # on_horizontal_drag

        self.__on_horizontal_drag_start = EventHandler(
            lambda e: DragStartEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "horizontal_drag_start", self.__on_horizontal_drag_start.handler
        )
        self.__on_horizontal_drag_update = EventHandler(
            lambda e: DragUpdateEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "horizontal_drag_update", self.__on_horizontal_drag_update.handler
        )
        self.__on_horizontal_drag_end = EventHandler(
            lambda e: DragEndEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "horizontal_drag_end", self.__on_horizontal_drag_end.handler
        )

        # on_vertical_drag

        self.__on_vertical_drag_start = EventHandler(
            lambda e: DragStartEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "vertical_drag_start", self.__on_vertical_drag_start.handler
        )
        self.__on_vertical_drag_update = EventHandler(
            lambda e: DragUpdateEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "vertical_drag_update", self.__on_vertical_drag_update.handler
        )
        self.__on_vertical_drag_end = EventHandler(
            lambda e: DragEndEvent(**json.loads(e.data))
        )
        self._add_event_handler(
            "vertical_drag_end", self.__on_vertical_drag_end.handler
        )

        # on_pan

        self.__on_pan_start = EventHandler(
            lambda e: DragStartEvent(**json.loads(e.data))
        )
        self._add_event_handler("pan_start", self.__on_pan_start.handler)
        self.__on_pan_update = EventHandler(
            lambda e: DragUpdateEvent(**json.loads(e.data))
        )
        self._add_event_handler("pan_update", self.__on_pan_update.handler)
        self.__on_pan_end = EventHandler(lambda e: DragEndEvent(**json.loads(e.data)))
        self._add_event_handler("pan_end", self.__on_pan_end.handler)

        # on_scale

        self.__on_scale_start = EventHandler(
            lambda e: ScaleStartEvent(**json.loads(e.data))
        )
        self._add_event_handler("scale_start", self.__on_scale_start.handler)
        self.__on_scale_update = EventHandler(
            lambda e: ScaleUpdateEvent(**json.loads(e.data))
        )
        self._add_event_handler("scale_update", self.__on_scale_update.handler)
        self.__on_scale_end = EventHandler(
            lambda e: ScaleEndEvent(**json.loads(e.data))
        )
        self._add_event_handler("scale_end", self.__on_scale_end.handler)

        # on_hover

        self.__on_hover = EventHandler(lambda e: HoverEvent(**json.loads(e.data)))
        self._add_event_handler("hover", self.__on_hover.handler)
        self.__on_enter = EventHandler(lambda e: HoverEvent(**json.loads(e.data)))
        self._add_event_handler("enter", self.__on_enter.handler)
        self.__on_exit = EventHandler(lambda e: HoverEvent(**json.loads(e.data)))
        self._add_event_handler("exit", self.__on_exit.handler)

        self.content = content
        self.mouse_cursor = mouse_cursor
        self.drag_interval = drag_interval
        self.hover_interval = hover_interval
        self.on_tap = on_tap
        self.on_tap_down = on_tap_down
        self.on_tap_up = on_tap_up
        self.on_secondary_tap = on_secondary_tap
        self.on_secondary_tap_down = on_secondary_tap_down
        self.on_secondary_tap_up = on_secondary_tap_up
        self.on_long_press_start = on_long_press_start
        self.on_long_press_end = on_long_press_end
        self.on_secondary_long_press_start = on_secondary_long_press_start
        self.on_secondary_long_press_end = on_secondary_long_press_end
        self.on_double_tap = on_double_tap
        self.on_double_tap_down = on_double_tap_down
        self.on_horizontal_drag_start = on_horizontal_drag_start
        self.on_horizontal_drag_update = on_horizontal_drag_update
        self.on_horizontal_drag_end = on_horizontal_drag_end
        self.on_vertical_drag_start = on_vertical_drag_start
        self.on_vertical_drag_update = on_vertical_drag_update
        self.on_vertical_drag_end = on_vertical_drag_end
        self.on_pan_start = on_pan_start
        self.on_pan_update = on_pan_update
        self.on_pan_end = on_pan_end
        self.on_scale_start = on_scale_start
        self.on_scale_update = on_scale_update
        self.on_scale_end = on_scale_end
        self.on_hover = on_hover
        self.on_enter = on_enter
        self.on_exit = on_exit

    def _get_control_name(self):
        return "gesturedetector"

    def _get_children(self):
        children = []
        if self.__content:
            self.__content._set_attr_internal("n", "content")
            children.append(self.__content)
        return children

    # content
    @property
    def content(self) -> Optional[Control]:
        return self.__content

    @content.setter
    @beartype
    def content(self, value: Optional[Control]):
        self.__content = value

    # mouse_cursor
    @property
    def mouse_cursor(self):
        return self._get_attr("mouseCursor")

    @mouse_cursor.setter
    @beartype
    def mouse_cursor(self, value: Optional[MouseCursor]):
        self._set_attr("mouseCursor", value.value if value is not None else None)

    # drag_interval
    @property
    def drag_interval(self) -> Optional[int]:
        return self._get_attr("dragInterval")

    @drag_interval.setter
    @beartype
    def drag_interval(self, value: Optional[int]):
        self._set_attr("dragInterval", value)

    # hover_interval
    @property
    def hover_interval(self) -> Optional[int]:
        return self._get_attr("hoverInterval")

    @hover_interval.setter
    @beartype
    def hover_interval(self, value: Optional[int]):
        self._set_attr("hoverInterval", value)

    # on_tap
    @property
    def on_tap(self):
        return self._get_event_handler("tap")

    @on_tap.setter
    def on_tap(self, handler):
        self._add_event_handler("tap", handler)
        self._set_attr("onTap", True if handler is not None else None)

    # on_tap_down
    @property
    def on_tap_down(self):
        return self.__on_tap_down

    @on_tap_down.setter
    def on_tap_down(self, handler):
        self.__on_tap_down.subscribe(handler)
        self._set_attr("onTapDown", True if handler is not None else None)

    # on_tap_up
    @property
    def on_tap_up(self):
        return self.__on_tap_up

    @on_tap_up.setter
    def on_tap_up(self, handler):
        self.__on_tap_up.subscribe(handler)
        self._set_attr("onTapUp", True if handler is not None else None)

    # on_secondary_tap
    @property
    def on_secondary_tap(self):
        return self._get_event_handler("secondary_tap")

    @on_secondary_tap.setter
    def on_secondary_tap(self, handler):
        self._add_event_handler("secondary_tap", handler)
        self._set_attr("onSecondaryTap", True if handler is not None else None)

    # on_tap_down
    @property
    def on_secondary_tap_down(self):
        return self.__on_secondary_tap_down

    @on_secondary_tap_down.setter
    def on_secondary_tap_down(self, handler):
        self.__on_secondary_tap_down.subscribe(handler)
        self._set_attr("onSecondaryTapDown", True if handler is not None else None)

    # on_secondary_tap_up
    @property
    def on_secondary_tap_up(self):
        return self.__on_secondary_tap_up

    @on_secondary_tap_up.setter
    def on_secondary_tap_up(self, handler):
        self.__on_secondary_tap_up.subscribe(handler)
        self._set_attr("onSecondaryTapUp", True if handler is not None else None)

    # on_long_press_start
    @property
    def on_long_press_start(self):
        return self.__on_long_press_start

    @on_long_press_start.setter
    def on_long_press_start(self, handler):
        self.__on_long_press_start.subscribe(handler)
        self._set_attr("onLongPressStart", True if handler is not None else None)

    # on_long_press_end
    @property
    def on_long_press_end(self):
        return self.__on_long_press_end

    @on_long_press_end.setter
    def on_long_press_end(self, handler):
        self.__on_long_press_end.subscribe(handler)
        self._set_attr("onLongPressEnd", True if handler is not None else None)

    # on_secondary_long_press_start
    @property
    def on_secondary_long_press_start(self):
        return self.__on_secondary_long_press_start

    @on_secondary_long_press_start.setter
    def on_secondary_long_press_start(self, handler):
        self.__on_secondary_long_press_start.subscribe(handler)
        self._set_attr(
            "onSecondaryLongPressStart", True if handler is not None else None
        )

    # on_secondary_long_press_end
    @property
    def on_secondary_long_press_end(self):
        return self.__on_secondary_long_press_end

    @on_secondary_long_press_end.setter
    def on_secondary_long_press_end(self, handler):
        self.__on_secondary_long_press_end.subscribe(handler)
        self._set_attr("onSecondaryLongPressEnd", True if handler is not None else None)

    # on_double_tap
    @property
    def on_double_tap(self):
        return self._get_event_handler("double_tap")

    @on_double_tap.setter
    def on_double_tap(self, handler):
        self._add_event_handler("double_tap", handler)
        self._set_attr("onDoubleTap", True if handler is not None else None)

    # on_double_tap_down
    @property
    def on_double_tap_down(self):
        return self.__on_double_tap_down

    @on_double_tap_down.setter
    def on_double_tap_down(self, handler):
        self.__on_double_tap_down.subscribe(handler)
        self._set_attr("onDoubleTapDown", True if handler is not None else None)

    # on_horizontal_drag_start
    @property
    def on_horizontal_drag_start(self):
        return self.__on_horizontal_drag_start

    @on_horizontal_drag_start.setter
    def on_horizontal_drag_start(self, handler):
        self.__on_horizontal_drag_start.subscribe(handler)
        self._set_attr("onHorizontalDragStart", True if handler is not None else None)

    # on_horizontal_drag_update
    @property
    def on_horizontal_drag_update(self):
        return self.__on_horizontal_drag_update

    @on_horizontal_drag_update.setter
    def on_horizontal_drag_update(self, handler):
        self.__on_horizontal_drag_update.subscribe(handler)
        self._set_attr("onHorizontalDragUpdate", True if handler is not None else None)

    # on_horizontal_drag_end
    @property
    def on_horizontal_drag_end(self):
        return self.__on_horizontal_drag_end

    @on_horizontal_drag_end.setter
    def on_horizontal_drag_end(self, handler):
        self.__on_horizontal_drag_end.subscribe(handler)
        self._set_attr("onHorizontalDragEnd", True if handler is not None else None)

    # on_vertical_drag_start
    @property
    def on_vertical_drag_start(self):
        return self.__on_vertical_drag_start

    @on_vertical_drag_start.setter
    def on_vertical_drag_start(self, handler):
        self.__on_vertical_drag_start.subscribe(handler)
        self._set_attr("onVerticalDragStart", True if handler is not None else None)

    # on_vertical_drag_update
    @property
    def on_vertical_drag_update(self):
        return self.__on_vertical_drag_update

    @on_vertical_drag_update.setter
    def on_vertical_drag_update(self, handler):
        self.__on_vertical_drag_update.subscribe(handler)
        self._set_attr("onVerticalDragUpdate", True if handler is not None else None)

    # on_vertical_drag_end
    @property
    def on_vertical_drag_end(self):
        return self.__on_vertical_drag_end

    @on_vertical_drag_end.setter
    def on_vertical_drag_end(self, handler):
        self.__on_vertical_drag_end.subscribe(handler)
        self._set_attr("onVerticalDragEnd", True if handler is not None else None)

    # on_pan_start
    @property
    def on_pan_start(self):
        return self.__on_pan_start

    @on_pan_start.setter
    def on_pan_start(self, handler):
        self.__on_pan_start.subscribe(handler)
        self._set_attr("onPanStart", True if handler is not None else None)

    # on_pan_updatevertical_drag
    @property
    def on_pan_update(self):
        return self.__on_pan_update

    @on_pan_update.setter
    def on_pan_update(self, handler):
        self.__on_pan_update.subscribe(handler)
        self._set_attr("onPanUpdate", True if handler is not None else None)

    # on_pan_end
    @property
    def on_pan_end(self):
        return self.__on_pan_end

    @on_pan_end.setter
    def on_pan_end(self, handler):
        self.__on_pan_end.subscribe(handler)
        self._set_attr("onPanEnd", True if handler is not None else None)

    # on_scale_start
    @property
    def on_scale_start(self):
        return self.__on_scale_start

    @on_scale_start.setter
    def on_scale_start(self, handler):
        self.__on_scale_start.subscribe(handler)
        self._set_attr("onScaleStart", True if handler is not None else None)

    # on_scale_update
    @property
    def on_scale_update(self):
        return self.__on_scale_update

    @on_scale_update.setter
    def on_scale_update(self, handler):
        self.__on_scale_update.subscribe(handler)
        self._set_attr("onScaleUpdate", True if handler is not None else None)

    # on_scale_end
    @property
    def on_scale_end(self):
        return self.__on_scale_end

    @on_scale_end.setter
    def on_scale_end(self, handler):
        self.__on_scale_end.subscribe(handler)
        self._set_attr("onScaleEnd", True if handler is not None else None)

    # on_hover
    @property
    def on_hover(self):
        return self.__on_hover

    @on_hover.setter
    def on_hover(self, handler):
        self.__on_hover.subscribe(handler)
        self._set_attr("onHover", True if handler is not None else None)

    # on_enter
    @property
    def on_enter(self):
        return self.__on_enter

    @on_enter.setter
    def on_enter(self, handler):
        self.__on_enter.subscribe(handler)
        self._set_attr("onEnter", True if handler is not None else None)

    # on_exit
    @property
    def on_exit(self):
        return self.__on_exit

    @on_exit.setter
    def on_exit(self, handler):
        self.__on_exit.subscribe(handler)
        self._set_attr("onExit", True if handler is not None else None)


class TapEvent(ControlEvent):
    def __init__(self, lx, ly, gx, gy, kind) -> None:
        self.local_x: float = lx
        self.local_y: float = ly
        self.global_x: float = gx
        self.global_y: float = gy
        self.kind: str = kind


class LongPressStartEvent(ControlEvent):
    def __init__(self, lx, ly, gx, gy) -> None:
        self.local_x: float = lx
        self.local_y: float = ly
        self.global_x: float = gx
        self.global_y: float = gy


class LongPressEndEvent(ControlEvent):
    def __init__(self, lx, ly, gx, gy, vx, vy) -> None:
        self.local_x: float = lx
        self.local_y: float = ly
        self.global_x: float = gx
        self.global_y: float = gy
        self.velocity_x: float = vx
        self.velocity_y: float = vy


class DragStartEvent(ControlEvent):
    def __init__(self, lx, ly, gx, gy, kind, ts) -> None:
        self.kind: str = kind
        self.local_x: float = lx
        self.local_y: float = ly
        self.global_x: float = gx
        self.global_y: float = gy
        self.timestamp: Optional[int] = ts


class DragUpdateEvent(ControlEvent):
    def __init__(self, dx, dy, pd, lx, ly, gx, gy, ts) -> None:
        self.delta_x: float = dx
        self.delta_y: float = dy
        self.primary_delta: Optional[float] = pd
        self.local_x: float = lx
        self.local_y: float = ly
        self.global_x: float = gx
        self.global_y: float = gy
        self.timestamp: Optional[int] = ts


class DragEndEvent(ControlEvent):
    def __init__(self, pv, vx, vy) -> None:
        self.primary_velocity: Optional[float] = pv
        self.velocity_x: float = vx
        self.velocity_y: float = vy


class ScaleStartEvent(ControlEvent):
    def __init__(self, fpx, fpy, lfpx, lfpy, pc) -> None:
        self.focal_point_x: float = fpx
        self.focal_point_y: float = fpy
        self.local_focal_point_x: float = lfpx
        self.local_focal_point_y: float = lfpy
        self.pointer_count: int = pc


class ScaleUpdateEvent(ControlEvent):
    def __init__(self, fpx, fpy, fpdx, fpdy, lfpx, lfpy, pc, hs, vs, s, r) -> None:
        self.focal_point_x: float = fpx
        self.focal_point_y: float = fpy
        self.focal_point_delta_x: float = fpdx
        self.focal_point_delta_y: float = fpdy
        self.local_focal_point_x: float = lfpx
        self.local_focal_point_y: float = lfpy
        self.pointer_count: int = pc
        self.horizontal_scale: float = hs
        self.vertical_scale: float = vs
        self.scale: float = s
        self.rotation: float = r


class ScaleEndEvent(ControlEvent):
    def __init__(self, pc, vx, vy) -> None:
        self.pointer_count: int = pc
        self.velocity_x: float = vx
        self.velocity_y: float = vy


class HoverEvent(ControlEvent):
    def __init__(self, ts, kind, gx, gy, lx, ly, dx=None, dy=None) -> None:
        self.timestamp: float = ts
        self.kind: str = kind
        self.global_x: float = gx
        self.global_y: float = gy
        self.local_x: float = lx
        self.local_y: float = ly
        self.delta_x: Optional[float] = dx
        self.delta_y: Optional[float] = dy
