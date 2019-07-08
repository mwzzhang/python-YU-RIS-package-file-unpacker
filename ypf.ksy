meta:
  id: ypf
  application: YU-RIS Script Engine package file (?)
  endian: le

seq:
  - id: magic
    contents: ["YPF", 0]
  - id: engine_version
    type: u4
  - id: file_count
    type: u4
  - id: header_len  # address of first file
    type: u4
  - id: guard
    contents: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

instances:
  header:
    pos: 0x20
    size: header_len - 0x20
    type: header

# temp header
types:
  header:
    seq:
      - id: entries
        type: file_entry
        repeat: eos
  
  file_entry:
    seq:
      - id: unknown0
        type: u4
      - id: filename_length_marker
        type: u1
      - id: filename
        type: 
          switch-on: filename_length_marker
          cases:
            0xf4: obfs_fname_9
            0xfc: obfs_fname_10
            0xf6: obfs_fname_11
            0xef: obfs_fname_12
            0xec: obfs_fname_13
            0xf1: obfs_fname_14
            0xf0: obfs_fname_15
            0xf3: obfs_fname_16
            0xe7: obfs_fname_17
            0xed: obfs_fname_18
            0xf2: obfs_fname_19
            0xd1: obfs_fname_20
            0xe4: obfs_fname_21
            0xe9: obfs_fname_22
            0xe8: obfs_fname_23
            0xee: obfs_fname_24
            0xe6: obfs_fname_25
            0xe5: obfs_fname_26
            0xea: obfs_fname_27
            0xe1: obfs_fname_28
            0xe2: obfs_fname_29
            0xe3: obfs_fname_30
            0xe0: obfs_fname_31
            0xdc: obfs_fname_32
            0xde: obfs_fname_33
            0xdd: obfs_fname_34
            0xdf: obfs_fname_35
            0xdb: obfs_fname_36
            0xda: obfs_fname_37
            0xd6: obfs_fname_38
            0xd8: obfs_fname_39
            0xd7: obfs_fname_40
            0xd9: obfs_fname_41
            0xd5: obfs_fname_42
            0xd4: obfs_fname_43
            0xd0: obfs_fname_44
            0xd2: obfs_fname_45
            0xeb: obfs_fname_46
            0xd3: obfs_fname_47
            0xcf: obfs_fname_48
            0xce: obfs_fname_49
            0xcd: obfs_fname_50
            0xcc: obfs_fname_51
            0xcb: obfs_fname_52
            0xf9: obfs_fname_53
            0xc9: obfs_fname_54
            0xc8: obfs_fname_55
      - id: file_type
        type: u1
        enum: file_type
      - id: compressed
        type: u1
      - id: uncompressed_length
        type: u4
      - id: in_archive_length
        type: u4
      - id: body_ofs
        type: u4
      - id: end_of_record
        contents: [0, 0, 0, 0]
      - id: unknown5
        type: u4
    instances:
      body:
        pos: body_ofs
        size: in_archive_length
        io: _root._io
        type: body
  
  body:
    seq:
      - id: cmprsd_body
        process: zlib
        size-eos: true
        if: _parent.compressed == 1
      - id: body
        size-eos: true
        if: _parent.compressed == 0

  obfsd_fname:
    seq:
      - id: text
        type: str
        encoding: SJIS
        size-eos: true
  
  obfs_fname_9:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 9
  obfs_fname_10:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 10
  obfs_fname_11:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 11
  obfs_fname_12:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 12
  obfs_fname_13:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 13
  obfs_fname_14:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 14
  obfs_fname_15:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 15
  obfs_fname_16:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 16
  obfs_fname_17:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 17
  obfs_fname_18:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 18
  obfs_fname_19:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 19
  obfs_fname_20:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 20
  obfs_fname_21:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 21
  obfs_fname_22:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 22
  obfs_fname_23:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 23
  obfs_fname_24:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 24
  obfs_fname_25:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 25
  obfs_fname_26:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 26
  obfs_fname_27:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 27
  obfs_fname_28:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 28
  obfs_fname_29:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 29
  obfs_fname_30:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 30
  obfs_fname_31:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 31
  obfs_fname_32:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 32
  obfs_fname_33:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 33
  obfs_fname_34:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 34
  obfs_fname_35:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 35
  obfs_fname_36:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 36
  obfs_fname_37:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 37
  obfs_fname_38:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 38
  obfs_fname_39:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 39
  obfs_fname_40:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 40
  obfs_fname_41:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 41
  obfs_fname_42:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 42
  obfs_fname_43:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 43
  obfs_fname_44:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 44
  obfs_fname_45:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 45
  obfs_fname_46:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 46
  obfs_fname_47:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 47
  obfs_fname_48:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 48
  obfs_fname_49:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 49
  obfs_fname_50:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 50
  obfs_fname_51:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 51
  obfs_fname_52:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 52
  obfs_fname_53:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 53
  obfs_fname_54:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 54
  obfs_fname_55:
    seq:
      - id: holder
        process: xor(201)
        type: obfsd_fname
        size: 55

enums:
  file_type:
    0: text
    2: png
    3: jpg
    5: wav
    6: ogg
