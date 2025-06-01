from __future__ import annotations

import asyncio
import socket
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from core import UvicornServer


class InterruptHandler:
    def __init__(
        self, server: UvicornServer, sockets: Optional[list[socket.socket]] = None
    ):
        self.server = server
        self.sockets = sockets
        self._task: Optional[asyncio.Task] = None

    def __call__(self):
        if self._task:
            raise KeyboardInterrupt

        self._task = self.server.loop.create_task(
            self.server.shutdown(sockets=self.sockets)
        )
