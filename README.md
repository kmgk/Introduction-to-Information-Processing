問題は告知なく修正、追加される場合があります。質問や要望がある場合は[twitter](https://twitter.com/hkimrgakgi)か[Issue](https://github.com/kmgk/Introduction-to-Information-Processing/issues)を立ててください。

ヒントとVBAチートシートは要望とモチベがあれば作成するかもしれません。

## 注意

文字化けする場合は`utf-8.csv`の方でやってみてください。

## ストーリー(読まなくても構いません)

あなたは材料キングダムの住人です。ある日、OHKA ウイルスが国中に蔓延し外出自粛による経済難が国を襲いました。そこで、経済対策として国民全員に 5 千兆円を配ることが決まりました。幸い国民全員の名前、住所、口座番号が紐づけられている国民管理システムがあるので、それを使って国民へ 5 千兆円を配布することができます。

しかし、材料キングダムにはお金を配布する際にある法律が関わってきます。それは、確認のため国民管理システム登録されている内容と同じもの（名前、住所、口座番号）を国に送信しなければならない、というものです。そのため国の担当者は一夜にしてそのシステムを作り上げてインターネット上に公開し、国民に情報を送信してもらいました。

そしてあなたはその情報を処理する以下のタスクを任されました。以下の問題を解いてください。

## 条件

csv ファイルを見ながら読むと理解しやすいと思います。

### 集めた情報

国民が送信した情報は`info.csv`に保存されています。保存形式は以下のようになっています。

| 性       | 名   | 県名   | 市名   | 町名   | 口座番号 |
| -------- | ---- | ------ | ------ | ------ | -------- |
| (例)山田 | 太郎 | 物質県 | 理工市 | 材料町 | 111-1111 |

各列は以下の要件を満たしています

- 県名

  `〇〇県`と`〇〇`の場合がある。都道府は存在せず県のみ存在する。

  例）`愛知県`、`愛知`

- 市名

  `〇〇市`と`〇〇`の場合がある。区などは存在せず市のみ存在する。

  例）`知立市`、`知立`

- 町名

  `〇〇町`と`〇〇`の場合がある。村などは存在せず町のみ存在する。

  例）`片倉町`、`片倉`

- 口座番号

  `〇〇〇-〇〇〇〇`(3 桁-4 桁)の場合と`〇〇〇〇〇〇〇`(7 桁)の場合がある

  例）`123-4567`、`1234567`

### 国民管理システム

国民管理システムの情報は`control.csv`に保存されています。保存形式は以下のようになっています。

| 性       | 名   | 住所               | 口座番号 |
| -------- | ---- | ------------------ | -------- |
| (例)山田 | 太郎 | 愛知県知立市片倉町 | 1111111  |

各列は以下の要件を満たしています

- 住所

  `〇〇県××市□□町`の形式で保存。例）`静岡県沼津市本田町`

- 口座番号

  `〇〇〇〇〇〇〇`(7 桁)で保存。例）`1234567`

## 問 1. 集めた情報の読み込み

`info.csv`を読み込み、読み込んだものを値を変えることなく 6xN の二次元配列に保存しその配列を返す Function プロシージャを作成してください。

<details>
<summary>解答例</summary>

```vb
Function problem1() As String()
    ChDrive ThisWorkbook.Path
    ChDir ThisWorkbook.Path

    Open "info.csv" For Input As #1
    Dim line As String, i As Long
    Dim arr() As String
    Dim lineNum As Long

    lineNum = 0
    Do Until EOF(1)
        Line Input #1, line
        lineElements = Split(line, ",")
        ReDim Preserve arr(5, lineNum)
        For i = 0 To UBound(lineElements)
            arr(i, lineNum) = lineElements(i)
        Next i
        lineNum = lineNum + 1
    Loop

    problem1 = arr()

    Close #1
End Function
```

</details>

## 問 2. エクセルへの記入

特に理由はありませんが、VBA の練習のために問 1 で作成した Function プロシージャの返り値を全てエクセルに記入する Sub プロシージャを作成してください。ただし、一行目は各列の種類 `性、名、県名、市名、町名、口座番号（のいずれか）`を入力してください。

<details>
<summary>解答例</summary>

```vb
Sub problem2(ByRef arr() As String)
    Dim i As Long, j As Long

    For i = 0 To UBound(arr, 1)
        For j = 0 To UBound(arr, 2)
            Cells(j + 1, i + 1).Value = arr(i, j)
        Next j
    Next i
End Sub
```

</details>

## 問 3. データ整理

問 1 で作った Function プロシージャの返り値の配列を整理してもらいます。現在の配列には`性、名、県名、市名、町名、口座番号`の情報が入っていますが、以下の処理をして`性、名、住所、口座番号`に変換したものを新しい配列に保存し、それを返す Function プロシージャを作成してください。

### 処理

- `性`、`名`はそのまま
- `県名`、`市名`、`町名`は`住所`として(#条件)を満たすように変換する
- `口座番号`は[条件](#条件)を満たすように変換する。

<details>
<summary>解答例</summary>

```vb
Function problem3(ByRef arr() As String) As String()
    Dim result() As String
    Dim i As Long, j As Long
    Dim lineNum As Long

    lineNum = 0
    ReDim Preserve result(3, lineNum)
    result(0, 0) = "性"
    result(1, 0) = "名"
    result(2, 0) = "住所"
    result(3, 0) = "口座番号"
    For i = 1 To UBound(arr, 2)
        lineNum = lineNum + 1
        ReDim Preserve result(3, lineNum)
        For j = 0 To 3
            Select Case j
            Case 0
                result(j, i) = arr(j, i)
            Case 1
                result(j, i) = arr(j, i)
            Case 2
                result(j, i) = Split(arr(2, i), "県")(0) + "県" + Split(arr(3, i), "市")(0) + "市" + Split(arr(4, i), "町")(0) + "町"
            Case 3
                kouza = Split(arr(5, i), "-")
                If UBound(kouza) = 0 Then
                    result(j, i) = kouza(0)
                Else
                    result(j, i) = kouza(0) + kouza(1)
                End If
            End Select
        Next j
    Next i

    problem3 = result()
End Function
```

</details>

## 問 4. csv 出力

問 3.で作った Function プロシージャの返り値の配列を `result.csv` に出力する Sub プロシージャを作成してください。ただし一行目は各列の種類 `性、名、住所、口座番号（のいずれか）`を出力してください。

<details>
<summary>解答例</summary>

```vb
Sub problem4(ByRef arr() As String)
    Dim i As Long, j As Long
    Dim filePath As String

    filePath = ThisWorkbook.Path & "\result.csv"
    Open filePath For Output As #1

    For i = 0 To UBound(arr, 2)
        For j = 0 To UBound(arr, 1)
            If j <> UBound(arr, 1) Then
                Print #1, arr(j, i) & ",";
            Else
                Print #1, arr(j, i)
            End If
        Next j
    Next i
    Close #1
End Sub

```

</details>

## 問 5. まとめ

問 1~問 4 までの一連の動作を組み合わせて実際に動くプログラムを作成してください。

<details>
<summary>解答例</summary>

```vb
Sub main()
    Dim arr() As String


    arr = problem1()
    Call problem2(arr)
    arr = problem3(arr)
    Call problem4(arr)
End Sub
```

</details>
