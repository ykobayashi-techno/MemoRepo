<style>
	img {
		border: 1px solid #000;
	}
</style>

# 最近AI関係で調べてたこと

## Cursor

[Cursor](https://www.cursor.com/)

### Cursorとは

ChatGPTやClaudeのChatAPIに対応しているエディタ

ただ単純に対応しているだけでなく、Web上の言語のドキュメントページやローカルのソースを指定すればそれを参照したうえで返答をしてくれる
ActionScriptのドキュメントページを指定したところ問題なく使えそうだった

AdobeAIR、ApacheFlexの開発情報はWeb上で探すのが今となってはちょっと大変だったりするので、ちらっと動作例を出してほしいときに有用だった
また、渡和さんのライブラリ部分についての返答もしっかりしてくれていたので驚いた

![CursorでAirplasのことを聞く](./images/cursor_airplas.png)

VSCodeベースなので拡張機能、デバッグやビルドの設定、Copilotもそのまま使えるのでスっと移行できた

## LLMをローカルで動かす

いろんな企業や個人がモデルを作って公開しているのでそれを実行してみたいと思い手元で動く方法を調べる

### ツールや場所

モデルが公開されているコミュニティサイト。個人だけでなくMicrosoftやMetaのような企業のモデルもここで公開されています

[Hagging Face](https://huggingface.co/)

たとえば最近出たCopilot+に対応したPCは、ローカルでAIが動くことが売りになっているが、ベースになってるモデルが公開されています

[Copilot+ PC](https://www.microsoft.com/ja-jp/windows/copilot-plus-pcs?r=1)

[MSのPhi3](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3)

![Phi3](./images/hagging-phi3.png)

簡単に実行するためのソフトとしてGUIやCUIベースでソフトがある。軽量な、量子化されているモデル(実行しやすくしたもの)を実行するにはこれらで十分

[LMStudio](https://lmstudio.ai/)
[Ollama](https://ollama.com/)

### その他（今回の方法）

せっかくなのでpythonの環境を整えてその他のモデルも動かしたい

pythonも知らないためGeminiに聞きながら環境を構築して実行してみた

最近、新たなサイバーエージェントから日本語のモデルも公開されたのでちょっと動かしてみたい（まだ）

[ニュースリリース](https://www.cyberagent.co.jp/news/detail/id=30463)
[デモページ](https://huggingface.co/spaces/cyberagent/calm3-22b-chat-demo)

#### 注意点

軽量なモデルでは許容範囲だと思いますが、ノートPCでは応答に時間がかかることがほとんどです

ほぼGPU必須かと思います

※とくに大型のモデルになるとVRAMが80GBほどいるので、ローカルでは不可能


