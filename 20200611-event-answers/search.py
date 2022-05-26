def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    left = 0    #探索範囲の左端を示す変数
    right = len(sorted_array) - 1   #探索範囲の右端を示す変数
    while left <= right:    #
        center = (left + right) // 2    #探索範囲の真ん中を示す変数
        if sorted_array[center] == target_number:   #探索対象が探索範囲の真ん中にあった時
            return center   #そのインデックスを返す
        elif sorted_array[center] < target_number:  #探索対象が真ん中の数より大きかった時
            left = center + 1   #探索範囲を右側にずらす
        else:   #探索対象が真ん中の数より小さかった時
            right = center - 1  #探索範囲を左側にずらす
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
