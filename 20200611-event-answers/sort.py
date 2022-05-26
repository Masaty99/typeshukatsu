def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = 0    #探索範囲の左端
    right = len(array) - 1    #探索範囲の右端
    while left < right:      #探索がぶつかるまで
        while left < right and array[left] < pivot:     #左からの探索
            left += 1
        while left < right and array[right] >= pivot:   #右からの探索
            right -= 1
        if left < right:    #入れ替え処理
            array[left], array[right] = array[right], array[left]
    if left == 0:   #左端の要素が最も小さい時
        left = 1    #分割位置を左から1個目の要素と2個目の要素の間に指定
    return sort(array[:left]) + sort(array[left:])

    # ここまで記述

if __name__ == '__main__':
    main()
