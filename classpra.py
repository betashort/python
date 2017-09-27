class parent():
    def __init__(self, name):
        self.name = name
        print("コンストラクタ起動しました。")
    def tall(self, cm):
        self.cm = cm
        print(self.name + "の身長は" + self.cm + "cmです")

#継承　
class child(parent):
    #__init__を書き換え（オーバーライド）
    def __init__(self, name):
        self.name = name
        print("継承で子供を作りました。")
    
    #weightの追加（メソッドの追加)
    def weight(self, g):
        self.g = g
        print(self.name + "の体重は" + self.g +"gです")

#オブジェクト生成（親）
person = parent('親')
#メソッドの呼び出し（tall)
person.tall('169')

#オブジェクト生成（子供）
children = child('子供')
#メソッドの呼び出し(継承,tall)
children.tall('150')
#メソッドの呼び出し(継承,weight)
children.weight('50')
