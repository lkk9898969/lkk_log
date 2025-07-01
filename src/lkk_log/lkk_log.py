import logging
import warnings
from io import StringIO
from pathlib import Path

from types import TracebackType
from typing import Literal, Mapping
from typing_extensions import TypeAlias


_SysExcInfoType: TypeAlias = (
    tuple[type[BaseException], BaseException, TracebackType | None]
    | tuple[None, None, None]
)
_ExcInfoType: TypeAlias = None | bool | _SysExcInfoType | BaseException

loglevels = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

warnings.filterwarnings("default", category=DeprecationWarning)


class LkkLogger:
    def __init__(
        self,
        name: str,
        level: loglevels = "INFO",
        /,
        fileLevel: loglevels = ...,
        filename: str = ...,
        consoleAttach: bool = True,
        fileAttach: bool = True,
        cwd: str | Path = ".",
    ):
        level = matchlevel(level)
        if fileLevel is ...:
            fileLevel = level
        else:
            fileLevel = matchlevel(fileLevel)
        if filename is ...:
            filename = name
        filename = str(Path(cwd) / filename)

        self.name = name
        self.filename = filename
        self.consoleAttach = consoleAttach
        self.fileAttach = fileAttach
        self.level = level
        self.fileLevel = fileLevel
        self.__logger = logging.getLogger(self.name)
        self.__logger.setLevel(logging.DEBUG)
        self.__customInit()

    def __customInit(self):
        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s : %(message)s", datefmt="%Y/%m/%d %H:%M:%S"
        )
        self.__stream = StringIO()
        self.__stream_handler = logging.StreamHandler(self.__stream)
        self.__stream_handler.setLevel(logging.DEBUG)
        self.__stream_handler.setFormatter(formatter)
        self.__logger.addHandler(self.__stream_handler)
        if self.consoleAttach:
            consoleHandler = logging.StreamHandler()
            consoleHandler.setLevel(self.level)
            consoleHandler.setFormatter(formatter)
            self.__logger.addHandler(consoleHandler)
        if self.fileAttach:
            fileHandler = logging.FileHandler(self.filename + ".log", encoding="utf-8")
            fileHandler.setLevel(self.fileLevel)
            fileHandler.setFormatter(formatter)
            self.__logger.addHandler(fileHandler)

    def debug(
        self,
        msg: object,
        *args: object,
        exc_info: _ExcInfoType = None,
        stack_info=False,
        stacklevel=1,
        extra: Mapping[str, object] = None,
        console: bool = ...,
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.debug(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if console is True and self.consoleAttach is False:
            print(self.__stream.getvalue(), end="")

    def info(
        self,
        msg: object,
        *args: object,
        exc_info: _ExcInfoType = None,
        stack_info=False,
        stacklevel=1,
        extra: Mapping[str, object] = None,
        console: bool = ...,
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.info(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if console is True and self.consoleAttach is False:
            print(self.__stream.getvalue(), end="")

    def warning(
        self,
        msg: object,
        *args: object,
        exc_info: _ExcInfoType = None,
        stack_info=False,
        stacklevel=1,
        extra: Mapping[str, object] = None,
        console: bool = ...,
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.warning(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if console is True and self.consoleAttach is False:
            print(self.__stream.getvalue(), end="")

    def error(
        self,
        msg: object,
        *args: object,
        exc_info: _ExcInfoType = None,
        stack_info=False,
        stacklevel=1,
        extra: Mapping[str, object] = None,
        console: bool = ...,
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.error(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if console is True and self.consoleAttach is False:
            print(self.__stream.getvalue(), end="")

    def critical(
        self,
        msg: object,
        *args: object,
        exc_info: _ExcInfoType = None,
        stack_info=False,
        stacklevel=1,
        extra: Mapping[str, object] = None,
        console: bool = ...,
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.critical(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if console is True and self.consoleAttach is False:
            print(self.__stream.getvalue(), end="")

    def exception(
        self, msg, *args, exc_info=True, stack_info=False, stacklevel=1, extra=None
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.exception(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )

    def log(
        self,
        level,
        msg,
        *args,
        exc_info=None,
        stack_info=False,
        stacklevel=1,
        extra=None,
    ):
        self.__stream.seek(0)
        self.__stream.truncate(0)
        self.__logger.log(
            level,
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )


def loggerhandler(
    loggername: str,
    logfilename: str = ...,
    level: loglevels = "INFO",
    logfile_level: loglevels = ...,
    consoleattach: bool = True,
    logfileattach=True,
    cwd: str | Path = ".",
):
    warnings.warn(
        f"{loggerhandler.__name__} is deprecated, use LkkLogger instead.",
        DeprecationWarning,
    )
    level = matchlevel(level)
    if logfile_level is ...:
        logfile_level = level
    else:
        logfile_level = matchlevel(logfile_level)
    if logfilename is ...:
        logfilename = loggername
    logfilename = str(Path(cwd) / logfilename)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s : %(message)s", datefmt="%Y/%m/%d %H:%M:%S"
    )
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)
    if consoleattach:
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(level)
        consolehandler.setFormatter(formatter)
        logger.addHandler(consolehandler)
    if logfileattach:
        filehandler = logging.FileHandler(logfilename + ".log", encoding="utf-8")
        filehandler.setLevel(logfile_level)
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
    return logger


def matchlevel(_level: loglevels):
    if type(_level) is str:
        match _level.upper():
            case "DEBUG":
                level = logging.DEBUG
            case "INFO":
                level = logging.INFO
            case "WARNING":
                level = logging.WARNING
            case "ERROR":
                level = logging.ERROR
            case "CRITICAL":
                level = logging.CRITICAL
            case _:
                level = logging.INFO
    elif type(_level) is int:
        if any(
            _level == level
            for level in [
                logging.DEBUG,
                logging.INFO,
                logging.WARNING,
                logging.ERROR,
                logging.CRITICAL,
            ]
        ):
            level = _level
    else:
        level = logging.INFO
    return level
