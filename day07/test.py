from find_nested_keys_values import (
    find_directory_size,
    find_parent_keys,
    update_key_value,
)

##################################################
##### TEST FUNCTIONALITY ON THE EXAMPLE DATA #####
##################################################

dct = {}
parent_keys = find_parent_keys(dct, "/", {})
dct["/"] = [0, {}]
dct = update_key_value(dct, parent_keys, "/", {"a": "dir"})
print(dct)

dct = {
    "/": [
        23352670,
        {
            "a": "dir",
            "b.txt": "14848514",
            "c.dat": "8504156",
            "d": "dir",
        },
    ]
}
parent_keys = find_parent_keys(dct, "a", "dir")
dct = update_key_value(dct, parent_keys, "a", [0, {}])
print(dct)

dct = {
    "/": [
        23446939,
        {
            "a": [
                94269,
                {"e": {}, "f": "29116", "g": "2557", "h.lst": "62596"},
            ],
            "b.txt": "14848514",
            "c.dat": "8504156",
            "d": "dir",
        },
    ]
}
parent_keys = find_parent_keys(dct, "e", {})
dct = update_key_value(dct, parent_keys, "e", {"i": "584"})
print(dct)

dct = {
    "/": [
        23447523,
        {
            "a": [
                94853,
                {
                    "e": {"i": "584"},
                    "f": "29116",
                    "g": "2557",
                    "h.lst": "62596",
                },
            ],
            "b.txt": "14848514",
            "c.dat": "8504156",
            "d": "dir",
        },
    ]
}
parent_keys = find_parent_keys(dct, "d", "dir")
dct = update_key_value(dct, parent_keys, "d", {})
print(dct)

dct = {
    "/": [
        48381165,
        {
            "a": [
                94853,
                {
                    "e": [584, {"i": "584"}],
                    "f": "29116",
                    "g": "2557",
                    "h.lst": "62596",
                },
            ],
            "b.txt": "14848514",
            "c.dat": "8504156",
            "d": [
                24933642,
                {
                    "j": "4060174",
                    "d.log": "8033020",
                    "d.ext": "5626152",
                    "k": "7214296",
                },
            ],
        },
    ]
}

sum = find_directory_size(dct, MAX_SIZE=100000)
print(sum)

size = find_directory_size(dct, MIN_SIZE=dct["/"][0] - 40000000)
print(size)

#################################################
##### TEST FUNCTIONALITY ON MY PUZZLE INPUT #####
#################################################

GET_SIZE = False

dct = {
    "/": {
        "gldg.jrd": "246027",
        "qffvbf": {
            "dcqf": {"gcjmpnsl": {"gldg.jrd": "198360"}},
            "grcj": {"grgtnhn.zdn": "56512"},
            "hwllqcd": {
                "frzf.mzc": "100505",
                "gldg.jrd": "209030",
                "jjtjjlsr.dnl": "9330",
                "mfmps.vjt": "191034",
                "nscv.wvb": "82405",
            },
            "jrhp.hgg": "76103",
            "nscv.wvb": "253696",
            "stnrzs": {
                "gmtmfpmb": {"hswhjhmj": "279472", "rsgsrn": "81339"},
                "jrhp": {
                    "fpmnp": {"grcj.tcj": "33215"},
                    "grcj.scb": "99771",
                    "hjglg": {"tctfwpf.jhv": "206893"},
                    "hwvzv": {"mfmps": {"rjrmbqwr.wbj": "46252"}},
                },
                "rhf": {
                    "dcgvw": "222859",
                    "grcj.qzh": "41140",
                    "zcjh": {"prqhbzl.hls": "92243"},
                    "zgqjbf": "217515",
                },
                "wzjtd": {
                    "bnjj": {"zjdvggcz.fhr": "158778"},
                    "dhhpf": {
                        "gldg.jrd": "228680",
                        "wcfpqqp.tcf": "18523",
                    },
                    "grcj": "dir",
                    "jqmnp": "dir",
                    "mfmps.dht": "16602",
                    "mrgh": "dir",
                    "rsgsrn": "112236",
                    "wqwwwfd": "dir",
                    "zgqjbf.bjh": "243851",
                },
            },
            "vzgpfd": "dir",
        },
        "qjjgh": "dir",
        "vpjqpqfm": "dir",
    }
}
parent_keys = find_parent_keys(dct, "grcj", "dir")
dct = update_key_value(dct, parent_keys, "grcj", {}, GET_SIZE)
print(dct)

dct = {
    "/": {
        "gldg.jrd": "246027",
        "qffvbf": {
            "dcqf": {"gcjmpnsl": {"gldg.jrd": "198360"}},
            "grcj": {"grgtnhn.zdn": "56512"},
            "hwllqcd": {
                "frzf.mzc": "100505",
                "gldg.jrd": "209030",
                "jjtjjlsr.dnl": "9330",
                "mfmps.vjt": "191034",
                "nscv.wvb": "82405",
            },
            "jrhp.hgg": "76103",
            "nscv.wvb": "253696",
            "stnrzs": {
                "gmtmfpmb": {"hswhjhmj": "279472", "rsgsrn": "81339"},
                "jrhp": {
                    "fpmnp": {"grcj.tcj": "33215"},
                    "grcj.scb": "99771",
                    "hjglg": {"tctfwpf.jhv": "206893"},
                    "hwvzv": {"mfmps": {"rjrmbqwr.wbj": "46252"}},
                },
                "rhf": {
                    "dcgvw": "222859",
                    "grcj.qzh": "41140",
                    "zcjh": {"prqhbzl.hls": "92243"},
                    "zgqjbf": "217515",
                },
                "wzjtd": {
                    "bnjj": {"zjdvggcz.fhr": "158778"},
                    "dhhpf": {
                        "gldg.jrd": "228680",
                        "wcfpqqp.tcf": "18523",
                    },
                    "grcj": {"bcbspw": "dir", "mpq": "dir", "pjzw": "dir"},
                    "jqmnp": "dir",
                    "mfmps.dht": "16602",
                    "mrgh": "dir",
                    "rsgsrn": "112236",
                    "wqwwwfd": "dir",
                    "zgqjbf.bjh": "243851",
                },
            },
            "vzgpfd": "dir",
        },
        "qjjgh": "dir",
        "vpjqpqfm": "dir",
    }
}
parent_keys = find_parent_keys(dct, "bcbspw", "dir")
dct = update_key_value(dct, parent_keys, "bcbspw", {}, GET_SIZE)
print(dct)

dct = {
    "/": {
        "gldg.jrd": "246027",
        "qffvbf": {
            "dcqf": {"gcjmpnsl": {"gldg.jrd": "198360"}},
            "grcj": {"grgtnhn.zdn": "56512"},
            "hwllqcd": {
                "frzf.mzc": "100505",
                "gldg.jrd": "209030",
                "jjtjjlsr.dnl": "9330",
                "mfmps.vjt": "191034",
                "nscv.wvb": "82405",
            },
            "jrhp.hgg": "76103",
            "nscv.wvb": "253696",
            "stnrzs": {
                "gmtmfpmb": {"hswhjhmj": "279472", "rsgsrn": "81339"},
                "jrhp": {
                    "fpmnp": {"grcj.tcj": "33215"},
                    "grcj.scb": "99771",
                    "hjglg": {"tctfwpf.jhv": "206893"},
                    "hwvzv": {"mfmps": {"rjrmbqwr.wbj": "46252"}},
                },
                "rhf": {
                    "dcgvw": "222859",
                    "grcj.qzh": "41140",
                    "zcjh": {"prqhbzl.hls": "92243"},
                    "zgqjbf": "217515",
                },
                "wzjtd": {
                    "bnjj": {"zjdvggcz.fhr": "158778"},
                    "dhhpf": {
                        "gldg.jrd": "228680",
                        "wcfpqqp.tcf": "18523",
                    },
                    "grcj": {
                        "bcbspw": {"rsgsrn": "5449"},
                        "mpq": {"mfmps": "135338"},
                        "pjzw": {"cpffwn": {"rnwqngz": "131835"}},
                    },
                    "jqmnp": {
                        "nscv.wvb": "281939",
                        "rsgsrn": "103834",
                        "wcfpqqp.tcf": "34528",
                    },
                    "mfmps.dht": "16602",
                    "mrgh": {"grcj": {"bbzm.sbq": "211470"}},
                    "rsgsrn": "112236",
                    "wqwwwfd": {"blfr.lqh": "59532"},
                    "zgqjbf.bjh": "243851",
                },
            },
            "vzgpfd": {
                "grcj": {
                    "jbfsbsnn.sgj": "160936",
                    "mfmps": {
                        "dcgvw": "176441",
                        "grcj.sdl": "9961",
                        "mfmps": "dir",
                        "nscv.wvb": "181303",
                        "zfjhqtp": "273550",
                    },
                    "mfqjssr": "dir",
                    "vzgpfd": "dir",
                    "zgqjbf": "dir",
                },
                "lvhfqr": "dir",
                "zgvjpnf": "dir",
            },
        },
        "qjjgh": "dir",
        "vpjqpqfm": "dir",
    }
}
parent_keys = find_parent_keys(dct, "mfmps", "dir")
dct = update_key_value(dct, parent_keys, "mfmps", {}, GET_SIZE)
print(dct)
