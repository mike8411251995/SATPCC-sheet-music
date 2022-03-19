import os
from PyPDF2 import PdfFileMerger

def half_to_full(id):
    return ''.join(chr(ord(char) + 65248) for char in str(id))

def rename(song_list):
    for id, (zh_name, en_name) in song_list.items():
        pdf1 = f"{id}.pdf"
        pdf2 = f"{half_to_full(id)}.pdf"
        if os.path.exists(pdf1): os.rename(pdf1, f"{zh_name}.pdf")
        if os.path.exists(pdf2): os.rename(pdf2, f"{zh_name} (吉他譜).pdf")

if True:
    VOLS = {
        "VOL1": {
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
            18: ('讚美之泉', 'Stream of Praise', '讓讚美飛揚'),
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
        },

        "VOL2": {
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
        },

        "VOL3": {
            1: ("禱告", "I Pray", "單單只為你"),
            2: ("揀選", "Chosen", "寶貴十架"),
            3: ("活石", "Living Stones", "寶貴十架"),
            4: ("這世代", "This Generation", "寶貴十架"),
            5: ("敬拜祢", "We Worship You", "寶貴十架"),
            6: ("我相信", "I Believe", "似乎在天堂"),
            7: ("我相信 [閩南語版]", "I Believe (Taiwanese)", "寶貴十架"),
            8: ("親近祢", "Close to You", "單單只為你"),
            9: ("寧靜谷", "Valley of Peace", "似乎在天堂"),
            10: ("深觸我心", "How Precious You are To Me", "深觸我心"),
            11: ("進入豐盛", "Into His Abundance", "深觸我心"),
            12: ("深深愛祢", "Deeper In Love", "深觸我心"),
            13: ("看見復興", "Until We See You", "深觸我心"),
            14: ("慈愛天父", "God of Mercy", "深觸我心"),
            15: ("一生愛祢", "With All My Love", "深觸我心"),
            16: ("榮耀羔羊", "Glorious King", "深觸我心"),
            17: ("祢的慈愛", "Unfailing Love", "似乎在天堂"),
            18: ("祢的同在", "Your Presence", "單單只為你"),
            19: ("全然美麗", "Beautiful", "似乎在天堂"),
            20: ("耶穌，耶穌", "Jesus, Jesus", "單單只為你"),
            21: ("祢是聖潔", "You Are Holy", "寶貴十架"),
            22: ("喔！十字架", "In the Cross", "寶貴十架"),
            23: ("簡單的歌", "A Simple Song", "似乎在天堂"),
            24: ("寶貴十架", "Precious Cross", "寶貴十架"),
            25: ("寶貴十架 [韓文版]", "Precious Cross (Korean)", "寶貴十架"),
            26: ("聖誕之願", "A Wish For Christmas", "似乎在天堂"),
            27: ("親愛的聖靈", "Come, Holy Spirit", "深觸我心"),
            28: ("求主充滿我", "Come and Fill Me Up", "深觸我心"),
            29: ("我全心頌讚", "I Will Praise You", "深觸我心"),
            30: ("聖潔的敬拜", "The Purest Worship", "深觸我心"),
            31: ("主我跟祢走", "Lord, I Walk With You", "單單只為你"),
            32: ("沙崙的玫瑰", "Rose of Sharon", "單單只為你"),
            33: ("單單只為祢", "For You Alone", "單單只為你"),
            34: ("耶和華尼西", "Jehovah Nissi", "單單只為你"),
            35: ("聖潔全能主", "Holy Is the Lord", "單單只為你"),
            36: ("全地當讚美", "The Whole Earth Will Sing", "單單只為你"),
            37: ("小小的夢想", "Little Dream", "寶貴十架"),
            38: ("祢美好應許", "Your Promise", "單單只為你"),
            39: ("在祢寶座前", "Before Your Throne", "寶貴十架"),
            40: ("似乎在天堂", "Just Like Heaven", "似乎在天堂"),
            41: ("求聽我呼求", "Hear My Voice", "似乎在天堂"),
            42: ("凡事都能做", "All Things Are Possible", "深觸我心"),
            43: ("祢是配得讚美", "You Alone are Worthy", "深觸我心"),
            44: ("邁向新的生命", "A Brand New Life", "深觸我心"),
            45: ("主祢是我力量", "You Are My Strength", "寶貴十架"),
            46: ("祢恩典不離開", "Your Grace", "似乎在天堂"),
            47: ("祢是我的一切", "You Are Everything To Me", "似乎在天堂"),
            48: ("我要常常喜樂", "I Will Always Rejoice", "似乎在天堂"),
            49: ("聖哉聖哉聖哉", "Holy, Holy, Holy", "寶貴十架"),
            50: ("聖靈降下恩雨", "Holy Spirit Rain Down", "寶貴十架"),
            51: ("這就是你的愛", "Your Love Is Amazing", "似乎在天堂"),
            52: ("我的救贖者活著", "My Redeemer Lives", "深觸我心"),
            53: ("耶和華坐著為王", "Lord, You Sit Enthroned", "單單只為你"),
            54: ("耶和華是我牧者", "Lord, You Are My Shepherd", "單單只為你"),
            55: ("我心切切渴慕祢", "My Heart Shall Long For You", "單單只為你"),
            56: ("主的喜樂是我力量", "The Joy of the Lord Is My Strength", "深觸我心"),
            57: ("Come Away With Me", "Come Away With Me", "似乎在天堂"),
        }
    }

for vol_name, vol in VOLS.items():
    # for k, v in vol.items():
    #     assert len(v) == 3

    #     chi, eng, album = v
        
    #     pdf1 = os.path.join(vol_name, f"{chi}.pdf")
    #     pdf2 = os.path.join(vol_name, f"{chi} (吉他譜).pdf")
    #     if os.path.exists(pdf1):
    #         os.makedirs(os.path.join(vol_name, album), exist_ok=True)
    #         os.rename(pdf1, os.path.join(vol_name, album, f"{chi}.pdf"))
    #     if os.path.exists(pdf2):
    #         os.makedirs(os.path.join(vol_name, album), exist_ok=True)
    #         os.rename(pdf2, os.path.join(vol_name, album, f"{chi} (吉他譜).pdf"))
    for k, v in vol.items():
        chi, eng, album = v
        pdf1 = os.path.join(vol_name, album, f"{chi}.pdf")
        pdf2 = os.path.join(vol_name, album, f"{chi} (吉他譜).pdf")
        if os.path.exists(pdf1) and os.path.exists(pdf2):
            merger = PdfFileMerger()
            for pdf in [pdf1, pdf2]:
                merger.append(pdf)
            merger.write(os.path.join(vol_name, album, f"{chi} (完整譜).pdf"))
            merger.close()
            os.rename(pdf1, os.path.join(vol_name, album, f"{chi} (一般譜).pdf"))
            os.rename(os.path.join(vol_name, album, f"{chi} (完整譜).pdf"),
                      os.path.join(vol_name, album, f"{chi}.pdf"))
            