### 主に読んだ部分

[JavaScript 「再」入門](https://developer.mozilla.org/ja/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

### それぞれの型の再確認など

#### [Array](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array)

ぼんやりと覚えていたので、配列のよく使いそうなメソッドを見て確認

filter()は空の配列が返すが、find()ではundefinedが返るなど、把握してないとおそらくハマるので、ちゃんと把握しておくべきかなと思った

#### [Symbol](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

- ES2015から追加されている新しいオブジェクト

知らなかったので詳しく読む

以下のように生成できる。同じシンボルが生成されることはないので、オブジェクトのキーなどに利用できる？

```js

let sym = new Symbol();
// 文字列も渡せる
let sym2 = new Symbol('key');

// Symbol.for()を利用すると同じSymbolを生成できる
const sym3 = Symbol.for("key");
const sym4 = Symbol.for("key");

// sym2==sym3 -> false
// sym3==sym4 -> true
// となる

// Symbol.forで作成したSymbolは、Symbol.keyFor(symbol) を利用することで、生成時のキーを取得できる
Symbol.keyFor(sym3)  // "key"

// Objectの生成時にSymbolを生成する場合は[]で囲む
let obj = {
  [sym2]: "comment"
  id: 1,
  name: "john",
  birthday: "1988-01-01"
};
//もしくは
obj[sym2] = "comment"

// 呼び出しも同様
obj.sym2;  // -> Symbol()

obj[sym2];  // -> "comment"

// for...inを行ったときに参照されない
for(const elm in obj) {
  console.log(obj[elm]); 
}

// > 5
// > "John"
// > "1988-01-01"
```

`for...in`を行ったとや`JSON.stringify()`行ったときに参照されないのでその処理内だけで使える一時的なKeyなどにしておくと使い勝手がよさそう
