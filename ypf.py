# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import zlib


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Ypf(KaitaiStruct):

    class FileType(Enum):
        text = 0
        png = 2
        wav = 5
        ogg = 6
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.ensure_fixed_contents(b"\x59\x50\x46\x00")
        self.engine_version = self._io.read_u4le()
        self.file_count = self._io.read_u4le()
        self.header_len = self._io.read_u4le()
        self.guard = self._io.ensure_fixed_contents(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

    class ObfsFname16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(16)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname54(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(54)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class Body(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._parent.compressed == 1:
                self._raw_cmprsd_body = self._io.read_bytes_full()
                self.cmprsd_body = zlib.decompress(self._raw_cmprsd_body)

            if self._parent.compressed == 0:
                self.body = self._io.read_bytes_full()



    class ObfsFname27(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(27)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname38(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(38)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname48(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(48)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname31(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(31)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname20(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(20)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname42(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(42)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname39(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(39)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(12)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname14(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(14)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname34(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(34)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname51(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(51)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname28(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(28)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname46(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(46)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname36(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(36)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname23(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(23)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname17(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(17)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname41(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(41)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname25(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(25)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname45(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(45)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname50(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(50)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname55(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(55)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname30(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(30)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname44(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(44)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname33(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(33)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname11(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(11)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname13(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(13)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname47(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(47)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname35(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(35)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname24(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(24)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname29(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(29)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname22(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(22)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname18(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(18)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname52(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(52)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname40(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(40)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(self._root.FileEntry(self._io, self, self._root))
                i += 1



    class ObfsFname53(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(53)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class FileEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown0 = self._io.read_u4le()
            self.filename_length_marker = self._io.read_u1()
            _on = self.filename_length_marker
            if _on == 236:
                self.filename = self._root.ObfsFname13(self._io, self, self._root)
            elif _on == 243:
                self.filename = self._root.ObfsFname16(self._io, self, self._root)
            elif _on == 239:
                self.filename = self._root.ObfsFname12(self._io, self, self._root)
            elif _on == 246:
                self.filename = self._root.ObfsFname11(self._io, self, self._root)
            elif _on == 219:
                self.filename = self._root.ObfsFname36(self._io, self, self._root)
            elif _on == 220:
                self.filename = self._root.ObfsFname32(self._io, self, self._root)
            elif _on == 214:
                self.filename = self._root.ObfsFname38(self._io, self, self._root)
            elif _on == 211:
                self.filename = self._root.ObfsFname47(self._io, self, self._root)
            elif _on == 224:
                self.filename = self._root.ObfsFname31(self._io, self, self._root)
            elif _on == 244:
                self.filename = self._root.ObfsFname9(self._io, self, self._root)
            elif _on == 230:
                self.filename = self._root.ObfsFname25(self._io, self, self._root)
            elif _on == 218:
                self.filename = self._root.ObfsFname37(self._io, self, self._root)
            elif _on == 249:
                self.filename = self._root.ObfsFname53(self._io, self, self._root)
            elif _on == 209:
                self.filename = self._root.ObfsFname20(self._io, self, self._root)
            elif _on == 233:
                self.filename = self._root.ObfsFname22(self._io, self, self._root)
            elif _on == 252:
                self.filename = self._root.ObfsFname10(self._io, self, self._root)
            elif _on == 234:
                self.filename = self._root.ObfsFname27(self._io, self, self._root)
            elif _on == 216:
                self.filename = self._root.ObfsFname39(self._io, self, self._root)
            elif _on == 201:
                self.filename = self._root.ObfsFname54(self._io, self, self._root)
            elif _on == 210:
                self.filename = self._root.ObfsFname45(self._io, self, self._root)
            elif _on == 208:
                self.filename = self._root.ObfsFname44(self._io, self, self._root)
            elif _on == 205:
                self.filename = self._root.ObfsFname50(self._io, self, self._root)
            elif _on == 203:
                self.filename = self._root.ObfsFname52(self._io, self, self._root)
            elif _on == 221:
                self.filename = self._root.ObfsFname34(self._io, self, self._root)
            elif _on == 227:
                self.filename = self._root.ObfsFname30(self._io, self, self._root)
            elif _on == 237:
                self.filename = self._root.ObfsFname18(self._io, self, self._root)
            elif _on == 207:
                self.filename = self._root.ObfsFname48(self._io, self, self._root)
            elif _on == 204:
                self.filename = self._root.ObfsFname51(self._io, self, self._root)
            elif _on == 217:
                self.filename = self._root.ObfsFname41(self._io, self, self._root)
            elif _on == 241:
                self.filename = self._root.ObfsFname14(self._io, self, self._root)
            elif _on == 231:
                self.filename = self._root.ObfsFname17(self._io, self, self._root)
            elif _on == 206:
                self.filename = self._root.ObfsFname49(self._io, self, self._root)
            elif _on == 226:
                self.filename = self._root.ObfsFname29(self._io, self, self._root)
            elif _on == 240:
                self.filename = self._root.ObfsFname15(self._io, self, self._root)
            elif _on == 225:
                self.filename = self._root.ObfsFname28(self._io, self, self._root)
            elif _on == 238:
                self.filename = self._root.ObfsFname24(self._io, self, self._root)
            elif _on == 232:
                self.filename = self._root.ObfsFname23(self._io, self, self._root)
            elif _on == 229:
                self.filename = self._root.ObfsFname26(self._io, self, self._root)
            elif _on == 235:
                self.filename = self._root.ObfsFname46(self._io, self, self._root)
            elif _on == 242:
                self.filename = self._root.ObfsFname19(self._io, self, self._root)
            elif _on == 215:
                self.filename = self._root.ObfsFname40(self._io, self, self._root)
            elif _on == 212:
                self.filename = self._root.ObfsFname43(self._io, self, self._root)
            elif _on == 213:
                self.filename = self._root.ObfsFname42(self._io, self, self._root)
            elif _on == 200:
                self.filename = self._root.ObfsFname55(self._io, self, self._root)
            elif _on == 223:
                self.filename = self._root.ObfsFname35(self._io, self, self._root)
            elif _on == 228:
                self.filename = self._root.ObfsFname21(self._io, self, self._root)
            elif _on == 222:
                self.filename = self._root.ObfsFname33(self._io, self, self._root)
            self.file_type = self._root.FileType(self._io.read_u1())
            self.compressed = self._io.read_u1()
            self.uncompressed_length = self._io.read_u4le()
            self.in_archive_length = self._io.read_u4le()
            self.body_ofs = self._io.read_u4le()
            self.end_of_record = self._io.ensure_fixed_contents(b"\x00\x00\x00\x00")
            self.unknown5 = self._io.read_u4le()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.body_ofs)
            self._raw__m_body = io.read_bytes(self.in_archive_length)
            io = KaitaiStream(BytesIO(self._raw__m_body))
            self._m_body = self._root.Body(io, self, self._root)
            io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    class ObfsFname37(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(37)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname26(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(26)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(32)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname19(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(19)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname21(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(21)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname9(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(9)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname15(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(15)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsdFname(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.text = (self._io.read_bytes_full()).decode(u"SJIS")


    class ObfsFname49(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(49)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname43(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(43)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    class ObfsFname10(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_holder = self._io.read_bytes(10)
            self._raw_holder = KaitaiStream.process_xor_one(self._raw__raw_holder, 201)
            io = KaitaiStream(BytesIO(self._raw_holder))
            self.holder = self._root.ObfsdFname(io, self, self._root)


    @property
    def header(self):
        if hasattr(self, '_m_header'):
            return self._m_header if hasattr(self, '_m_header') else None

        _pos = self._io.pos()
        self._io.seek(32)
        self._raw__m_header = self._io.read_bytes((self.header_len - 32))
        io = KaitaiStream(BytesIO(self._raw__m_header))
        self._m_header = self._root.Header(io, self, self._root)
        self._io.seek(_pos)
        return self._m_header if hasattr(self, '_m_header') else None


