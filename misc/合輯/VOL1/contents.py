import os

def half_to_full(id):
    return ''.join(chr(ord(char) + 65248) for char in str(id))

song_list = {
    1: ('尋找', 'Searching', '彩虹下的約定'),
    2: ('甦醒', 'Awakening', '甦醒'),
    3: ('是耶穌', "It's Jesus", '彩虹下的約定'),
    4: ('起來吧', 'Arise', '甦醒'),
    5: ('全然向祢', 'All For You', '讓讚美飛揚'),
    6: ('光明之子', 'Children of Light', '讓讚美飛揚'),
    7: ('有一位神', 'There Is A God', '讓讚美飛揚'),
    8: ('除祢以外', 'Whom Have I But You', '耶和華祝福滿滿'),
    9: ('從今天起', 'From This Day On', '耶和華祝福滿滿'),
    10: ('新造的人', 'A New Creation', '讓讚美飛揚'),
    11: ('愛我願意', 'I Receive Your Love', '彩虹下的約定'),
    12: ('與你有約', 'The Promise', '彩虹下的約定'),
    13: ('誰能像祢', 'Who Is Like You', '讓讚美飛揚'),
    14: ('興起發光', 'Arise and Shine', '甦醒'),
    15: ('賜我自由', 'Grant Me Freedom', '彩虹下的約定'),
    16: ('馨香晚祭', 'The Evening Sacrifice', '彩虹下的約定'),
    17: ('犧牲的愛', 'The Sacrificial Love', '耶和華祝福滿滿'),
    18: ('讀美之泉', 'Stream of Praise', '讓讚美飛揚'),
    19: ('天父的孩子', "Father's Beloved Child", '彩虹下的約定'),
    20: ('主我敬拜祢', 'Lord, I Worship You', '甦醒'),
    21: ('生命的舵手', 'The Navigator of My Life', '讓讚美飛揚'),
    22: ('注目看耶穌', 'Look Upon Jesus', '甦醒'),
    23: ('為中國祈禱', 'A Prayer For China', ''),
    24: ('愛喜樂生命', 'Love, Joy and Life', '耶和華祝福滿滿'),
    25: ('認識祢真好', "It's Good to Know You", '耶和華祝福滿滿'),
    26: ('豐盛的人生', 'Abundant Life', '甦醒'),
    27: ('讓讚美飛揚', 'Let Praise Arise', '讓讚美飛揚'),
    28: ('一切歌頌讚美', 'Praise The Lord', '彩虹下的約定'),
    29: ('主賜福如春雨', 'Rain of Blessings', '耶和華祝福滿滿'),
    30: ('平安的七月夜', 'Peaceful July', '甦醒'),
    31: ('彩虹下的約定', 'The Covenant Under The Rainbow', '彩虹下的約定'),
    32: ('給我清潔的心', 'Create In Me A Clean Heart', '甦醒'),
    33: ('萬軍之耶和華', 'Almighty Jehovah', '讓讚美飛揚'),
    34: ('我們是光明之子', 'We Are the Children of Light', '讓讚美飛揚'),
    35: ('耶和華祝福滿滿', "Jehovah's Blessings Abound", '耶和華祝福滿滿'),
    36: ('激起生命的浪花', 'The Journey Through the Waves', '彩虹下的約定'),
    37: ('我對祢的愛永不變', 'My Love For You Will Never Change', '彩虹下的約定'),
    38: ('你們要讚美耶和華', 'Praise The Lord All Ye People', '耶和華祝福滿滿'),
    39: ('唯有主耶穌的寶血', 'Only The Blood', '讓讚美飛揚'),
    40: ('我的心你要稱頌耶和華', 'Praise The Lord, O My Soul', '甦醒'),
    41: ('這是耶和華所定的日子', 'This is The Day', '彩虹下的約定'),
}

for id, (zh_name, en_name) in song_list.items():
    pdf1 = f"{id}.pdf"
    pdf2 = f"{half_to_full(id)}.pdf"
    if os.path.exists(pdf1): os.rename(pdf1, f"{zh_name}.pdf")
    if os.path.exists(pdf2): os.rename(pdf2, f"{zh_name} (吉他譜).pdf")