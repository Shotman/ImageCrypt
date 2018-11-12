import base64
import sys
from ImageCrypt.data.base import BaseData
from ImageCrypt.data.encrypt.binary import EncodeBinaryData


class EncodeFileData(BaseData):

    def __init__(self, path):
        super(EncodeFileData, self).__init__(
            path
        )
        with open(path, "rb") as f:
            self._data = base64.b64encode(f.read())
        self.binary = EncodeBinaryData(
            self._data,
        )

    @property
    def data(self):
        return self._data

    def validate(self, size, sp, ep):
        self._logger.info("Validating if data will fit into image.")
        available_space = (size[0] * size[1] * 3)
        if available_space < len(self.binary.bytes):
            self._logger.error(
                "This image can only store {0:d} bytes of data. "
                "Your message is {1:d} bytes".format(
                    available_space,
                    len(self.binary.bytes),
                )
            )
            sys.exit(1)
