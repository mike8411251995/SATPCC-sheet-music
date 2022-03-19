import os

def half_to_full(id):
    return ''.join(chr(ord(char) + 65248) for char in str(id))

song_list = {
    1: ('序曲', 'Worship Prelude', '全新的你'),
    2: ('陪我走', 'Walk With Me', '讓愛走動'),
    3: ('主禱文', "The Lord's Prayer", '展開清晨的翅膀'),
    4: ('耶穌愛你', 'Jesus Loves You', '全新的你'),
    5: ('雲上太陽', 'The Sun Above the Clouds', '全能的創造主'),
    6: ('全新的你', 'A New You', '全新的你'),
    7: ('彼此相愛', 'Love One Another', '全新的你'),
    8: ('常常喜樂', 'Rejoice Always', '全能的創造主'),
    9: ('復興的火', 'The Fire of Revival', '全能的創造主'),
    10: ('主，懇求祢', 'Lord, Guide Me', '全能的創造主'),
    11: ('復興聖潔', 'Revive Holiness', '展開清晨的翅膀'),
    12: ('在祢手中', 'In Your Hands', '展開清晨的翅膀'),
    13: ('讓愛走動', 'Love Overflows', '讓愛走動'),
    14: ('在主愛中', "In God's Love", '讓愛走動'),
    15: ('奇妙的愛', 'Amazing Love', '讓愛走動'),
    16: ('秋雨之福', 'Autumn Blessings', '讓愛走動'),
    17: ('仰望恩典', 'Upon Your Grace', '讓愛走動'),
    18: ('年歲的冠冕', 'The Crown of the Ages', '全新的你'),
    19: ('我主我的神', 'My Lord, My God', '全新的你'),
    20: ('天堂在我心', 'Heaven Is In My Heart', '全新的你'),
    21: ('榮耀都歸祢', 'Glory To You', '全新的你'),
    22: ('願祢國降臨', 'Your Kingdom Come', '全能的創造主'),
    23: ('傾聽我的心', 'Listen to My Heart', '全能的創造主'),
    24: ('更深渴慕祢', 'Deeper Longing', '展開清晨的翅膀'),
    25: ('我愛祢，我主', 'I Love You, My Lord', '讓愛走動'),
    26: ('願為主閃亮', 'Shine for the Lord', '讓愛走動'),
    27: ('進入祢的同在', 'Into Your Presence', '全新的你'),
    28: ('把冷漠變成愛', 'Fill Our Hearts With Love', '全新的你'),
    29: ('獻上自己為祭', 'Offer Myself as a Sacrifice', '全能的創造主'),
    30: ('黑暗中的光芒', 'The Light in the Darkness', '全能的創造主'),
    31: ('專心仰望耶穌', 'Focus on Jesus', '全能的創造主'),
    32: ('全能的創造主', 'Wonderful Creator', '全能的創造主'),
    33: ('永活全能的神', 'Almighty Living God', '全能的創造主'),
    34: ('求祢仰起臉來', 'Let the Light of Your Face', '全能的創造主'),
    35: ('我親愛的耶穌 [序曲]', 'My Sweet Jesus', '展開清晨的翅膀'),
    36: ('萬國禱告的殿', 'House of Prayer', '展開清晨的翅膀'),
    37: ('耶穌，我的耶穌', 'Jesus, My Jesus', '展開清晨的翅膀'),
    38: ('如果你想知道', 'If You Want To Know (Where Love is)', '展開清晨的翅膀'),
    39: ('寶座前的敬拜', 'Worship At Your Throne', '讓愛走動'),
    40: ('我一生要讚美祢', "I'll Praise You All My Life", '全新的你'),
    41: ('我願觸動祢心弦', 'Lord, I Want to Touch Your Heart', '展開清晨的翅膀'),
    42: ('展開清晨的翅膀', 'Wings of the Dawn', '展開清晨的翅膀'),
    43: ('彈琴歌唱讚美祢', 'Praise Him!', '展開清晨的翅膀'),
    44: ('祢使我雙腳跳舞', 'Set My Feet to Dancing', '讓愛走動'),
    45: ('改變我，改變世界', 'Change Me, Change the World', '讓愛走動'),
    46: ('耶和華祢是我的神', 'Jehovah, You Are My God', '全新的你'),
    47: ('我心要稱謝耶和華', 'My Heart Will Praise The Lord', '全能的創造主'),
    48: ('耶穌，超乎萬名之名', 'Jesus, Name Above All Names', '展開清晨的翅膀'),
    49: ('願祢榮耀國度降臨', 'Your Glorious Kingdom Come', '展開清晨的翅膀'),
    50: ('這一生最美的祝福', 'The Gift of Knowing You', '讓愛走動'),
    51: ('萬物充滿祢的恩典 [閩]', 'All Creation Filled by Your Love', '讓愛走動'),
    52: ('主的恩典乃是一生之久', 'The Light of Your Grace', '讓愛走動'),
}

for id, (zh_name, en_name) in song_list.items():
    pdf1 = f"{id}.pdf"
    pdf2 = f"{half_to_full(id)}.pdf"
    if os.path.exists(pdf1): os.rename(pdf1, f"{zh_name}.pdf")
    if os.path.exists(pdf2): os.rename(pdf2, f"{zh_name} (吉他譜).pdf")