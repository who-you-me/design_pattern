# デザインパターンに慣れる

| パターン名 | 概要 |
| ---------- | ---- |
| Iterator | 複数の要素を内包するオブジェクトのすべての要素に順にアクセスする方法を提供する。反復子。 |
| Adapter | 元々関連性のない2つのクラスを接続するクラスを作る。 |

# サブクラスにまかせる

| パターン名 | 概要 |
| ---------- | ---- |
| Template Method | あるアルゴリズムの途中経過で必要な処理を抽象メソッドに委ね、その実装を変えることで処理が変えられるようにする。
| Factory Method | 実際に生成されるインスタンスに依存しない、インスタンスの生成方法を提供する。 |

# インスタンスを作る

| パターン名 | 概要 |
| ---------- | ---- |
| Sigleton | あるクラスについて、インスタンスが単一であることを保証する。 |
| Prototype | 同様のインスタンスを生成するために、原型のインスタンスを複製する。 |
| Builder | 複合化されたインスタンスの生成過程を隠蔽する。 |
| Abstract Factory | 関連する一連のインスタンスを状況に応じて適切に生成する方法を提供する。 |

# 分けて考える

| パターン名 | 概要 |
| ---------- | ---- |
| Bridge | クラスなどの実装と、呼出し側の間の橋渡しをするクラスを用意し、実装を隠蔽する。 |
| Strategy | データ構造に対して適用する一連のアルゴリズムをカプセル化し、アルゴリズムの切替えを容易にする。 |

# 同一視

| パターン名 | 概要 |
| ---------- | ---- |
| Composite | 再帰的な構造を表現する。 |
| Decorator | あるインスタンスに対し、動的に付加機能を追加する。Filterとも呼ばれる。 |

# 構造を渡り歩く 

| パターン名 | 概要 |
| ---------- | ---- |
| Visitor | データ構造を保持するクラスと、それに対して処理を行うクラスを分離する。 | 
| Chain of Responsibility | イベントの送受信を行う複数のオブジェクトを鎖状につなぎ、それらの間をイベントが渡されてゆくようにする。 | 

# シンプルにする

| パターン名 | 概要 |
| ---------- | ---- |
| Facade | 複数のサブシステムの窓口となる共通のインタフェースを提供する。 |
| Mediator | オブジェクト間の相互作用を仲介するオブジェクトを定義し、オブジェクト間の結合度を低くする。 |


# 状態を管理する

| パターン名 | 概要 |
| ---------- | ---- |
| Observer | インスタンスの変化を他のインスタンスから監視できるようにする。Listenerとも呼ばれる。 | 
| Memento | データ構造に対する一連の操作のそれぞれを記録しておき、以前の状態の復帰または操作の再現が行えるようにする。 |
| State | オブジェクトの状態を変化させることで、処理内容を変えられるようにする。 |

# 無駄をなくす

| パターン名 | 概要 |
| ---------- | ---- |
| Flyweight | 多数のインスタンスを共有し、インスタンスの構築のための負荷を減らす。 |
| Proxy | 共通のインタフェースをもつインスタンスを内包し、利用者からのアクセスを代理する。Wrapperとも呼ばれる。 |

# クラスで表現する

| パターン名 | 概要 |
| ---------- | ---- |
| Command | 複数の異なる操作について、それぞれに対応するオブジェクトを用意し、オブジェクトを切り替えることで操作の切り替えを実現する。 |
| Interpreter | 構文解析のために、文法規則を反映するクラス構造を作る。 |
