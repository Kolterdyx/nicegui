from typing import Any, Callable, Optional

from .. import globals  # pylint: disable=redefined-builtin
from ..element import Element
from ..events import ClickEventArguments, handle_event
from .mixins.text_element import TextElement
from .mixins.value_element import ValueElement


class Menu(ValueElement):

    def __init__(self, *, value: bool = False) -> None:
        """Menu

        Creates a menu based on Quasar's `QMenu <https://quasar.dev/vue-components/menu>`_ component.
        The menu should be placed inside the element where it should be shown.

        :param value: whether the menu is already opened (default: `False`)
        """
        super().__init__(tag='q-menu', value=value, on_value_change=None)

    def open(self) -> None:
        """Open the menu."""
        self.value = True

    def close(self) -> None:
        """Close the menu."""
        self.value = False

    def toggle(self) -> None:
        """Toggle the menu."""
        self.value = not self.value


class ContextMenu(Element):

    def __init__(self) -> None:
        """Context Menu

        Creates a context menu based on Quasar's `QMenu <https://quasar.dev/vue-components/menu>`_ component.
        The context menu should be placed inside the element where it should be shown.
        It is automatically opened when the user right-clicks on the element and appears at the mouse position.
        """
        super().__init__('q-menu')
        self._props['context-menu'] = True
        self._props['touch-position'] = True


class MenuItem(TextElement):

    def __init__(self,
                 text: str = '',
                 on_click: Optional[Callable[..., Any]] = None, *,
                 auto_close: bool = True,
                 ) -> None:
        """Menu Item

        A menu item to be added to a menu.
        This element is based on Quasar's `QItem <https://quasar.dev/vue-components/list-and-list-items#qitem-api>`_ component.

        :param text: label of the menu item
        :param on_click: callback to be executed when selecting the menu item
        :param auto_close: whether the menu should be closed after a click event (default: `True`)
        """
        super().__init__(tag='q-item', text=text)
        self.menu = globals.get_slot().parent
        self._props['clickable'] = True

        def handle_click(_) -> None:
            handle_event(on_click, ClickEventArguments(sender=self, client=self.client))
            if auto_close:
                assert isinstance(self.menu, Menu)
                self.menu.close()
        self.on('click', handle_click, [])
