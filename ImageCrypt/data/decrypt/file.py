import base64
from ImageCrypt.data.base import BaseData
from ImageCrypt.data.decrypt.binary import DecodeBinaryData


class DecodeFileData(BaseData):

    def __init__(self, path):
        super(DecodeFileData, self).__init__(
            path
        )
        self.binary = DecodeBinaryData()

    @property
    def data(self):
        if self._data is None:
            self._data = base64.b64decode(self.binary.string)
        return self._data

    def validate(self, size, sp, ep):
        pass

    def save(self):
        self._logger.info(
            "Saving saving decrypted data under path: {0:s}".format(self._path)
        )
        with open(self._path, "w+") as f:
            f.write(self.data)
